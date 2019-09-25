#include <stdlib.h> //standard library
#include <stdio.h> //input/output library
#include <string.h> //string routines
#include <math.h> //math routines
#include "nrutil.h"

#define PI (1.0/3.0)

float trapzd(float (*func)(float), float a, float b, int n);

float func1(float x); //function prototype of func1 (for main to know)
int filesize(FILE *fp);
float func2(float x, float *y, float *vec);

// declare a structure of "type" particle
// make P a global variable
struct particle {
  float pos[3];
  float vel[3];
  float temp, density;
  int type;
} *P;


int main(int argc, char **argv) //command line arguments
{
  //argc is the number of arguments (including executable)
  //argv vector of strings that hold the arguments 0-indexed

  FILE *fp; // file pointer. 
  int N, i, k, ii[10];
  float x, f, etol,a=0,b=1, total, h, y, *vec, **vec2d, total_NR;
  float func1(float);

  // declare array of structures
  N = atoi(argv[1]);
  P = malloc(100*sizeof(struct particle)); // 100-element array of our structure "particle"
  fprintf(stderr,"Allocated memory for %d particles\n",N);
  P[0].pos[0] = 0;
  P[0].vel[0] = 0;
  P[0].temp = 100;
  P[0].density = 1.0E-6;
  fprintf(stderr,"Particle 0 has temp= %e\n",P[0].temp);

  
  vec = malloc(100*sizeof(float)); // 100-element array, 0-indexed
  //vec = calloc(100,sizeof(float)); // same as above, only now elements initialized to 0
  //vec = vector(-10,89); // numerical recipes declaration
  vec2d = matrix(1,100,1,100); // NR again.
  
  for(i=0;i<-100;++i)
    {
      vec[i] = i*i;
      vec2d[i][i] = vec[i];
      printf("%d %e\n",i,vec[i]);
    }

  x = func2(2.0,&y,vec);
  fprintf(stderr,"%e %e\n",x,y);

  a = 0;
  b = 1;
  
  if(argc<3)
    {
      fprintf(stderr,"Not enough arguments specified.\n");
      fprintf(stdout,"Not enough arguments specified.\n");
      exit(0);
    }
  
  N = atoi(argv[1]);
  //etol = atof(argv[2]);
  
  x = func1(2);
  fprintf(stdout,"f(2)=%f\n",x);
  printf("f(2)=%f\n",x); //equivalent to above (goes to stdout)

  h = (b-a)/N;
  total = 0;
  for(i=2;i<N;++i) // ++i => i=i+1
    {
      total += h*func1(a+i*h);
    }
  total += func1(a)/2*h;
  total += func1(b)/2*h;

  // let's compare to NR's trapedzoid method
  for(i=1;;i++)
    {
      total_NR = trapzd(func1, a, b, i);
      if(pow(2,i)>=N)break;
    }
  
  printf("%d %e %e %e\n\n\n\n",N,total,total_NR,fabs(total-PI)/PI);
  exit(0);
  
  // open a file for reading
  fp = fopen(argv[2],"r"); //fopen(filename,what-to-do-with-file)
  N = filesize(fp);
  fprintf(stderr,"There are %d lines in file [%s]\n",N, argv[2]);
  
  for(i=1;i<=N;++i)
    {
      //fscanf(fp,"%d %d",&j,&k);
      fscanf(fp,"%d %d",&ii[0],&ii[1]);
      printf("%d %d\n\n",ii[0],ii[1]);
    }
  
  // %d - integer
  // %e - exponential
  // %f - float number
  // %c - character
  // %s - string
  // %ld - long integer
  // %lf - double precision float
  // \n carriage return
  // \t tab
  
}

float func1(float x)
{
  float y;
  y = x*x;
  return y;
}

int filesize(FILE *fp)
{
  int i=-1;
  char a[1000];

  while(!feof(fp))
    {
      i++;
      fgets(a,1000,fp); //gets is "get a string" "f" mean from a file
    }
  rewind(fp);
  return(i);
}

float func2(float x, float *y, float *vec)
{
  *y = exp(x*vec[10]); // "the thing that y points to" ie address in memory
  vec[11] = sqrt(x); // can change the values inside the array within the function
  return x*x;
}
  
