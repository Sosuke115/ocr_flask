# OCR system

OCR API implemented with flask and pytesseract


# Usage

##### build docker image
```bash
docker build -t ocr_server docker
```

##### run image processing (optional)
```bash
docker run --rm -it -d -v $(pwd):/work -w /work --name image_encoder -p 8080:8080 ocr_server sh -c "python encode.py images/sample.tif"
```

##### run server
```bash
docker run -it -d -v $(pwd):/work -w /work --name ocr_server -p 5000:5000 ocr_server sh -c "python run.py"
```

<!-- ```bash
cd ocr_flask
./run.sh
``` -->

##### process (all)

```bash
curl -XPOST "http://localhost:5000/sync-process" -d '{"image_data": "<encoded image (base 64)>"}'
```
or
```bash
curl -XPOST "http://localhost:5000/sync-process" -d @encoded/encode.json
```

##### process (image to task id)

```bash
curl -XPOST "http://localhost:5000/async-process" -d '{"image_data": "<encoded image (base 64)>"}'
```
or 
```bash
curl -XPOST "http://localhost:5000/async-process" -d @encoded/encode.json
```



##### process (task id to text)
 

```bash
curl -XGET "http://localhost:5000/async-process" -d '{"task_id": "<task id as received from POST /image>"}'
```

# Example result
```bash
$ curl -XPOST "http://localhost:5000/sync-process" -d @encoded/encode.json
{
  "text": "| have a lot of money\n\f"
}
```

# Author
 
* Sosuke
* website : https://sosuke115.github.io
* Twitter : https://twitter.com/ponyo_ponyo115

Thank you!



