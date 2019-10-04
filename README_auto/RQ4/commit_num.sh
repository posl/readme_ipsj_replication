#!/bin/sh

>data.csv
>data_all.csv

while read line
do

cur_dir=`pwd`
echo $line
cd ./repos/$line
number=$(git log --oneline README.md|wc -l)
num=$(git log --oneline |wc -l)
cd $cur_dir
echo $number >> data.csv
echo $num >> data_all.csv
done <project_name.csv
