#!/bin/sh

cd ../spendaro

cd api && pip install -r requirements.txt
cd ..
cd client && npm install --verbose