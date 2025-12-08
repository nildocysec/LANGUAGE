#include<stdio.h>

//Function Declaration Or Prototype
int fun_square(int num);

int fun_power(int num, int exponent){
    
    int result=1,i;
    for(i=1;i<=exponent;i++){
        result*=num;
    }

    return result;
}

int main(){

    int num;
    printf("Enter a number to square\n");
    scanf("%d",&num);
    //Function call
    int square=fun_square(num);
    printf("%d is square if %d \n",square,num);

    int exponent;
    printf("Enter power : ");
    scanf("%d",&exponent);
    int result=fun_power(num,exponent);
    printf("%d to the power %d is %d \n",num,exponent,result);



    return 0;
}

//Function Definition
int fun_square(int num){

    int square=num*num;
    return square;

}