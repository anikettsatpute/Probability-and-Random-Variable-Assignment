#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeff.h"

int main()

{

    gaussian("../Data/temp1.dat",1000000);
    gaussian("../Data/temp2.dat",1000000);
    sum_square_gen("../Data/6_1.dat","../Data/temp1.dat","../Data/temp2.dat");
    return 0;

}