#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include "coeff.h"
int main()
{
    printf("Mean is %lf\n",mean("../Data/uni.dat"));
    printf("Variance is %lf\n",variance("../Data/uni.dat"));
    return 0;
}