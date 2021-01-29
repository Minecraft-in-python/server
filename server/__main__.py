from sys import argv

from server import console
from server import server
from server import setpass
from server.utils import *

if __name__ == '__main__':
    if len(argv) == 1 or argv[1] == 'server':
        server.Server().start()
    elif len(argv) == 2 and argv[1] == 'console':
        console.Console().start()
    elif len(argv) == 2 and argv[1] == 'setpass':
        setpass.set_password()
    elif len(argv) == 2 and argv[1] == 'help':
        print('Minecraft server version %s' % VERSION['str'])
        print('usage: python -m server <server|console|help>\n')
        print('arguments:')
        print('  server  - start a server(default)')
        print('  console - run a console')
        print('  setpass - set password')
        print('  help    - show this help')
    else:
        print('usage: python -m server <server|console|setpass|help>')
