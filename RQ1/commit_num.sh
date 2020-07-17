#!/bin/sh

>data.csv

while read line
do

cur_dir=`pwd`
echo $line
cd ./repos/$line
number=$(git log --oneline README.md|wc -l)
cd $cur_dir
echo $number >> data.csv
done <project_name.csv
