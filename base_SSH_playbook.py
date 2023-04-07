#!/usr/bin/python3
# -*- coding: utf-8  -*-

# pip install paramiko

import paramiko


from mySecret import annuaire



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



    if type( payload ) == "<class 'str'>":
        payload( client )
    else:
        for pay in payload:
             pay( client)

    if client :
        client.close()


#for host in [ 'phil', 'toto']:
#    vector( host, ls )

vector( 'toto', [ ls, pwd]  )
