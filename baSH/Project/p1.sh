# write a script to throw dice and give user id if any die output is 6


#!/bin/bash

read -p "Enter number of dice to use : " num

until [[ $try_again == 0 ]]
do
    i=1
    try_again=1

    while [[ $i -le $num ]]
    do
        let die_out=$RANDOM%6+1
        echo "Output of die $i: $die_out"
        let i++

        if [[ $die_out -eq 6 ]]
        then
            echo "------------------------"
            echo "unlocked user id : $UID"
            echo "------------------------"

        fi

    done

    read -p "Press 0 to quit or try again : " try_again

done