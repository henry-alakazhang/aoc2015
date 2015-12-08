#!/bin/sh

cat input.txt | sed 's/\\/\\\\/g' | sed 's/"/\\"/g' > 2.txt
len_o=`wc -c input.txt | cut -d\  -f1 `   
len_2=`wc -c 2.txt | cut -d\  -f1 ` 
lines=`wc -l input.txt | cut -d\  -f1 ` 
echo `expr $len_2 + $lines + $lines - $len_o`