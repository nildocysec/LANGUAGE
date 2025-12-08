#!/bin/bash

myarray=(1 2 hello "hi" 9.2)
echo "element at index 2 : ${myarray[2]}"
echo ${myarray[1]}
echo "All array elements : ${myarray[*]}"

# Length of an array
echo ${#myarray[*]}

# Slicing
echo "values of 2 elements from index 1 = ${myarray[*]:1:2}"

# add elements at end of an array
myarray+=("new" 6 7.7)
echo ${myarray[*]}

# Key and Value
declare -A newarray                     # Declare an array
newarray=([name]="nil" [age]=22)        # Initialize an array
echo ${newarray[name]}                  # Print value using key

