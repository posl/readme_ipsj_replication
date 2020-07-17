#!/bin/sh

num=`head -n 1 mode.csv`
echo $num

while read line
do
    cur_dir=`pwd`
    echo $line
    cd ./repos/$line
    # echo `pwd`
    # echo 'a'
    # READMEのコミットを五分割
    if [ $num -eq 1 ];then
        number=1
        tag=`git log --oneline -- README.md | tail -n 1 | cut -d ' ' -f 1 `
    else 
        number=`git log --oneline -- README.md | wc -l`
        number=$(($number* ($num-1)/4))
        tag=`git log --oneline -- README.md | tail -n $number | cut -d ' ' -f 1 | head -n 1`
    fi
    # echo 'b'
    # READMEの初期状態のタグの取り出し
    #tag=`git log --oneline -- README.md | tail -n 1 | cut -d ' ' -f 1`
    # numberのコミットのタグの取り出し
    # echo $tag
    # echo 'c'
    # README.mdをtagのバージョンに
    git checkout $tag README.md
    cd $cur_dir
done <project_name.csv

echo $number