from LL_Lines import local_log
import os 

class Analyse :
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

    def getPomPath(self):
        pomPath = []    #存放pom文件的路径  用来判断是否自动配置
        for path,dir_list,file_list in os.walk(self.projectDir):  
            for file_name in file_list:  
                if file_name == 'pom.xml':
                    pomPath.append(os.path.join(path))
        pomPath = list(set(pomPath))
        return pomPath
    
    def getGradlePath(self):
        gradlePath = []    #存放gradle文件的路径    用来判断是否自动配置
        for path,dir_list,file_list in os.walk(self.projectDir):  
            for file_name in file_list:  
                if file_name == 'build.gradle':
                    gradlePath.append(os.path.join(path))
        gradlePath = list(set(gradlePath))
        return gradlePath
    
    def getDockerPath(self):
        dockerPath = []    #存放有docker文件的路径     区分微服务
        for path,dir_list,file_list in os.walk(self.projectDir):  
            for file_name in file_list:  
                if os.path.splitext(file_name)[0] == 'Dockerfile' :         
                    dockerPath.append(os.path.join(path)) #,file_name))
        dockerPath = list(set(dockerPath))
        return dockerPath

    # 获取微服务名
    @staticmethod
    def McsName(str):
        mcsName = str.split('\\')[-1]
        return mcsName

    def TotalLines (self):
        lines = {}          #比较阈值  给出最小 最大服务
        mcsPath = self.getDockerPath()
        for mcs in mcsPath:
            name = self.McsName(mcs)
            line =  local_log(mcs).count_Total_Lines()
            if line:
                lines[name] = line 
        return lines

# projectDir = 'D:\杂物\lib\ftgo-application'
# print(Analyse(projectDir).TotalLines())
