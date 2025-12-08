#include<stdio.h>

void main(){
    printf("Hello World ! \n");
    
    int age = 22;
    float rating = 4.5;
    char name = 'N';

    printf("age is %d \n",age);         // \n gives newline \t gives newtab
    printf("name is %c \n",name);
    printf("rating is %f \n",rating);

    /* 
    printf print data
    scanf read data from keyboard
    */

    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    printf("sum is : %d",a+b);

}