# Flaskとrender_template関数をFlaskライブラリからインポート
from flask import Flask, render_template

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# テストページの表示
@app.route('/test')
def test():
    return render_template('test.html')

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

# チャット一覧画面ページの表示
@app.route('/chat_list')
def chat_list():
    return render_template('chat_list.html')

# チャット画面ページの表示
@app.route('/chat')
def chat():
    return render_template('chat.html')

# チャット一覧画面ページの表示
@app.route('/matching')
def matching():
    return render_template('matching.html')

# チャット画面ページの表示
@app.route('/request_list')
def request_list():
    return render_template('request_list.html')

# プロフィール画面ページの表示
@app.route('/profile')
def profile():
    return render_template('profile.html')

# プロフィール編集画面ページの表示
@app.route('/profile_edit')
def profile_edit():
    return render_template('profile_edit.html')

# アプリケーションを実行。ホストを'0.0.0.0'に設定し、ポート5001でリッスン。デバッグモードを有効にする
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)