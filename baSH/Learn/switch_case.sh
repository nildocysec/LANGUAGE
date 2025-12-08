#!/bin/bash

echo "a) date"
echo "2) ls"
echo "6.6) hostname"
read -p "Enter  your choice : " ch

case $ch in
    a)date;;

    2)  
        ls
        pwd
        ;;

    6.6)hostname;;

    *)
        echo "Invalid choice"
        echo "Re run program"

esac