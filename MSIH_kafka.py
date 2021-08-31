# -*- coding:utf-8 -*-
import os

class MSIH:
    def __init__(self,projectDir) : 
        self.projectDir = self.raw_string(projectDir)
        self.typeList = ['yml']
        self.file_name = ['docker-compose']
    
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

    def getFile(self):
        fileLists = []
        stat_MSIH = 0
        for parent,dirNames,fileNames in os.walk(self.projectDir):
            for filename in fileNames:
                ext = filename.split('.')[-1]
                fn = filename.split('.')[0]
                if fn in self.file_name:
                    stat_MSIH = 1
                    return stat_MSIH
                if ext in self.typeList:
                    fileLists.append(os.path.join(parent,filename))
        return fileLists
 
    def getKafka(self):
        fileLists = []
        for parent,dirNames,fileNames in os.walk(self.projectDir):
            for filename in fileNames:
                ext = filename.split('.')[-1]
                if ext in self.typeList:
                    fileLists.append(os.path.join(parent,filename))
        return fileLists

    @staticmethod
    def jugeDockerCompos(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            if file_line != '' and file_line != '\n':
                if 'docker-compos'in str(file_line):                
                    count += 1
        return count

    @staticmethod
    def jugeKafka(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            if file_line != '' and file_line != '\n':
                if 'kafka'in str(file_line):                
                    count += 1
        return count
 
    def findMSIH(self):
        fileLists = self.getFile()
        if isinstance (fileLists,int):
            return fileLists
        else:
            for typeList in fileLists:
                stat_MSIH = 0
                stat_MSIH = self.jugeDockerCompos(typeList)
                if stat_MSIH:
                    return stat_MSIH 
    
    def findKafka(self):
        stat_Kafka = 0
        fileLists = self.getKafka()
        for typeList in fileLists:
           if self.jugeKafka(typeList):
               stat_Kafka = 1
        return stat_Kafka        
        

# projectDir = 'D:\杂物\lib\ftgo-application'
# print(MSIH(projectDir).findMSIH())
# print(MSIH(projectDir).findKafka())
