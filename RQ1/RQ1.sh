#!/bin/sh

#cd repos/
#sh clone.sh
#cd  ..

sh commit_num.sh

echo 0 > mode.csv
python create_ls.py

sh git.sh
python create_logfile.py

echo 1 > mode.csv
python create_ls.py

python issue-RQ1.py

