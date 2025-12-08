#include<stdio.h>

int main (){

    int age;
    printf("enter age :");
    scanf("%d",&age);
    
    if(age<18){
        printf("You are minor !\n");
    }
    else if (age>=18 && age<=35){
        printf("You should work hard !\n");
    }
    else{
        printf("You can be president !!\n");
    }    

    
    (age>35) ? printf("Can be president\n") : printf("can not be president\n");


    return 0;
}
//Nested possible
