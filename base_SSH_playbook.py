#!/usr/bin/python3
# -*- coding: utf-8  -*-

# pip install paramiko

import paramiko
import datetime

from mySecret import annuaire

var = 5

cmd = """
#!/bin/bash
$echo password | sudo -S su -
whoami
cd /etc/
tree
"""


def tree( client ):
    _stdin, _stdout, _stderr = client.exec_command("echo '"+cmd+"' > myTree.sh")
    _stdin.close()
    _stdin, _stdout, _stderr = client.exec_command("./myTree.sh")
    print( 'out',_stdout.read().decode())
    print( 'err', _stderr.read().decode())
    _stdin.close()
    



def ping( client ):
    _stdin, stdout, _stderr = client.exec_command("ping -c 5 www.google.com ")
    #print( 'out',_stdout.read().decode())
    #print( 'err', _stderr.read().decode())
    

    x = datetime.datetime.now()

    string = x.strftime("%Y-%m-%d-%H:%M:%S")

    file = open( 'install'+ string +'.log', 'w')
    while True :
        output = stdout.readline()

        if len( output ) == 0 :
            break;
        file.writelines(  output.strip() + "\n" ) 
        ##print(output.strip())
        # Do something else
    _stdin.close()
    file.close()


def ls( client ):
    _stdin, _stdout, _stderr = client.exec_command("pwd")
    print( 'out',_stdout.read().decode())
    print( 'err', _stderr.read().decode())
    _stdin.close()

    _stdin, _stdout, _stderr = client.exec_command("df -h")
    print( 'out',_stdout.read().decode())
    print( 'err', _stderr.read().decode())
    _stdin, _stdout, _stderr = client.exec_command("df -h", _stdin=_stdout)
    print( 'out',_stdout.read().decode())
    print( 'err', _stderr.read().decode())
    _stdin.close()


def pwd( client ):
    _stdin, _stdout, _stderr = client.exec_command("pwd")
    print( 'out',_stdout.read().decode())
    print( 'err', _stderr.read().decode())
    _stdin.close()



print( type( ' '))

def versionPython( client ):
    _stdin, _stdout,  _stderr = client.exec_command("python --version")
    print( 'out >' ,_stdout.read().decode())
    print( 'err >' , _stderr.read().decode())
    _stdin.close()



def getSSH ( nom ):
    host        = annuaire.playbook[ nom ]['ip']
    username    = annuaire.playbook[ nom ]['login']
    password    = annuaire.playbook[ nom ]['pw']

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)

    return client 




def vector ( nom, payload ):
    client = getSSH ( nom )

    payload( client )

    if client :
        client.close()


#for host in [ 'phil', 'toto']:
#    vector( host, ls )

vector( 'phil', tree  )
