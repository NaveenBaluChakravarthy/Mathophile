import os
import time
import subprocess
root_path = os.getcwd()

C_Repos = os.listdir(root_path)
C_Repos.pop(C_Repos.index('ZzCommit.py'))
C_Repos.pop(C_Repos.index('ZzPull.py'))

for repo in C_Repos:
    repo_path = os.path.join(root_path, repo)
    os.chdir(repo_path)
    p = subprocess.run(['git', 'pull'], capture_output = True, text = True, shell = True) 
    print(f"Repo Name : {repo}")
    print(p.stdout)
    print('*' * 100)
        
print('Quitting in 15 seconds')     
time.sleep(15)