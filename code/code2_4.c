#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{

    FILE* fp;
    fp = fopen("gau.dat","r");

    double numberArray[1000000];
    double sum = 0.0,sum_var = 0.0;

    for (int i = 0; i < 1000000; i++)
    {
        fscanf(fp, "%lf", &numberArray[i]);
    }
    for (int i = 0; i < 1000000; i++)
    {
        sum+=numberArray[i];
    }
    double mean = (sum/1000000);
    printf("Mean is %lf\n", mean);
    for (int i = 0; i < 1000000; i++)
    {
        sum_var += (numberArray[i]-mean)*(numberArray[i]-mean);
    }
    double var = (sum_var/1000000);
    printf("Variance is %lf\n", var);
    fclose(fp);
    return 0;
}