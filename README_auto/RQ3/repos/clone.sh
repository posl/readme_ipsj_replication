#!/bin/sh

cd ../repos
str=".git"
str1="https://yuki-sadoshima:1c83417e749e03c77e53102329cea97f947836a1@"

while read line
do
url=`echo $line | cut -d',' -f3`
cloneurl=$str1$url$str
git clone $cloneurl
done <dataset_combined.csv