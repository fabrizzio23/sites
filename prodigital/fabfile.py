#! -*- coding:utf8 -*-

import os
from fabric.api import *
from fabric.colors import green, red

REMOTE_BASE_PATH='/home/fabrizzio23/deploy/'

env.hosts = ['127.0.0.1']
env.user = 'fabrizzio23'

def hola():
    print("¡Hola!")

def pullgit():
    local('git pull origin master')
   


def install_deps():
    with cd(REMOTE_BASE_PATH):
	with prefix('source ' + REMOTE_BASE_PATH + 'envs/prodigital/bin/activate'):
	    run('pip install -r ' + REMOTE_BASE_PATH + 'sites/prodigital/requirements/requirements.txt')
