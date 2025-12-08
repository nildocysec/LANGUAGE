/*
print such pattern.

*****
*****
*****
*****

*/

#include<stdio.h>

void fun_pattern(int length, int height){
    int i,j;
    for(i=0;i<height;i++){
        printf("\n");
        for(j=0;j<length;j++){
            printf(" *");
        }
    }
}

int main(){
    int height,length;
    printf("ENter length and height of pattern : ");
    scanf("%d",&length);
    scanf("%d",&height);

    fun_pattern(length,height);

    return 0;
}