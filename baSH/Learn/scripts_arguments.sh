#!/bin/bash

# Access arguments
echo "First : $1"
echo "second : $2"

echo "All arguments entered : $@"

echo "number of arguments entered : $#"

for idx in $@
do
    echo "typing : $idx"
    echo "---------"
done

# Shifting arguments
echo "creating user $1"
shift                   # put all except first argument in next argument
echo "Description : $@"
