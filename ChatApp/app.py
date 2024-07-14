# Flaskとrender_template関数をFlaskライブラリからインポート
from flask import Flask, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# cssのページの表示
@app.route('/')
def test():
    return render_template('sample.html')

# ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')

# 新規会員登録ページの表示
@app.route('/signup')
def signup():
    return render_template('registration/signup.html')

# ホーム画面ページの表示
@app.route('/home')
def home():
    return render_template('home.html')

# アプリケーションを実行。ホストを'0.0.0.0'に設定し、ポート5001でリッスン。デバッグモードを有効にする
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)