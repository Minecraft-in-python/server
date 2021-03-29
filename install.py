#!/usr/bin/python3
from hashlib import sha256
from json import dump
from os import path
from sys import platform

VERSION = '0.3.1'

def install():
    # 安装
    print('This is server %s installation script.')
    input('Press ENTER to install server: ')
    file = path.join(search_mcpy(), 'server')
    data = {
            'long-desc': 'description.long',
            'short-desc': 'description.short',
            'password': sha256('123'.encode()).hexdigest(),
            'port': 16384
            }
    dump(data, open(path.join(search_mcpy(), 'server.json'), 'w+'), indent='\t')

def search_mcpy():
    # 寻找文件存储位置
    _os = __import__('os')
    environ, path = _os.environ, _os.path
    if 'MCPYPATH' in environ:
        MCPYPATH = environ['MCPYPATH']
    elif platform == 'darwin':
        MCPYPATH = path.join(path.expanduser('~'), 'Library', 'Application Support', 'mcpy')
    elif platform.startswith('win'):
        MCPYPATH = path.join(path.expanduser('~'), 'mcpy')
    else:
        MCPYPATH = path.join(path.expanduser('~'), '.mcpy')
    return MCPYPATH

if __name__ == '__main__':
    install()
