
# coding: utf-8

# In[32]:

import cv2
import os
import codecs
from PIL import Image, ImageFont, ImageDraw, ImageColor


# In[90]:



## ATTENTION!!! PARAMETERS NEEDED!!!
# 所有文件均使用相对位置，所以ipynb文件需要与以下所有文件在同一目录
# filename 为所读取字幕文件的文件名
# fontname 为所使用的字体文件的文件名
# fontsize为字体大小
# bgcolor 为生成的图片的背景颜色，可以为Hexadecimal(String),RGB,HSL以及常用HTML颜色名 
# subcoord 为字幕左上角坐标
filename = "newchntest.txt"
fontname = "MFShangYa_Noncommercial-Regular.otf"
fontsize = 50
bgcolor = "green"
subcoord1 = (90,850)
subcoord2 = (90,920)

def to_unicode(listName):
    for x in range(len(listName)):
        listName[x] = listName[x].decode('gbk')
    return listName

## 打开文件并读取字幕数据
subText = open(filename,'r')
subList = subText.readlines()
subList = to_unicode(subList)
textLen = len(subList)
print "File Successfully Read, {} Lines Found.".format(textLen)

## 读取并设置字幕字体
font = ImageFont.truetype(fontname, fontsize, 0, "gbk")

for i in range(len(subList)/2):
    ## 创建新图片
    subString1 = subList[2*i]
    subString2 = subList[2*i-1]
    im = Image.new("RGB", (1920,1080), bgcolor)
    ## 创建绘图句柄
    draw = ImageDraw.Draw(im)
    draw.text(subcoord1, subString1, font=font)
    draw.text(subcoord2, subString2, font=font)
    im.save("{}.jpg".format(i+1),"JPEG")


# In[ ]:




# In[ ]:



