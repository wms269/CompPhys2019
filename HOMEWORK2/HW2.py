import math
import numpy
import matplotlib.pyplot as plt
import scipy


#1
#6.11
def exp(x):
    exp = math.exp
    return exp

def func1(c, x):
    exp = math.exp
    func1 = 1-exp(-c*x)    
    return func1

def func2(c, x, om):
    func2 = (1+om)*func1(c, x)-om*x
    return func2

#6.11b

def relax(c, x):
    #overrelaxation method for finding x = 1-exp(-cx)
        q=0
        xold = 0
        while abs(x-xold)>10**-6:
            q=q+1
            xold = x            
            x = func1(c, x)
            print(abs(x-xold))

#6.11c

def overrelax1(c, x, om):
    #overrelaxation method for finding x = 1-exp(-cx)
        q=0
        xold = 0
        while abs(x-xold)>10**-6:
            q=q+1
            xold = x            
            x = func2(c, x, om)
            print(abs(x-xold))

#2
#6.13a
def func3(x):
    exp = math.exp    
    func3 = 5*exp(-x) + x - 5
    return func3

def binarysearch(l, r):
    while abs(l-r)>10**-6:
        sign1 = numpy.sign(func3(l))
        sign2 = numpy.sign(func3(r))
        xnew = (1/2)*(l+r)
        sign3 = numpy.sign(func3(xnew))
        if sign3==sign1:
            l = xnew
        else:
            r = xnew
    return xnew

def dispconst(l, r):
    h = 6.62607004*10**-34
    c = 3*10**8
    k = 1.38064852*10**-23
    b = h*c/(binarysearch(l,r)*k)
    print(b)
    return b
    
#6.13b
def sunT(l, r, lamb):
    T = dispconst(l,r)/(lamb)
    print(T)





#3

#2d test fcn

def func4(x,y):
    fxy = (x-2)**2+(y-2)**2
    return fxy

#2d grad

def grad2D(x, y, h1):
    a = []
    dfx = (func4(x+(h1/2), y)-func4(x-(h1/2), y))/h1 
    dfy = (func4(x, y+(h1/2))-func4(x, y-(h1/2)))/h1 
    a.append(dfx)
    a.append(dfy) 
    return a

#gradient descent method for 2d
def graddescent2D(x0, y0, gam, h1):
    an1 = [x0, y0]
    an0 = [0, 0]
    it = 0
    maxit=10**4
    b = []
    itvect = []

    while True:
        if abs(an0[0]-an1[0])<10**-6 and abs(an0[1]-an1[1])<10**-6:            
            return an1            
            break 
        if it>maxit:
            print('not converging')            
            break        
        it+=1       
        gradient = grad2D(an1[0], an1[1], h1)        
        an0[0] = an1[0]
        an0[1] = an1[1]
        an1[0] = an1[0]-gam*gradient[0]
        an1[1] = an1[1]-gam*gradient[1]
        itvect.append(it)        
        b.append(an1[0])
        print(it)
    plt.plot(itvect, b, 'r')
    plt.title('f(x) for each iteration')
    plt.show()

#global variable for chi squared values
chisquares = []

#3dgrad with chisquared

#Global variable for data data

data = numpy.loadtxt('HW2Data')    
logM = data[:,0]
expected = data[:,1]
err = data[:,2]
exp = math.exp
log = math.log10
M0 = 10**11

#x = phi star y= M star z= alpha

def schecter(x,y,z,M):    
    exp = math.exp    
    s0 = 10**(x)*(10**(M)/10**(y))**(z+1)*exp(-10**(M)/10**(y))*2.3
    return s0

def calcx2(x,y,z):
    chi2 = 0
    count = 0        
    for i in logM:      
        chi2 += (expected[count]-schecter(x,y,z,i))**2/(err[count])**2 
        count += 1 
    return chi2

def grad3D(x0, y0, z0, h1, h2, h3):
    gradvect = []
    dfx = (calcx2(x0+h1, y0, z0)-calcx2(x0-h1, y0, z0))/(2*h1) 
    dfy = (calcx2(x0, y0+h2, z0)-calcx2(x0, y0-h2, z0))/(2*h2)
    dfz = (calcx2(x0, y0, z0+h3)-calcx2(x0, y0, z0-h3))/(2*h3)
    gradvect.append(dfx)
    gradvect.append(dfy)
    gradvect.append(dfz)
    return gradvect

def graddescent3D(x0, y0, z0, h1, gam):
    an3 = [x0, y0, z0]

    an2 = [0,0,0]
    itvect = []
    a = []
    it = 0
    maxit=10**6
    while True:
        if abs(an2[0]-an3[0])<10**-6 and abs(an2[1]-an3[1])<10**-6 and abs(an2[2]-an3[2])<10**-6:                         
            print("wedidit")            
            break

        if it>maxit:
            print("not converging")
            break        
        it+=1
        itvect.append(it)        
        a.append(calcx2(an3[0],an3[1],an3[2]))
       
        #Calculate graident at starting point
        gradient = grad3D(an3[0], an3[1], an3[2], h1, h1, h1)
  
        #remember old values        
        an2[0] = an3[0]
        an2[1] = an3[1]
        an2[2] = an3[2]
        #get new valules        
        an3[0] = an3[0]-gam*gradient[0]
        an3[1] = an3[1]-gam*gradient[1]
        an3[2] = an3[2]-gam*gradient[2]
        print(abs(an2[0]-an3[0]), abs(an2[1]-an3[1]), abs(an2[1]-an3[1]))
    plt.plot(itvect, a, 'r')
    plt.title('Chi Squared for each iteration')
    plt.show()

    return an3



def initialplot(x0, y0, z0, gam, h1):
    params = graddescent3D(x0, y0, z0, gam, h1)   
    Mvect, finalfitvect, initialvect = [], [], []
    for i in logM:
        M = 10**i
        finalfit = schecter(params[0], params[1], params[2], i)
        initial = schecter(x0, y0, z0, i)
        Mvect.append(M)
        finalfitvect.append(finalfit)
        initialvect.append(initial)
    ax = plt.subplot(111)
    ax.plot(logM, finalfitvect, 'r', label='fit to the schetchter function')
    #ax.plot(logM, initialvect, 'g', label='initial guess to schechter function')    
    ax.scatter(logM, expected, label = 'measured values of n(Mgal)')
    ax.errorbar(logM, expected, yerr = err)
    plt.xlabel('Log(M Galaxy)')
    plt.ylabel('Log(Schechter)') 
    ax.legend()    
    plt.show()

def chi2vsit(x,y,z):
    a = []
    it = []    
    for i in range(10**6):
        it.append(i)        
        a.append(calcx2(x,y,z))
    plt.plot(it, a, 'r')
    plt.xlabel('iteration step')
    plt.ylabel('Chi Squared value')
    plt.show()
if __name__ == '__main__':
   # overrelax1(2, 1, 0.5)
   # binarysearch(1, 7)
   # dispconst(1, 7)
   # sunT(1,7, 502*10**-9)
   # graddescent2D(1, 1, 10**-1, 10**-2)
   # grad3D(-2.528, 1.122, -0.943, 0.01, 0.01, 0.01)
   # schecter(-3.2,10**11.5,-0.5,  1) 
   # graddescent3D(-2.5, 10.95, -3,10**-3, 10**-6)
    initialplot(-3.23, 12, -1.243,10**-5, 10**-6)
   # chi2vsit(-3.23, 11.95, -1.2)
