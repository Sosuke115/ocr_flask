from flask import Blueprint, request, jsonify
import base64
import io
import pytesseract
from PIL import Image

api = Blueprint("api", __name__)
text_db = {}


@api.route("/sync-process", methods=["POST"])
def process_sync():
    data = request.get_json(force=True)
    img_stream = io.BytesIO(base64.b64decode(data["image_data"]))
    img_stream = Image.open(img_stream)
    rec_string = pytesseract.image_to_string(img_stream)
    result = {"text": rec_string}
    return jsonify(result)


@api.route("/async-process", methods=["POST", "GET"])
def process_async():
    data = request.get_json(force=True)
    if request.method == "POST":
        # convert image to text
        img_stream = io.BytesIO(base64.b64decode(data["image_data"]))
        img_stream = Image.open(img_stream)
        rec_string = pytesseract.image_to_string(img_stream)
        # generate task_id
        task_id = str(len(text_db) + 1)
        # save text
        text_db[task_id] = rec_string
        result = {"task_id": task_id}
    else:
        task_id = data["task_id"]
        if task_id in text_db:
            result = {"task_id": text_db[task_id]}
        else:
            result = {"task_id": None}
    return jsonify(result)
