#!/usr/bin/env python3

if path not in sys.path:
    sys.path.append(path)
    
import sys
from myapp import app as application

if __name__ == '__main__':
    application.run( host='0.0.0.0' )
