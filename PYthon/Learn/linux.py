import subprocess

subprocess.run('echo "Running linux commands usng python subprocess"', shell=True)

result=subprocess.run('ls -l linux.py', shell=True, stdout=subprocess.PIPE)
print(result.stdout)