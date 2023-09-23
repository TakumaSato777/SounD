from flask import *
from flask_cors import CORS

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

CORS(app)

# @api.after_request
# def after_request(response):
#   # response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

##以下はページ動作確認用
@app.route("/json")
def index():
    # JSONファイルの相対パス
    relative_path = "response_example.json"

    # ファイルを読み込み、JSONデータを取得
    try:
        with open(relative_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return "ファイルが見つかりません", 404
    except Exception as e:
        return str(e), 500

##Getメソッドによりidoとkeidoに応じた聖地を距離順で送信する。
@app.route('/seichiList', methods=['GET'])
def seichiList():
    try:
        ido = float(request.args.get('ido'))
        keido = float(request.args.get('keido'))

        #idoとkeidoから距離を計算して、距離順に直す処理を行い、JSONファイル化する。
        
        # JSONファイルの相対パス
        relative_path = "response_seichiList_example.json"

        # ファイルを読み込み、JSONデータを取得
        try:
            with open(relative_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return jsonify(data)
        except FileNotFoundError:
            return "ファイルが見つかりません", 404
        except Exception as e:
            print(e)
            return str(e), 500

    except ValueError:
        return jsonify({"error": "Invalid coordinates. Please provide valid floating-point numbers for 'ido' and 'keido'."}), 400


##GetメソッドによりIdに応じた曲のリストを取得する
@app.route('/kyokuList', methods=['GET'])
def kyokuList():
        
    try:
        id = float(request.args.get('id'))
        
        #Idに対応するファイルを検索し、JSONファイル化する。

        # JSONファイルの相対パス
        relative_path = "response_kyokuList_example.json"

        # ファイルを読み込み、JSONデータを取得
        try:
            with open(relative_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return jsonify(data)
        except FileNotFoundError:
            return "ファイルが見つかりません", 404
        except Exception as e:
            print(e)
            return str(e), 500
        
    except ValueError:
        return jsonify({"error": "Invalid coordinates. Please provide valid floating-point numbers for 'ido' and 'keido'."}), 400
    


if __name__ == "__main__":
    app.run(port=8888)



