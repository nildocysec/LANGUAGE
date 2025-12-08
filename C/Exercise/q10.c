/*
Write a program to print prime numbers in a range.
*/

#include<stdio.h>

int fun_check_prime_number(int n){
    for(int i=2;i<n;i++){
        if(n%i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    int starting,ending;
    printf("Enter range from to : ");
    scanf("%d",&starting);
    scanf("%d",&ending);

    for(int i=starting;i<ending;i++){

        int result = fun_check_prime_number(i);
        if(result==1){
            printf("%d\n",i);
        }
    
    }

    return 0;

}