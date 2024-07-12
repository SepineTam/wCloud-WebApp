#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : gen.py

from wordcloud import WordCloud
from matplotlib import pyplot as plt
import matplotlib

from wCloud.utils import *

matplotlib.use('Agg')  # 使用Agg后端，它不需要GUI支持


def fig_path(name, file_type="png"):
    return os.path.join(BASE_PATH, f"test/out/figures/{name}.{file_type}")

def gen_fig(name, text, stopwords, font_path):
    # 创建词云
    wordcloud = WordCloud(
        font_path=font_path,
        width=800, height=500,
        background_color="white"
    ).generate(cut_text(text, stopwords))

    """
    生成图片
    plt.figaspect(0.5) -> 设置图形的宽高比为0.5，图形的高度是宽度的两倍。
    facecolor='white' -> 设置图形的背景颜色为白色。
    """
    plt.figure(figsize=plt.figaspect(0.5), facecolor='white')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # 关闭图形的坐标轴，使得图形更干净，只显示关键的视觉内容，没有坐标轴的干扰。
    # plt.savefig(out_path)
    return plt


if __name__ == "__main__":
    text = "Here is a looooooooooog word or sentence"
    stopwords = load_stopwords("../default/stopwords/default_stopwords.txt")
    font_path = "../default/fonts/SimHei.ttf"
    figure = gen_fig(
        text=text,
        stopwords=stopwords,
        font_path=font_path,
        name="no_name"
    )
