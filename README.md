# SounD
SounDはその場所にあった音楽を聴きたい、
聖地巡礼者向けの、
音楽提案アプリです。
これは特定の場所に行くとそのシーンに合った音楽を聴くことができ、
検索して音楽を聴くこととは違って、
検索の手間を省き、聖地への没入感を高める機能が備わっています。

このアプリケーションは株式会社レコチョクで9/16~9/17の二日間で開催されたハッカソンにおいて5人チームで作成しました。
バックエンドとフロントエンドの開発は分けて、私はフロントエンドを担当しました。


# DEMO

html上でユーザーから受け付けたリクエストをサーバーに送信し、サーバーから曲のリストを送り、その受け取った曲名とURLを表示するデモです。

https://github.com/TakumaSato777/SounD/assets/106140050/ddb3093e-2980-4f89-ba37-8870edb8f2e8


 
# Requirement

 
* flask
* flask_cors
 
# Installation
 Requirementのインストール方法
 
```bash
pip install flask_cors
pip install flask
```
 
# Usage
 
DEMO起動方法
1.backend_python.pyを起動
2.index.htmlを起動
3.聖地をクリックすると曲が表示される
 
```bash
python backend_python.py 
```

