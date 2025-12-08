#include<stdio.h>
#include<stdlib.h>

int main(){

//Memory Allocation
    int *ptr;
    ptr=(int*)malloc(3*sizeof(int));
    ptr[0]=1;
    ptr[1]=2;
    ptr[2]=3;

    for(int i=0;i<3;i++){
        printf("%d\t",ptr[i]);
    }

//Calloc Allocation
    float *ptr2 = (float*)calloc(3,sizeof(float));
    for(int i=0;i<3;i++){
        printf("%f\t",ptr2[i]);
    }


//Reallocation Of Memory to increase or decrease size
    ptr=realloc(ptr,5);
    for(int i=0;i<5;i++){
        scanf("%d",&ptr[i]);
    }

    for(int i=0;i<5;i++){
        printf("%d\t",ptr[i]);
    }


//Free Allocted Memory
    free(ptr);
    free(ptr2);


    return 0;
}