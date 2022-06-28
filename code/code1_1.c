#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    FILE* fp;
    fp = fopen("uni.dat","w");
    for(int i =0 ; i<1000000 ; i++)
    {
        double no = (double) rand()/RAND_MAX;
        fprintf(fp,"%lf\n" , no);
    }
    fclose(fp);
    return 0;
}