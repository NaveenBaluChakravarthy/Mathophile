import os
import time
import subprocess
root_path = os.getcwd()

C_Repos = os.listdir(root_path)
C_Repos.pop(C_Repos.index('ZzCommit.py'))
C_Repos.pop(C_Repos.index('ZzPull.py'))

print("Repos and their IDs\n\n")
for inx, repo in enumerate(C_Repos):
    print(f"\t{inx+1:02d}. {repo}")
    
repolist = input('\n\nEnter the ID of repo separated by + sign : ')
repolist = repolist.split('+')

for repoid in repolist:
    proceed = False
    print('*' * 100)
    try:
        idx = int(repoid) - 1
        if 0 <= idx < len(C_Repos):
            proceed = True
        else:
            print("Repo ID out of bound")        
    except:
        print("Invalid Repo ID")
        break
    
    if proceed:
        repo_path = os.path.join(root_path, C_Repos[idx])
        os.chdir(repo_path)
        p = subprocess.run(['git', 'pull'], capture_output = True, text = True, shell = True) 
        print(f"Repo Name : {C_Repos[idx]}")
        print(p.stdout)
        
        
        
time.sleep(15)