from subprocess import call

call('cd some-stuff', shell=True)
call('git pull', shell=True)
call('git add --all', shell=True)
call('git commit --all -m "Das testen"', shell=True)
call('git push origin master', shell=True)
