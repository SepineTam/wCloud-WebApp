#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : load.py

def load_stopwords(filepath='static/base/stopwords/default_stopwords.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = {line.strip() for line in f if line.strip()}
    return stopwords

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


if __name__ == '__main__':
    stopwords = load_stopwords("../../default/stopwords/default_stopwords.txt")
    print(stopwords)
