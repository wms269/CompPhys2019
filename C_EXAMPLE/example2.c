#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include "nrutil.h"

struct part {
  float pos[3];
  float vel[3];
  float mass;
  int type;
} *P;

int main(int argc, char **argv)
{

  P = malloc(100*sizeof(struct part));
  P[50].pos[0] = 1.0;
  
}
