#include<stdio.h>

int main(){
    int day;
    printf("enter day from 0 to 6 : ");
    scanf("%d",&day);

    switch (day){
        case 0: printf("Sunday");
                break;
        case 1: printf("monday");
                break;
        case 2: printf("tuesday");
                break;
        case 3: printf("wednesday");
                break;
        case 4: printf("thursday");
                break;
        case 5: printf("friday");
                break;
        case 6: printf("Saturday");
                break;
        default : printf(" no such day");


    }

    return 0;
}
//Nested possible