hd= /home/tinker


CC= gcc
CLINK= gcc 
CLIB= -L${HOME}/cosmo/lib -lm 
XDIR= $(HOME)/exec
CFLAGS = -O3

OBJS1=	example.o nrutil.o trapzd.o
example:	$(OBJS1)
	$(CLINK) $(CFLAGS) -o $@ $(OBJS1) $(CLIB)
#	cp $@ $(HOME)/exec/


