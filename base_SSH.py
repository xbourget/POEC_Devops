#!/usr/bin/python3
# -*- coding: utf-8  -*-

# pip install paramiko

import paramiko
from  secret import data 

host = "192.168.1.149"
host = "192.168.155.31"
username = "work"
#username = "mitia"
password = data.passwordWork
#password = data.passwordMitia

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

#client.connect(host, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)


_stdin, _stdout, _stderr = client.exec_command("ls .")
print( 'out',_stdout.read().decode())
print( 'err', _stderr.read().decode())
_stdin.close()

_stdin, _stdout, _stderr = client.exec_command("df")
print(_stdout.read().decode())
print(_stderr.read().decode())
_stdin.close()

_stdin, _stdout,_stderr = client.exec_command("ls -l /")
print(_stdout.read().decode())
_stdin.close()

_stdin, _stdout,_stderr = client.exec_command("pwd")
print(_stdout.read().decode())
_stdin.close()


if client :
    client.close()
