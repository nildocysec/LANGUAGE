#!/bin/bash

mystr="welcome @ 11"

# Length 
echo ${#mystr}

# Make Upper case
echo ${mystr^^}

# Make Lower case
echo ${mystr,,}

# Replace
mystr=${mystr/welcome/NEW_welcome}
echo ${mystr}

# Slicing
slicestr=${mystr:2:7}
echo ${slicestr}