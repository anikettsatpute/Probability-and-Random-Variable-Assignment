//Function declaration
double **createMat(int m,int n);
void readMat(double **p, int m,int n);
void print(double **p,int m,int n);
double **loadtxt(char *str,int m,int n);
double linalg_norm(double **a, int m);
double **linalg_sub(double **a, double **b, int m, int n);
double **linalg_inv(double **mat, int m);
double **matmul(double **a, double **b, int m, int n, int p);
double **transpose(double **a,  int m, int n);
void uniform(char *str, int len);
void gaussian(char *str, int len);
double mean(char *str);
//End function declaration


//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


//Defining the function for reading matrix 
void readMat(double **p, int m,int n)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix

//Read  matrix from file
double **loadtxt(char *str,int m,int n)
{
FILE *fp;
double **a;
int i,j;


a = createMat(m,n);
fp = fopen(str, "r");

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   fscanf(fp,"%lf",&a[i][j]);
  }
 }
//End function for reading matrix from file

fclose(fp);
 return a;

}


//Defining the function for printing
void print(double **p, int m,int n)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf \n",p[i][j]);
 }
}
//End function for printing

//Defining the function for norm

/*double linalg_norm(double **a, int m)
{
int i;
double norm=0.0;

 for(i=0;i<m;i++)
 {
norm = norm + a[i][0]*a[i][0];
}
return sqrt(norm);

}*/
//End function for norm

//Defining the function for difference of matrices

double **linalg_sub(double **a, double **b, int m, int n)
{
int i, j;
double **c;
c = createMat(m,n);

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
c[i][j]= a[i][j]-b[i][j];
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for inverse of 2x2 matrix


double **linalg_inv(double **mat, int m)
{
double **c, det;
c = createMat(m,m);

det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];

c[0][0] = mat[1][1]/det;
c[0][1] = -mat[1][0]/det;
c[1][0] = -mat[0][1]/det;
c[1][1] = mat[0][0]/det;

return c;

}
// End  function for inverse of 2x2 matrix


//Defining the function for difference of matrices

double **matmul(double **a, double **b, int m, int n, int p)
{
int i, j, k;
double **c, temp =0;
c = createMat(m,p);

 for(i=0;i<m;i++)
 {
  for(k=0;k<p;k++)
  {
    for(j=0;j<n;j++)
    {
	temp= temp+a[i][j]*b[j][k];
    }
	c[i][k]=temp;
	temp = 0;
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for transpose of matrix

double **transpose(double **a,  int m, int n)
{
int i, j;
double **c;
//printf("I am here");
c = createMat(n,m);

 for(i=0;i<n;i++)
 {
  for(j=0;j<m;j++)
  {
c[i][j]= a[j][i];
//  printf("%lf ",c[i][j]);
  }
 }
return c;

}
//End function for transpose of matrix

//Defining the function for generating uniform random numbers
void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
  double temp = (double)rand()/RAND_MAX;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating uniform random numbers

//Defining the function for calculating the mean of random numbers
double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i-1);
return temp;
}
//End function for calculating the mean of random numbers

//Defining the function for generating Gaussian random numbers
void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{  
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating Gaussian random numbers

//Defining the function for calculating variance of random numbers
double variance(char *str)
{
  FILE* fp;
    fp = fopen(str,"r");

    double x,temp=0.0;
    int i=0;
    while(fscanf(fp,"%lf",&x)!=EOF)
    {
        i=i+1;
        temp = temp+x*x;
    }
    double var;
    var = temp/(i-1);
    fclose(fp);
    return var;
}
//End function for calculating the variance of random or gaussian numbers

//Begin Creating a random number.
double create_rand()
{

  double sum_var;
  sum_var = (double)rand()/RAND_MAX;
  return sum_var;
}
//end Creating a random number.

//Defining a function to generate sum of two random numbers
void sum_uniform(char *str,int len)
{
    int i;
    FILE *fp;
    fp = fopen(str,"w");
    //Generate numbers
    for (i = 0; i < len; i++)
    {
        double temp = create_rand()+create_rand();
        fprintf(fp,"%lf\n",temp);
    }
    fclose(fp);
}
//End  function to generate sum of two random numbers


//defining function to craeate equiprobable -1 and 1

void equiprobable5_1(char *str , int len)
{
  FILE *fp;
  fp = fopen(str,"w");
    //Generate 1 or -1
    for (int i = 0; i < len; i++)
    {
      double temp = ((double)rand()/RAND_MAX);
      if(temp>0.5){
        fprintf(fp,"%d\n",1);
      }
      else{
        fprintf(fp,"%d\n",-1);
      }
    }
    fclose(fp);
}

//Endfunction to craeate equiprobable -1 and 1

//begin function for maxlike number generator
void maxlike_gen_5_2(char *str,double a)
{
  FILE *fp1;
  FILE *fp2;
  FILE *fp3;
  double x,N,temp;
  fp3 = fopen("../Data/gau.dat","r");
  fp2 = fopen("../Data/5_1.dat","r");
  fp1 = fopen(str,"w");
  while(fscanf(fp3,"%lf",&x)!=EOF)
    {
        fscanf(fp2,"%lf",&N);
        temp = a*N + x;
        fprintf(fp1,"%lf\n",temp);
    }
    fclose(fp1);
    fclose(fp2);
    fclose(fp3);
}
//end function for maxlike number generator

//Begin conditional Probability in question 5.5
void Probe_5_5()
{
  FILE *fp1;
  FILE *fp2;
  double y;
  double x;
  double count1=0.0,count2=0.0,base1=0.0,base2=0.0;
  fp1 = fopen("../Data/5_2.dat","r");
  fp2 = fopen("../Data/5_1.dat","r");
  
  while(fscanf(fp1,"%lf",&y)!=EOF)
  {
    fscanf(fp2,"%lf",&x);
    if((x==1) && (y<0)){
      count1++;
      base1++;
    }
    else if((x==-1) && (y>0)){
      count2++;
      base2++;
    }
    else if(x==1){
      base1++;
    }
    else {
      base2++;
    }
  }
  double prob1,prob2;
  prob1=(count1/base1);
  prob2=(count2/base2);

  printf("$P_{e|0}$ = %lf\n",prob1);
  printf("$P_{e|1}$ = %lf\n",prob2);
}
//End conditional Probability in question 5.5

//declaring function which generates sum of square of gaussian
void sum_square_gen(char *str,char *temp1,char *temp2)
{
  FILE *fp;
  FILE *fp1;
  FILE *fp2;
  fp1 = fopen(temp1,"r");
  fp2 = fopen(temp2,"r");
  fp  = fopen(str,"w");

  double x_1,x_2;

  while(fscanf(fp1,"%lf",&x_1)!=EOF)
  {
    fscanf(fp2,"%lf",&x_2);
    double temp;
    temp = x_1*x_1 + x_2*x_2;
    fprintf(fp,"%lf\n",temp);
  }
  fclose(fp);
  fclose(fp1);
  fclose(fp2);
}
//end function which generates sum of square of gaussian