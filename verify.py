#!/usr/bin/python
"""
    Script to verify the functionality of a loadbalancer
"""

import argparse
import re
import urllib2
from collections import defaultdict


class Verify(object):
    ''' Main class for the verification '''
    def __init__(self):

        parser = argparse.ArgumentParser(description='Verify loadbalancer activity.')
        parser.add_argument('--number', '-n', type=int, nargs='+', \
            help='number of requests to be sent to the loadbalancer')
        self.args = parser.parse_args()


    def execute(self):
        ''' Execution function iteracts over the amount of connections
        and reports the headers from backend servers '''
        limit = 100
        stats = defaultdict(int)
        if self.args.number:
            limit = self.args.number[0]
        regex = re.compile('Backend.')
        for connection in range(0, limit):
            response = urllib2.urlopen('http://localhost:6666/')
            matches = [backend for backend in response.info().headers if re.match(regex, backend)]
            key = matches[0].split(':')[1].strip()
            stats[key] += 1
        for key in stats:
            print key + ':', stats[key]


if __name__ == '__main__':
    Verify().execute()
