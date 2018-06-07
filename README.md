
"# py3con" 
try shell

git config --global credential.helper cache

from subprocess import call
call('git add -u', shell = True)
call('git commit -a "..."', shell = True)
call('git pushwq
', shell = True)
