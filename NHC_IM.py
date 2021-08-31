# -*- coding:utf-8 -*-
import os
import time

class NHC_IM:
    def __init__(self,projectDir) : 
        self.projectDir = self.raw_string(projectDir)   
        self.file_name = ['prometheus']
        self.file_n = ['Dockerfile']

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
    
    # Insufficient Monitoring
    def findPrometheus(self):
        stat_IM = 0
        for parent,dirNames,fileNames in os.walk(self.projectDir):
            for filename in fileNames:
                fn = filename.split('.')[0]
                if fn in self.file_name:
                    stat_IM = 1#表示存在监控
        return stat_IM

    def getDockerfile(self):
        fileLists = []
        for parent,dirNames,fileNames in os.walk(self.projectDir):
            for filename in fileNames:
                ext = filename.split('.')[0]
                if ext in self.file_n:
                    fileLists.append(os.path.join(parent,filename))
        return fileLists
    
    @staticmethod
    def countLine(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            if file_line != '' and file_line != '\n':
                if 'HEALTHCHECK' in str(file_line):
                    count += 1              
        return count
    
    # No HealthCheck
    def findNHC(self):
        fileLists= self.getDockerfile()
        stat_NHC = 0
        if fileLists:
            for typeList in fileLists:
                if self.countLine(typeList):
                    stat_NHC = 1
        return stat_NHC     #1就有健康检测
        
# projectDir = 'D:\杂物\lib\ftgo-application'
# print(NHC_IM(projectDir).findPrometheus())
# print(NHC_IM(projectDir).findNHC())

    