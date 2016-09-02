# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:53:00 2016

@author: lstanevich
"""

from exception_decor import exception
from exception_logger import logger
 
@exception(logger)
def zero_divide():
    1 / 0
 
if __name__ == '__main__':
    logger.info("TEST")