# -*- coding: utf-8 -*-
##<span style="font-size:18px;">#coding=utf-8  
#Author: http://blog.csdn.net/boksic  
import sys
import importlib
importlib.reload(sys)
import jieba
import jieba.analyse
import collections  
#reload(sys)   
#sys.setdefaultencoding('utf8')  
#txt = open('jieba_input.txt','r').read()  

txt = open('jieba_input.txt','r').read() 	#以读的方法打开输入文件
#stopkey=[line.strip().decode('utf-8') for line in open('cn_jieba_sw.txt').readlines()]  
wfile=open('jieba_result.txt','w')  #以写的方法打开输出文件
  
t50 = jieba.analyse.extract_tags(txt,  topK=50,  withWeight=False,  allowPOS=())  #读取输入文件，提取使用频率前50的词

print (t50)  #打印词频前50的词

#for item in t50:
#    print (item[0],item[1])

print ('start to count freq now')

word_list = jieba.lcut(txt)  #把输入文件分词
stopwords = ['，', '。','、',' ','（','）','：'] #定义停用词表

word_list = [s for s in word_list if s not in stopwords] #把停用词表里的词去除

wfd1={}

for word1 in t50:    #词频前50的词，提取使用次数，并写入输出词典
    freq1 = word_list.count(word1)
    wfd1[word1] = freq1
 
#sort_wfd1=sorted(wfd1.items(),key=operator.itemgetter(1))
sort_wfd1 = collections.OrderedDict(sorted(wfd1.items(), key = lambda t: -t[1])) #讲输出词典的内容排序，按使用次数降序排列

for key,value in sort_wfd1.items():  
    print (key + ":%d" % value)   #打印输出词典的内容
    wfile.write(key + ":%d" % value) #把输出词典的内容写出文档
    wfile.write('\n') #每写一次换行
    
wfile.close()  #关闭输出文档
#print (sort_wfd2)
#print (sort_wfd1)
