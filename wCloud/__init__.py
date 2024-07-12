#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : __init__.py

import os

from wCloud.gen import gen_fig
from wCloud.utils.load import *
from wCloud.utils.get import *


def generate(in_path, stopwords_path, fonts_path, out_root):
    text = load_file(in_path)
    stopwords = load_stopwords(stopwords_path)

    name = get_name(in_path)
    out_name = name + ".png"
    out_path = os.path.join(out_root, out_name)

    plt = gen_fig(name, text, stopwords, fonts_path)
    plt.savefig(out_path)

    return name


if __name__ == '__main__':
    BASE_PATH = os.path.dirname(__file__)
