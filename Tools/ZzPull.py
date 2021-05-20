import os
import time
import subprocess
root_path = os.getcwd()

C_Repos = ['Daily-Practice']

for repo in C_Repos:
    repo_path = os.path.join(root_path, repo)
    os.chdir(repo_path)  
    p = subprocess.run(['git', 'pull'], capture_output = True, text = True, shell = True)
    print(p.stdout)
   
time.sleep(15)