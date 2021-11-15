import os
import time
import subprocess
root_path = 'D:\Code'

f = open('D:\gitlog.txt', 'w+')
repo = input('Enter the repo name : ')

repo_path = os.path.join(root_path, repo)
os.chdir(repo_path)
p = subprocess.run(['git', 'log'], capture_output = True, text = True, shell = True) 
f.write(p.stdout)
f.write('*' * 100)
        
print('Quitting in 5 seconds')     
time.sleep(5)