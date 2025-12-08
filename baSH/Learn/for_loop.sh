#!/bin/bash

for i in 1 2 3 4 5
do
    echo $i
done

for j in my name is @ 14
do
    echo $j
done

for k in {1..10}
do
    echo $k
done

# File Path
items="filename.txt"
for i in $(cat $items)
do
    echo $i
done

myarray=(1 2 3 hello "hi")
length=${#myarray[*]}
for (( i=0;i<length;i++))
do
    echo ${myarray[i]}
done