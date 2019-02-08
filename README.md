
"# py3con" 
try shell

git config --global credential.helper cache

from subprocess import call
call('git add -u', shell = True)
call('git commit -a "..."', shell = True)
call('git pushwq
', shell = True)


# In PowerShell
py -3 -m venv env
env\scripts\activate
pip install -r requirements.txt
Set-Item Env:FLASK_APP ".\application.py"
flask run

# In Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FLASK_APP=application.py flask run
