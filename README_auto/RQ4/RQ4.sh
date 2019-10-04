#!/bin/sh

#cd repos/
#sh clone.sh
#cd  ..

sh commit_num.sh

echo 0 > mode.csv
python create_ls.py

echo 1 > mode.csv
sh git.sh
python create_logfile.py
python create_ls.py

python issue-RQ4.py

