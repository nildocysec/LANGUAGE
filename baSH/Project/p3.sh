# This program archive larger files from given path


#!/bin/bash

# Archive location and conditions
out_path="/home/ratri0kali/LANGUAGE/baSH/Project/Archives"
depth=1

# Target location to find files
in_path=$1
if [[ -d $in_path ]]
then
    cd $in_path
    echo "Entered in $(pwd)"

else
    echo "Given path no found. Please check and try again"

fi  

# Find files and archive
for i in `find $in_path -maxdepth $depth -type f -size +50k`
do
    echo "[$(date "+%Y-%m-%d %H:%M:%S")] archiving $i ==> $out_path"
    gzip $i || exit 1
    mv $i.gz $out_path || exit 1
    echo "Done for $i"
    

done