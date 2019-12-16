#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @Title     : TODO
# @Objective : TODO
# @Time      : 2019/10/31 15:25
# @Author    : hubishan
# @Site      :
# @File      : test_tf_hub.py
# @Software  : IntelliJ IDEA

import os
import sys
import tensorflow_hub as hub

# bert_module = hub.Module("https://tfhub.dev/google/bert_chinese_L-12_H-768_A-12/1", trainable=True)

bert_module = hub.Module("D:\\data\\2")



# bert_inputs = dict(input_ids=input_ids,input_mask=input_mask,segment_ids=segment_ids)
# bert_outputs = bert_module(bert_inputs, signature="tokens", as_dict=True)
# pooled_output = bert_outputs["pooled_output"]
# sequence_output = bert_outputs["sequence_output"]