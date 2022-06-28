#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    FILE* fp;
    fp = fopen("3_1.dat","w");
    float numberArray[1000000];
    for(int i =0 ; i<1000000 ; i++)
    {
        double no = (double) rand()/RAND_MAX;
        double V,x;
        x = 1-no;
        V = -2*log(x);
        fprintf(fp,"%lf\n" , V);
    }
    fclose(fp);
    return 0;
}