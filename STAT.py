from TO_NAG import TO_NAG
from NHC_IM import NHC_IM
from MSIH_kafka import MSIH
from LL_Lines import local_log
from analyse import Analyse

class Stat:
    def __init__(self,projectDir) : 
        self.projectDir = self.raw_string(projectDir)

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
    
    def mega(self):
        LineMax = 1400 
        targetMcs = []
        totalLines = Analyse(self.projectDir).TotalLines()
        for key in totalLines:
            if totalLines[key] > LineMax:
                targetMcs.append(key)
        return targetMcs

    def nano(self):
        LineMin = 100 
        targetMcs = []
        totalLines = Analyse(self.projectDir).TotalLines()
        for key in totalLines:
            if totalLines[key] < LineMin:
                targetMcs.append(key)
        return targetMcs

    def MC(self):
        Pom = Analyse(self.projectDir).getPomPath()
        Mcs = Analyse(self.projectDir).getDockerPath()
        stat_MC = 0
        if  len(Pom) == 0:
            return stat_MC
        elif len(Mcs):
            if len(Pom) == len(Mcs):
                stat_MC = 1
        return stat_MC

    def LL(self):
        mcsPath = Analyse(self.projectDir).getDockerPath()
        for mcs in mcsPath:
            stat_LL = local_log(mcs).Local_logging()
        return stat_LL
        
    def MSIH(self):
        stat_MSIH = MSIH(self.projectDir).findMSIH()
        return stat_MSIH

    def Kafka(self):
        stat_Kafka = MSIH(self.projectDir).findKafka()
        return stat_Kafka

    def NHC(self):
        stat_NHC = NHC_IM(self.projectDir).findPrometheus()
        return stat_NHC

    def IM(self):
        stat_IM = NHC_IM(self.projectDir).findNHC()
        return stat_IM

    def TO(self):
        stat_TO = TO_NAG(self.projectDir).findHystrix()
        return stat_TO

    def NAG(self):
        stat_NAG = TO_NAG(self.projectDir).findZuul()
        return stat_NAG

# projectDir = 'D:\杂物\lib\ftgo-application'
# print(Stat(projectDir).mega())
# print(Stat(projectDir).nano())
# print(Stat(projectDir).MC())