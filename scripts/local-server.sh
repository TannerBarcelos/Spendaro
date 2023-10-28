#!/bin/sh

cd ../spendaro/api && pip install -r ./requirements/requirements-dev.txt
uvicorn server:app --reload