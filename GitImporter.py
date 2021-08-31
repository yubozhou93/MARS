import sys
from analyse import Analyse
import os
from git import Repo
from git.repo.fun import is_git_dir
from url import GetUrl
from STAT import Stat
import shutil
import json

class GitRepository(object):
	def __init__(self,repo_url,branch = 'master'):
		self.local_path = r'/root/repos'
		self.repo_url = repo_url
		self.repo = None
		self.initial(repo_url,branch)

	def initial(self,repo_url,branch):
		if not os.path.exists(self.local_path):
			os.makedirs(self.local_path)
		git_local_path = os.path.join(self.local_path,".git")
		if not is_git_dir(git_local_path):
			self.repo = Repo.clone_from(repo_url,to_path = self.local_path,branch = branch)
		else:
		    self.repo = Repo(self.local_path)
		
	def RemoveDir(self):
		if not os.path.exists(self.local_path):
			os.mkdir(self.local_path)
		else:
			shutil.rmtree(self.local_path)
			os.mkdir(self.local_path)


if __name__ == '__main__':
	repo_url = sys.argv[1]
	repo = GitRepository(repo_url)
	local_path = r'/root/repos'
	#repo.RemoveDir()
	result = {}
	repoName = repo_url.split('/')[-1]
	result["name"] =  repo_url.split('/')[-1]
	#result['Number of microservices'] = 
	if len(Stat(local_path).mega()) != 0:
		result["MS"] = Stat(local_path).mega()
	else :
		result["MS"] = "does not exist "
	
	if len(Stat(local_path).nano()) != 0 :
		result["NS"] = Stat(local_path).nano()
	else :
		result["NS"] = "does not exist"
	
	urls = GetUrl(repo_url).getPage(repo_url)
	result["HE"] = urls
	
	if Stat(local_path).MC():
		result["MC"] = "exist Manual Configuration"
	else:
		result["MC"] = "does not exist Manual Configuration"
	
	if Stat(local_path).NAG():
		result["NAG"] = "exist API Gateway"
	else:
		result["NAG"] = "No API Gateway"
	
	if Stat(local_path).TO():
		result["TO"] = "exist breaker"
	else:
		result["TO"] = "no breaker"
	
	if Stat(local_path).MSIH():
		result["MSIH"] = "no Multiple Service Instances per Host"
	else:
		result["MSIH"] = "exist Multiple Service Instances per Host"
	
	if Stat(local_path).NHC():
		result["NHC"] = "exist HealthCheck"
	else:
		result["NHC"] = "no HealthCheck"
	
	if Stat(local_path).LL():
		result["LL"] = "have Local Logging"
	else:
		result["LL"] = "no Local Logging"
	
	if Stat(local_path).IM():
		result["IM"] = "exist Monitoring"
	else:
		result["IM"] = "Insufficient Monitoring"
	
	if Stat(local_path).Kafka():
		result["Give It a Rest Pitfall"] = "Multiple protocol can exist"
	else:
		result["Give It a Rest Pitfall"] = "Give It a Rest Pitfall"
	
	if len(urls) == (len(Analyse(local_path).getDockerPath())-1):
		result["ESB"] = "ESB exist"
	else:
		result["ESB"] = "no ESB"
	
	result=json.dumps(result)
	print(result)
