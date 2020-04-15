# Install
Requiers Python3 and pip
clone repo
```sh
git clone https://github.com/inab/documentation-hub-dependencies.git
```
#### Important
You need a github access [token]
create a file ```config.py``` in the folder and add your token
The file should look like this:
```py
#!/usr/bin/env python
token = "Paste github token here"
```
```sh
$ pip install -r requirements.txt
$ python main.py -h #help 
```
[token]:<https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>
