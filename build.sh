#!/bin/bash

curl -L https://github.com/rust-lang/mdBook/releases/download/v0.4.25/mdbook-v0.4.25-x86_64-unknown-linux-gnu.tar.gz | tar xvz 
pip install -r requirements.txt
python main.py

