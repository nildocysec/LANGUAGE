#!/bin/bash



for i in {1..20}
do
    if [[ $(($i%2)) -ne 0 ]]
    then
        echo $i

    elif [[ $i -gt 13 ]]
    then
        break #break loop

    else
        continue # Skip for current iteration

    fi

done



