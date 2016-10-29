#!/usr/bin/env python

import logging
import yaml



#logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
                    
logger = logging.getLogger(__name__)




def main(args):
    logger.info('FizzBuzz Test')
    
    for n in range(1,21):
		if (n%3 == 0 and n%5 == 0):
			logger.debug('Divisivel por 3 e 5')
			print str(n) + " - FizzBuzz"
		elif n%3 == 0:
			print str(n) + " - Fizz"
		elif n%5 == 0:
			print str(n) + " - Buzz"
		else:
			print n
		
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
