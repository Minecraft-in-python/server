#!/usr/bin/python3
from hashlib import sha256
from json import dump
from os import path
from sys import platform

VERSION = '0.3.2'

def install():
    # 安装
    print('This is server %s installation script.' % VERSION)
    input('Press ENTER to install server: ')
    file = path.join(search_mcpy(), 'server')
    data = {
            'description.long': 'description.long',
            'description.short': 'description.short',
            'port': 15425
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
