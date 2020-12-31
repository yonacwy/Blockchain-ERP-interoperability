import socket
from json import JSONEncoder
import datetime
import logging
import sys
import json
_logger=logging.getLogger(__name__)

class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def connect_send(data):
    _logger.info('CONNECTION SUCCESSFUL')
    _logger.info(data)
    #### TCP ####
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    sock.connect(server_address)

    try:
        # Send data
        message = data
        print(sys.stderr, 'sending "%s"' % message)
        s = json.dumps(data, indent=4, cls=DateTimeEncoder)
        sock.sendall(bytes(s, encoding="utf-8"))

    finally:
        print(sys.stderr, 'closing socket')
        sock.close()
    #### END ####