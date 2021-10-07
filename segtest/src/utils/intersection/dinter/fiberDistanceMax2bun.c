#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "bundleTools.h"
#include "BundleTools.c"

int main(int argc, char *argv[])
{
   clock_t t_ini,t_fin;
   t_ini=clock();
   double t_segundos;
   if(argc==5)
   {
    struct bundle f1;
    struct bundle f2;
    f1=read_bundle(argv[1]);
	printf("\n\n Leida f1: %i \n\n",f1.nfibers);
    f2=read_bundle(argv[2]);
	printf("\n\n Leida f2: %i \n\n",f2.nfibers);
	
    int i,j;

    float menor=1000.0;

    //char nametxt[largo];
    
	//printf("\n\n Leida f2: %i \n\n",f2.nfibers);
	
    float** m = (float**) malloc (f1.nfibers*sizeof(float*));
    for(i=0;i<f1.nfibers;i++)
	m[i] = (float*) malloc(f2.nfibers*sizeof(float));

    m=fiberDistanceMax2bun(f1,f2);

    FILE *fw;
    fw = fopen(argv[3],"a+b");

    if (strcmp(argv[4],"1") == 0){fprintf(fw,"\n");}

    
    for(i=0;i<f1.nfibers;i++)
    {
        for(j=0;j<f2.nfibers;j++)
        {
	     if(sqrt(*(m[i]+j))<= menor){menor=sqrt(*(m[i]+j));}

        }
   
    }
    fprintf(fw, "%f\t",menor);
    //fprintf(fw, "%s %f\t",nametxt,menor);
   

    fclose(fw);

   }
   else{printf("Cantidad invalida de argumentos\n");}
   t_fin=clock();
   t_segundos=(double)(t_fin-t_ini)/CLOCKS_PER_SEC;	
   //printf("Demora en segundos: %16g \n",t_segundos);
   printf("Demora en segundos: %f\n",t_segundos);
   return 0;
}
