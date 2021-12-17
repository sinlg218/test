# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:07:43 2021

@author: xin
"""
import requests
import base64
import pandas as pd
import numpy as np
import os
import datetime
import time
import docx
import win32com
import json
import sqlalchemy
import pymysql
import neo4j
import chardet
import pdfplumber
import re
import pytesseract
import PIL
import beautifulsoup4	#bs4，导入命令可能有误；2021.12.13测试

#修改，看是否能出现暂存区 2021.12.17 测试

#直接用add 再次追踪，以添加到缓存区
