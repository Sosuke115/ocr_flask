#!/bin/sh
echo "building docker image"
docker build -t ocr_server docker

echo "running image processing"
docker run --rm -it -d -v $(pwd):/work -w /work --name image_encoder \
-p 8080:8080 ocr_server sh -c "python encode.py images/phototest2.tif"

echo "running server"
docker run -it -d -v $(pwd):/work -w /work --name ocr_server \
-p 5000:5000 ocr_server sh -c "python run.py"
