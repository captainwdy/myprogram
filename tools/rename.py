#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#File:rename.py
#Author: wangdayao(captainwdy@163.com)
#Date: 2016/02/15 09:54:56
#Descrip: rename old file to new file

import os

def new_file_name(file):
    """return new file name"""
    return file[5:]


for file in  os.listdir("."):
    if os.path.isfile(file):
        new_file = new_file_name(file)
        print file, "to", new_file
        #os.rename(file, new_file)
