# -*- coding:utf-8 -*-
import os
# 获取当前项目目录

class local_log:
    def __init__(self,projectDir) : 
        self.projectDir = self.raw_string(projectDir)
        # 文件类型
        self.typeList = ['java']

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
    def findLog(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            if file_line != '' and file_line != '\n':
                if 'log4j' in str(file_line):
                    count = 1   #如果输出了就说明有
        return count
    
    #统计一个文件中代码的行数
    @staticmethod
    def countLine(fileName):
        count = 0
        for file_line in open(fileName,'rb').readlines():
            if file_line != '' and file_line != '\n':
                count += 1
        #print (fileName + '----' , count)
        return count
    
    def Local_logging(self):
        fileLists= self.getFile()
        stat_LL = 0
        for typeList in fileLists:   
            if self.findLog(typeList):
                stat_LL = 1
                return stat_LL
        return stat_LL

    def count_Total_Lines(self):
        fileLists = self.getFile()
        totalLines = 0
        for typeList in fileLists:
            totalLines = totalLines + self.countLine(typeList)
        return totalLines


# projectDir = 'D:\杂物\lib\dubbo\dubbo-common'
# print(local_log(projectDir).Local_logging())
# print(local_log(projectDir).count_Total_Lines())