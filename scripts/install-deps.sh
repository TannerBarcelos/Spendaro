#!/bin/sh

cd ../spendaro

cd api && pip install -r ./requirements/requirements-dev.txt
cd ..
cd client && npm install --verbose