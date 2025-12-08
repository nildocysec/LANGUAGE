#include<stdio.h>

int main(){

    for (int i=0;i<5;i++){
        printf("Hello_%d \n",i);
    }

    for(int i=10;i>5;i--){
        printf("%d \n",i);
    }

    for(char ch='a';ch<'i';ch++){
        printf("%c \n",ch);
    }

    for(float f=1.0;f<5.0;f++){
        printf("%f\n",f);
    }


    return 0;
}