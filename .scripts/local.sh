#!/bin/bash
cd src
rm -rf ./vendor
pipenv run chalice package build
sed -i '' 's/"CodeUri": ".\/deployment.zip"/"CodeUri": ".\/"/g' build/sam.json
sed -i '' 's/"Handler": "app.app"/"Handler": "local.app"/g' build/sam.json
pipenv run cfn-flip build/sam.json template.yml
pipenv run pip install -r <(pipenv lock -r) --target vendor/
printf "import sys\n\
import os\n\
sys.path.append(os.path.join(os.path.dirname(__file__), 'vendor'))\n\
from app import app\n\
app = app" > ./local.py
pipenv run sam local start-api -t template.yml -p 4000
