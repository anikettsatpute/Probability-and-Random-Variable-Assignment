#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "coeff.h"

int main()
{

    printf("Mean is %lf\n" , mean("../Data/gau.dat"));
    printf("Variance is %lf\n" , variance("../Data/gau.dat"));
    return 0;
}