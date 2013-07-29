#! -*- coding:utf8 -*-

import os
from fabric.api import *
from fabric.colors import green, red

REMOTE_BASE_PATH='/home/fabrizzio23/deploy/'

env.hosts = ['127.0.0.1']
env.user = 'fabrizzio23'

def hola():
    print("¡Hola!")

def pull_github():
   #if os.path.exists('/tmp/sites.zip'):
   #	local('rm -r /tmp/sites.zip')

   #local('git archive --format=zip --prefix=sites/ HEAD > /tmp/sites.zip')

   # put('/tmp/sites.zip' , '/tmp/')

   # with cd(REMOTE_BASE_PATH):
   #	run('unzip -o /tmp/sites.zip')
   local('git pull origin master')
   


def install_deps():
    with cd(REMOTE_BASE_PATH):
	with prefix('source ' + REMOTE_BASE_PATH + 'envs/prodigital/bin/activate'):
	    run('pip install -r ' + REMOTE_BASE_PATH + 'sites/prodigital/requirements/requirements.txt')
