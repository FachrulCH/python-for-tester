# What is Pipenv

## Pipfile

# How to use pipenv


## Initiate
```console
python-for-tester on  master [⇡?] 
➜ pipenv --three                        
Creating a virtualenv for this project…
Pipfile: /Users/fachrulch/koding/FachrulCH/python-for-tester/Pipfile
Using /usr/local/bin/python3 (3.7.6) to create virtualenv…
⠧ Creating virtual environment...created virtual environment CPython3.7.6.final.0-64 in 411ms
  creator CPython3Posix(dest=/Users/fachrulch/.local/share/virtualenvs/python-for-tester-hblkEfR2, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/Users/fachrulch/Library/Application Support/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /Users/fachrulch/.local/share/virtualenvs/python-for-tester-hblkEfR2
Creating a Pipfile for this project…
```

## Install depedencies

```console
python-for-tester on  master [⇡?] took 2s 
➜ pipenv install pytest  
Installing pytest…
Adding pytest to Pipfile's [packages]…
✔ Installation Succeeded 
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success! 
Updated Pipfile.lock (1c4d3d)!
Installing dependencies from Pipfile.lock (1c4d3d)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 11/11 — 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```