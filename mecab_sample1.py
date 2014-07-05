#coding:utf-8
import sys
import MeCab
result = MeCab.parse("PythonからMeCabの形態素解析を使ってみました。")
print result
