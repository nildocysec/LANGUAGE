#!/bin/bash

echo "India"
echo "USA"
read -p "Enter Country : " country
read -p "Enter age : " age

if [[ $country == "India" ]] && [[ $age -gt 18 ]]
then
    echo "You can vote"
elif [[ $country == "USA" ]] && [[ $age -ge 18 ]]
then
    echo "You can vote"
else
    echo "You can not vote"

fi

# && for AND
# || for OR
# ! for NOT

# Ternary
marks=5
[[ $marks -le 5 ]] && echo "Failed !!" || echo "Passed :D"