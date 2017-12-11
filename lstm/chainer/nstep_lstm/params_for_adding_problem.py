#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# LSTM層の数
N_LAYERS = 1

DROPOUT = 0.3

# fibonacci数列を割る値
VALUE = 5

# 常に同じ計算をする。
np.random.seed(0)

# 時系列データの全長
TOTAL_SIZE = 10000

# 訓練とテストの分割比
SPRIT_RATE = 0.9

# 入力時の時系列データ長
SEQUENCE_SIZE = 200

EPOCHS = 30
BATCH_SIZE = 100

# 入力層の次元
N_IN = 2

# 隠れ層の次元
N_HIDDEN = 200

# 出力層の次元
N_OUT = 1