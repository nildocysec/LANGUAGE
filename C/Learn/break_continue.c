#include<stdio.h>

int main(){

    for(int i=0;i<10;i++){
        printf("%d\n",i);
        if(i==6){
            break;
        }
    }

    do{
        printf("Enter a number : ");
        int num;
        scanf("%d",&num);
        
        if(num%2==0 && num !=0){
            continue;
        }
        else if(num==0){
            break;
        }
        printf("%d\n",num);

    }while(1);

    return 0;
}