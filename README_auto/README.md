Readme auto
===========

使い方
-----
1. Readme autoをクローン  
2. 再現したいRQに対応したディレクトリを開く  
3. '$ sh init.sh'とコマンド入力  
4. 'based_list.csv'や'first_list.csv'が消えていることを確認する  
5. '$ sh (RQ~のようなディレクトリ名).sh'を実行  
6. 'RQ~_result.csv'に結果が出力されている  

その他生成物
-----------
・based_list.csv → dataset_combined(pranaデータより入手)を分析し、プロジェクト毎にコミット数やセクションの種別をまとめたもの  
・~_list.csv → 各プロジェクトの特定のバージョン(first_listなら初期バージョン)に対応したbased_listと同じ形式のファイル  
・dataset_combined_cp.csv,mode.csv → 実験の過程で生成・利用するファイル  

各操作ファイル(sh,python)の説明
----------------------------
・repos/clone.sh ・・・ repos内に実験用リポジトリをクローンする  
・git.sh ・・・ repos内のレポジトリのバージョンを変更する  
・create_logfile.py ・・・ 現在のリポジトリのバージョンに応じたデータセットを生成する  
・create_ls.py ・・・データセットからプロジェクト毎の様々な情報を抽出する  
・issue-RQ~.py ・・・データを集計し結果を出力する  
・commit_num.sh ・・・ 各リポジトリのコミット数を調べる  
・RQ~.sh ・・・ 実験を再現する  
・init.sh ・・・ 初期化する  

備考
----
・クローンの行程は30分から60分かかるので再現実験の行程から省いた  
・元となっている佐渡嶋先輩の実験はここ → https://github.com/posl/sadoshima_readme  
・改良可能箇所として、RQ~.shおよびinit.shにクローンの行程を盛り込むことができるはず  
・クローン時にproxyうんたらのようなエラーが出た時は以下を実行  
$ git config --global --unset http.proxy  
これで治らない場合は原因不明  
