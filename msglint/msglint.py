#!/usr/bin/env python

import sys
import os
from POFile import POFile
import logging

def check_msg_lint(moduledir):
    dapo = os.path.join(moduledir, 'i18n', "da.po")
    po = POFile(dapo)
    if not po.validate():
        print po.validateError

def main():
    if len( sys.argv ) == 2 and os.path.isdir(sys.argv[1]):
        check_msg_lint(sys.argv[1])
    else:
        logging.warning("First param should be directoy path to check")


if __name__ == '__main__':
    exit(main())
