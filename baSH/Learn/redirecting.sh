#!/bin/bash

set -x

# Over Write in File >
touch newfile.txt
date > newfile.txt
pwd > newfile.txt

# Append in File >>
date >> newfile.txt
ping -c 1 www.google.com >> newfile.txt

# Neither store in file nor on terminal
hostname &> /dev/null

# Script name
echo $0