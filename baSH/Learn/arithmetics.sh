#!/bin/bash

a=10
b=2

mult_ab=$a*$b
echo $mult_ab

# Using let
let mult_ab=$a*$b
echo $mult_ab

# Using double brackets (())
echo "Addition = $(($a+$b))"

sub_ab=$(($a-$b))
echo $sub_ab

# Increment
let a++
echo $a

# Decrement
let a--
echo $a