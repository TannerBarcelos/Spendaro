#!/bin/sh

cd ../spendaro/api && pip install -r requirements.txt
uvicorn server:app --reload