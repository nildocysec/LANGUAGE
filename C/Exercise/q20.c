/*
Write a program to print the highest frequency character in a string.
*/

#include<stdio.h>
#include<string.h>

void fun_highest_frequency_character(char *str){

    int size=strlen(str);
    int f1,f2=0;
    char f_char;

    for(int i=0;i<size;i++){
        f1=0;
        for(int j=i;j<size;j++){

            if(str[i]==str[j]){
                f1++;
            }
        }

        if(f1>f2){
            f2=f1;
            f_char=str[i];
        }
    }

    if(f_char==' '){
        printf("Highest frequency is of SPACE.\n");
    }
    else printf("Highest frequency is of : %c",f_char);
}

int main(){

    char str[100];
    fgets(str,100,stdin);

    fun_highest_frequency_character(str);

    return 0;
}
