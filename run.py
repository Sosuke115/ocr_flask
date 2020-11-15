from flask import Flask, jsonify
from api import api

# Flask本体
app = Flask(__name__)

# Blueprint登録
app.register_blueprint(api)


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    result = {
        "error": {
            "type": error.name,
            "message": error.description,
            "status_code": error.code,
        }
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)