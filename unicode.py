#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(ord('中'),ord('文'))
s = '中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))