#!/bin/bash

read -p "Enter age : " age

if [[ $age < 18 ]]
then
    echo "Minor"

elif [[ $age > 18 ]]
then
    echo "Major"

else
    echo "wait.. voter id in process.."

fi