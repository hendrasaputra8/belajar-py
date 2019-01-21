import subprocess

rc = subprocess.call(['which', 'htop'])
if rc == 0:
    print 'htop installed!'
else:
    print 'htop missing in path!'
    subprocess.call('/root/scripts/install.sh')  # --> path bash bisa taro dimana pun
