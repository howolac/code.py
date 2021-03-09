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

#列表
eggs = ['10a', '1']
bacon = ['1', '10A']

#切换一下大小写：
eggs = (('***'.join(eggs)).lower()).split('***')
bacon = (('***'.join(bacon)).lower()).split('***')

#令彼此不相同!
assert eggs == bacon, 'eggs and bacon can\'t be same'
