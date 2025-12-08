#include<stdio.h>

int main(){

    int i=1,n;
    printf("Enter number to print its table : ");
    scanf("%d",&n);

    while(i<11){
        printf("%d\n",n*i);
        i++;
    }


    return 0;

}