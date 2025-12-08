/*
Write a program to remove blank spaces in a string
*/

#include<stdio.h>
#include<string.h>

void fun_remove_spaces(char *str){

    int j=0;

    for(int i=0;str[i]!='\0';i++){

        if(str[i] != ' '){
            str[j]=str[i];
            j++;
        }

    }
    str[j]='\0';
}

int main(){

    char str[100];
    fgets(str,100,stdin);

    fun_remove_spaces(str);
    puts(str);

    return 0;
}