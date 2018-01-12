import sys
import logging

def error_handling():
    return 'Error: {} {}'.format(sys.exc_info()[0],
                                 sys.exc_info()[1],
                                 sys.exc_info()[2].db_lineno)

try:
    a + b
except:
    logging.error(error_handling())
