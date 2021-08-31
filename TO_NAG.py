# -*- coding:utf-8 -*-
import os

class TO_NAG:
    def __init__(self,projectDir) : 
        self.projectDir = self.raw_string(projectDir)   
        self.typeList = ['xml']
    
    @staticmethod
    def raw_string(projectDir):
        escape_dict = {    '\a': r'\a',
                    '\b': r'\b',
                    '\c': r'\c',
                    '\f': r'\f',
                    '\n': r'\n',
                    '\r': r'\r',
                    '\t': r'\t',
                    '\v': r'\v',
                    '\'': r'\'',
                    '\"': r'\"',
                    '\0': r'\0',
                    '\1': r'\1',
                    '\2': r'\2',
                    '\3': r'\3',
                    '\4': r'\4',
                    '\5': r'\5',
                    '\6': r'\6',
                    '\7': r'\7',
                    '\8': r'\8',
                    '\9': r'\9'}
        rstring = ""
        for char in projectDir:        
            try:
                if char in escape_dict:
                    rstring += escape_dict[char]
                else:
                    rstring += char
            except:
                KeyError:print("error")
        return rstring

# 遍历项目中的文件夹
    def getFile(self):
        fileLists = []
        for parent,dirNames,fileNames in os.walk(self.projectDir):
            for filename in fileNames:
                ext = filename.split('.')[-1]
                if ext in self.typeList:
                    fileLists.append(os.path.join(parent,filename))
        return fileLists
    
    @staticmethod
    def jugeZuul(fileName):
        count = 0
        for file_line in open(fileName).readlines():
            if file_line != '' and file_line != '\n':
                if '<artifactId>spring-cloud-starter-netflix-zuul</artifactId>' in str(file_line) or '<artifactId>spring-cloud-starter-zuul</artifactId>'in str(file_line):                
                    count += 1
        return count
    
    @staticmethod
    def jugeHystrix(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            # 不统计空白行
            if file_line != '' and file_line != '\n':
                #print(file_line)
                if '<artifactId>hystrix-core</artifactId>'in str(file_line) or '<artifactId>spring-cloud-starter-netflix-hystrix</artifactId>'in str(file_line):                
                    count += 1
        return count

    # No API Gateway
    def findZuul(self):
        fileLists = self.getFile()
        stat_zuul = 0
        if fileLists:
            for typeList in fileLists:
                if self.jugeZuul(typeList):
                    stat_zuul = 1
        return stat_zuul

    #Timeouts
    def findHystrix(self):
        fileLists = self.getFile()
        stat_Hystrix = 0
        if fileLists:
            for typeList in fileLists:
                if self.jugeHystrix(typeList):
                    stat_Hystrix = 1
        return stat_Hystrix
    
# projectDir = 'D:\杂物\lib\ftgo-application'
# print(TO_NAG(projectDir).findZuul())
# print(TO_NAG(projectDir).findHystrix())