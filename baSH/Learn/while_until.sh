#!/bin/bash

num=2
count=0

# Run when condition True
while [[ $count -le 10 ]]
do
    echo "$num X $count = $(($num*$count))"
    let count++
done


num=0
count=0
# RUn when condition False
until [[ $count -ge 10 ]]
do
    echo $(($num+$count))
    let count++
done

# # Infinite loop
# while true
# do
#     echo "Working.."
#     sleep 1s
# done

# Read content from file
while read item
do
    echo $item
done < hello_world.sh

# Read from csv file
while IFS="," read name age city
do
    echo $name " " $age " " $city
done < csvfile.csv