#!/bin/sh

cat input.txt | sed 's/\\\\/\//g' | sed 's/\\"/(/g' | sed 's/"//g' | sed 's/\\x.//g' > 1.txt
len_o=`wc -c input.txt | cut -d\  -f1 `   
len_1=`wc -c 1.txt | cut -d\  -f1 ` 
echo `expr $len_o - $len_1`