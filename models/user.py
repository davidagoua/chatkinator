import os
from socket import *


class Client(object):

    host = 'localhost'
    port = 4001
    connecter = False

    def __init__(self, username=None):
        self.username = username
        self.connecter = True

