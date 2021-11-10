from flask import Flask, render_template
from models import make_db
import json
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_view():
    return render_template('hello.html', title='random_greeting')

# ランダムに挨拶を取得してjsonとして返す


@app.route('/greeting_post', methods=['POST'])
def greeting_process():
    # 先程作成したdbtool.pyのメソッド呼び出し
    result_greeting = make_db.get_random_greeting()
    return_json = {
        'greeting': result_greeting['greeting'],
        'image': result_greeting['image_path']
    }

    return jsonify(ResultSet=json.dumps(return_json))


if __name__ == '__main__':
    app.run(debug=True)
