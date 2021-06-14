import os
import time
import subprocess
root_path = os.getcwd()

C_Repos = os.listdir(root_path)
C_Repos.pop(C_Repos.index('ZzCommit.py'))
C_Repos.pop(C_Repos.index('ZzPull.py'))

statuslist = []
statuslist.append('\n\n' + '-' * 60)
statuslist.append('Repository' + ' ' * 31 + 'Status\n' + '-' *60)

for repo in C_Repos:
    repo_path = os.path.join(root_path, repo)
    os.chdir(repo_path)  
    p = subprocess.run(['git', 'status'], capture_output = True, text = True, shell = True)
    if 'working tree clean' in p.stdout:
        statuslist.append(f'{repo:40s} Working Tree Clean')
    else:
        commitmsg = input(f'Enter your commit message for {repo}: ')
        
        q = subprocess.run(['git',  'add',  '.'], capture_output = True, text = True, shell = True)
        r = subprocess.run(['git', 'commit',  '-m',  commitmsg], capture_output = True, text = True, shell = True)
        s = subprocess.run(['git', 'push'],  capture_output = True, text = True, shell = True)
        statuslist.append(f'{repo:40s} Commit Performed')

statuslist.append('-' * 60)

for item in statuslist:
    print(item)
    time.sleep(0.2)
    
print("\n\n\nAppropriate actions have been made on all repos.\n\nQuitting in 15 seconds..")
time.sleep(15)