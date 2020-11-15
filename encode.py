import base64
import json
import click


@click.command()
@click.argument("file_path")
def encode_base64(file_path):
    encode_file = r"encoded/encode.json"

    with open(file_path, "rb") as f:
        data = f.read()

    # encode image with base64
    encode_bytes = base64.b64encode(data)
    encode_str = encode_bytes.decode("utf-8")

    request_json = {"image_data": encode_str}

    with open(encode_file, "w") as f:
        json.dump(request_json, f)


if __name__ == "__main__":
    encode_base64()