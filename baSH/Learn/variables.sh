#!/bin/bash

name="nil"
age=22
rating=4.5

echo "my name is : $name"
echo $age
echo $rating

age=25
echo "new age is : $age"

echo $(hostname)        # output of a command

readonly constant_variable="kali"       # value of constant variable can not be reassigned
echo $constant_variable

