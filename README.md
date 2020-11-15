### ocr_flask

OCR API implemented with flask


### Usage

```bash
cd ocr_flask
./run.sh
```

##### process (all)

```bash
curl -XPOST "http://localhost:5000/image-sync" \
-d '{"image_data": "<b64 encoded image>"}'
```
or
```bash
curl -XPOST "http://localhost:5000/image-sync" \
-d @encoded/encode.json
```

##### process (image to task id)

```bash
curl -XPOST "http://localhost:5000/image" \
-d '{"image_data": "<b64 encoded image>"}'
```
or 
```bash
curl -XPOST "http://localhost:5000/image" \
-d @encoded/encode.json
```




##### process (task id to text)
 

```bash
curl -XGET "http://localhost:5000/image" \
-d '{"task_id": "<task id as received from POST /image>"}'
```






