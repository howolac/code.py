#!python
import logging
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s\
- %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start debug')

#项目：debug
'''

'''
#usage:

import os
logging.info('import is working')

#for语句,遍历到10
for i in range(13):
    print('i = ' + str(i))
    #触发AssertionError
    assert i < 10, str(i) + 'must be <10'
    i += 1
