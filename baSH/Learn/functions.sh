#!/bin/bash

# Function Definition
function fun_my_info1 {
    name="nil"
    age=22
    echo "Welcome to My Info 1 : "
    echo $name
    echo $age
}

# Function Call
fun_my_info1

# Function Definition
fun_my_info2() {
    name="nil"
    age=22
    echo "Welcome to My Info 2 : "
    echo $name
    echo $age
}

# Function Call
fun_my_info2

# Function with arguments
fun_sum() {
    local num1=$1
    local num2=$2
    sum=$(($num1+$num2))
    echo "sum = $sum"
}

# Call function with arguments
fun_sum 22 25

# local variable bounded to function or its loop
echo $num1
echo $num2
