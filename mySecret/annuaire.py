#!/usr/bin/python3
# -*- coding: utf-8  -*-

# pip install paramiko

import paramiko


playbook =  {

                'phil' : { 'login': 'phil', 'ip' : '172.16.0.177', 'pw': 'password'  },
                'toto' : { 'login': 'toto', 'ip' : '172.16.0.72', 'pw': 'toto'  }
            }

