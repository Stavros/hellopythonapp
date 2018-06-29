#!/usr/bin/env python3

import sys
if path not in sys.path:
    sys.path.append(path)
from hellopythonapp import app as application

if __name__ == '__main__':
    application.run( host='0.0.0.0' )
