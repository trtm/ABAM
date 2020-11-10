#!/bin/sh

cd data/

kaggle datasets download trtmio/aspect-based-argument-mining

unzip aspect-based-argument-mining.zip

rm aspect-based-argument-mining.zip

wc -l ABAM_SEGMENTS.tsv
wc -l ABAM_SENTENCES.tsv

cd ../

python3 src/data.py
