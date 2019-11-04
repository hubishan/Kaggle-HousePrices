#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Title     : TODO
# @Objective : TODO
# @Time      : 2019/10/28 20:51
# @Author    : hubishan
# @Site      :
# @File      : HousePrices kernel.py
# @Software  : IntelliJ IDEA

import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
# %matplotlib inline
plt.style.use('ggplot')

train = pd.read_csv('..\\data\\train.csv')
test = pd.read_csv('..\\data\\test.csv')

train = pd.read_csv('D:\IdeaProjects\Kaggle-HousePrices\data\train.csv\data\\train.csv')
test = pd.read_csv('..\\data\\test.csv')

plt.figure(num=1,figsize=(15,8))
# sns.boxplot(train.YearBuilt, train.SalePrice[2000])

sns.boxplot(train.YearBuilt[train['YearBuilt'] == 2000], train[train['YearBuilt'] == 2000].SalePrice)

# 返回YearBuilt在[1995,2000]中的索引
index1=train[train['YearBuilt'].isin([1995,2000])].index
index2=train.ix[train['YearBuilt'].isin([1995,2000]),'YearBuilt']

sns.boxplot(train.YearBuilt[train[train['YearBuilt'].isin([1995,2000])].index], train.SalePrice[train[train['YearBuilt'].isin([1995,2000])].index])
train.ix[train['YearBuilt'].isin([1995,2000]),'YearBuilt']
# sns.boxplot(train.YearBuilt[train['YearBuilt'].isin(1995:2000)], train[train['YearBuilt'].isin([1995:2000])].SalePrice)

sns.set_style("ticks")
plt.show()


# plt.figure(num=2,figsize=(155,38))
# sns.boxplot(train.YearBuilt, train.SalePrice)
# plt.show(2)


