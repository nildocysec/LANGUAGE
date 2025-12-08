#include<stdio.h>

int fun_hello(int count){

    if(count<=0){
        return 0;
    }

    printf("Hello\n");
    fun_hello(count-1);
    
}

int fun_sum_natural_num(int num){
    int sum;
    if(num==1){
        return 1;
    } 
    sum= num + fun_sum_natural_num(num-1);
    return sum;
}

int fun_factorial(int num){

    int fact;
    if(num==0){
        return 1;
    }
    fact=num*fun_factorial(num-1);
    return fact;

}

int fun_fibonacci(int n){
    if(n==0){
        return 0;
    }
    if(n==1){
        return 1;
    }
    int fibNm1=fun_fibonacci(n-1);
    int fibNm2=fun_fibonacci(n-2);
    int fibN=fibNm1 + fibNm2;
    
    return fibN;
}

int main(){

    fun_hello(5);
    
    int sum=fun_sum_natural_num(10);
    printf("Sum is %d\n",sum);

    int fact=fun_factorial(7);
    printf("factorial is : %d\n",fact);

    int fibonacci=fun_fibonacci(5);
    printf("fibonacci is : %d\n",fibonacci);

    return 0;
}