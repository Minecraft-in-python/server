from socketserver import ThreadingTCPServer

from server.server import ServerHandler
from server.source import settings
from server.utils import *

if __name__ == '__main__':
    server = ThreadingTCPServer(('localhost', settings['port']), ServerHandler)
    log_info('Server start: localhost@%s' % settings['port'])
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        log_info('Server stop')
