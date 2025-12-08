/*
Write a program to convert all lowercase alphabets to uppercase in a string.
*/

#include<stdio.h>
#include<string.h>

void fun_lower_to_upper(char *str){

    int size;
    size=strlen(str);
    for(int i=0;i<size;i++){
        if(str[i] >= 'a' && str[i] <='z'){
            str[i] = str[i] - 32;
        }
    }

}

int main(){

    char str[100];
    fgets(str,100,stdin);

    fun_lower_to_upper(str);
    puts(str);

    return 0;
}