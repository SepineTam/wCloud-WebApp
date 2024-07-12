#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : app.py
import time

from flask import Flask, render_template, request, send_from_directory
import os
# import time

from wCloud import generate
from Config import *

app = Flask(__name__)

BASE_DIR = "./"  # ./

# 基础目录
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')  # ./static
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')  # ./uploads
DEFAULT_FOLDER = os.path.join(BASE_DIR, 'default')  # ./default
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')  # ./downloads

# 下载和上传文件的路径
OUT_BASE_DIR = os.path.join(DOWNLOAD_FOLDER, 'out')  # ./downloads/out
TEXT_BASE_DIR = os.path.join(UPLOAD_FOLDER, 'sources')  # ./uploads/sources
USERS_STOPWORDS_DEFAULT_DIR = os.path.join(UPLOAD_FOLDER, 'custom_stopwords')  # ./uploads/custom_stopwords

# official的选项的路径
FONT_DEFAULT_DIR = os.path.join(DEFAULT_FOLDER, 'fonts')  # ./default/fonts
STOPWORDS_DEFAULT_DIR = os.path.join(DEFAULT_FOLDER, 'stopwords')  # ./default/stopwords

# 把这些组成一个list
PATH_LIST = [
    UPLOAD_FOLDER, STATIC_FOLDER, DEFAULT_FOLDER, DOWNLOAD_FOLDER,
    OUT_BASE_DIR, TEXT_BASE_DIR, USERS_STOPWORDS_DEFAULT_DIR,
    FONT_DEFAULT_DIR, STOPWORDS_DEFAULT_DIR,
]

# 看看是不是少了哪个目录，如果少了就创建一下
[os.makedirs(path, exist_ok=True) for path in PATH_LIST]

# app的路径配置
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEXT_BASE_DIR'] = TEXT_BASE_DIR
app.config['STATIC_FOLDER'] = STATIC_FOLDER

app.config['USERS_STOPWORDS_DIR'] = USERS_STOPWORDS_DEFAULT_DIR
app.config['DOWNLOAD_BASE_DIR'] = OUT_BASE_DIR

ALLOWED_EXTENSIONS = {'txt', 'md'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    global stopwords_path
    if request.method == 'POST':
        # 看是否上传了文件
        if 'text-file' not in request.files:
            return render_template('index.html', error='没有上传原始文件')
        text_file = request.files['text-file']
        if text_file.filename == '':
            return render_template('index.html', error='没有选择文件')

        if text_file and allowed_file(text_file.filename):
            # 保存上传的文本文件
            text_file_save = os.path.join(app.config['TEXT_BASE_DIR'], text_file.filename)
            text_file.save(text_file_save)

            # 来check一下停词文件
            stopwords = request.form['stop-words']
            if stopwords == "custom":
                if 'custom-stop-words' not in request.files:
                    return render_template('index.html', error='没有上传停词文件')
                custom_stopwords_file = request.files['custom-stop-words']
                if text_file.filename == '':
                    return render_template('index.html', error='没有选择文件')

                if custom_stopwords_file and allowed_file(custom_stopwords_file.filename):
                    # 保存用户上传的自定义的停词文件
                    custom_stopwords_file_save = os.path.join(
                        app.config['USERS_STOPWORDS_DIR'], custom_stopwords_file.filename
                    )
                    custom_stopwords_file.save(custom_stopwords_file_save)
                    stopwords_path = custom_stopwords_file_save
            elif stopwords != "custom":
                stopwords_name = stopwords + '.txt'
                stopwords_path = os.path.join(STOPWORDS_DEFAULT_DIR, stopwords_name)

            # 获取其他参数
            _font = request.form['font']
            font = fonts_dict[_font]
            shape = request.form['shape']

            try:
                name = generate(
                    in_path=text_file_save,
                    stopwords_path=stopwords_path,
                    fonts_path=(fonts_path := os.path.join(FONT_DEFAULT_DIR, font)),
                    out_root=OUT_BASE_DIR,
                )
                # time.sleep(2)
                wordcloud_url = os.path.join(app.config['DOWNLOAD_BASE_DIR'], f'{name}.png')
                return render_template('index.html', wordcloud=wordcloud_url)
                # return render_template('index.html', wordcloud=wordcloud_url, error=stopwords_path)
            except Exception as e:
                return render_template('index.html', error=f'生成词云时出错: {str(e)}')

    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

# 给生成的词云提供可访问的URL
@app.route('/downloads/out/<path:filename>')
def download(filename):
    return send_from_directory(app.config['DOWNLOAD_BASE_DIR'], filename)


if __name__ == '__main__':
    app.run(debug=True)
