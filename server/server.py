from json import dumps, loads
from socketserver import BaseRequestHandler
import time

from server.player import PlayerManager
from server.source import settings
from server.utils import *


class ServerHandler(BaseRequestHandler):

    def setup(self):
        log_info('Receive data ftom %s@%d' % self.client_address)
        data = self.request.recv(1024).decode()
        if data == 'client':
            self.type = 'client'
            self.request.send(('server {"version" : %s, "str": "%s"}' % (VERSION['data'], VERSION['str'])).encode())
            data = self.request.recv(1024).decode()
            if data.startswith('client '):
                if loads(data[7:])['version'] != VERSION['data']:
                    self.request.send('refuse'.encode())
                    self.success = False
                else:
                    self.request.send('get_player'.encode())
                    data = self.request.recv(1024).decode()
                    if data.startswith('player '):
                        data = loads(data[7:])
                        log_info('New player: %s, %s' % (data['name'], data['id']))
                        self.request.send(('welcome %s' % data['name']).encode())
                        self.success = True
                    else:
                        self.success = False
                        self.request.send('refuse'.encode())
        elif data == 'get_info':
            self.type = 'get_info'
            data = {
                    'description.long': settings['description.long'],
                    'description.short': settings['description.short'],
                    'time': time.time(),
                }
            self.request.send(dumps(data).encode())
            self.success = False
        else:
            self.success = False
            self.request.send('refuse'.decode())

    def handle(self):
        pass

    def finish(self):
        if self.type == 'client':
            log_info('%s quit server' % 'PLAYER')
