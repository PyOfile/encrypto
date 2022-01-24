# encrypto
This is a simple python program to create passwords.

### To use, first make sure you have python installed.
```
sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip -y && sudo apt install python3-venv -y
```
#
### Make Environment
```
python3 -m venv env
```
#
### environment activation env
```
source env/bin/activate
```
#
### Create password with limited punctuation at only 16 characters
#
```
python3 pass_gen.py
```
#
### Create password with full punctuation at only 32 characters
#
```
python3 pass_gen_sec.py
```
#
### environment deactivation
```
deactivate
```
#
