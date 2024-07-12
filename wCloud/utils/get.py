#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : get.py

import os

def get_path(path):
    return os.path.dirname(path)

def get_name(path):
    base_name = os.path.basename(path)
    file_name, file_extension = os.path.splitext(base_name)
    return file_name

def get_extension(path):
    base_name = os.path.basename(path)
    file_name, file_extension = os.path.splitext(base_name)
    return file_extension

def get_name_and_extension(path):
    base_name = os.path.basename(path)
    file_name, file_extension = os.path.splitext(base_name)
    return file_name, file_extension


if __name__ == '__main__':
    # 用法示例
    BASE_PATH = os.path.dirname(__file__)
    print("base_path:\t", get_path(BASE_PATH))
    print("name:\t\t", get_name(BASE_PATH))
