# Flaskとrender_template関数をFlaskライブラリからインポート
from flask import Flask, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')

@app.route('/')
def test():
    return render_template('sample.html')

# アプリケーションを実行。ホストを'0.0.0.0'に設定し、ポート5001でリッスン。デバッグモードを有効にする
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)