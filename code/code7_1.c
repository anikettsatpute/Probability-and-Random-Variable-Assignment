#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "./coeff.h"

int  main(void) //main function begins
{
double gamma;
double j;
int i;
char file[30];

// ral distribution for 20 different values of gamma
for(i=0;i<15;i++) {
    j = (double)i;
    gamma = pow(10,j/10.0);
    sprintf(file,"../Data/7_1/%d.dat",i);
    gen_7_1(file,gamma);
}

return 0;
}