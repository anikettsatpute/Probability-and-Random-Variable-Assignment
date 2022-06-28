#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double generator()
{
    double X;
    float sum=0.0;
    for(int i=0 ; i<12 ;i++)
    {
        double no = (double) rand()/RAND_MAX;
        sum+= no;
    }
    X = sum - 6;
    return X;
}

int main()
{
    FILE* fp;
    fp = fopen("gau.dat","w");
    for(int i =0 ; i<1000000 ; i++)
    {
        fprintf(fp,"%lf\n" , generator());
    }
    fclose(fp);
    return 0;
}