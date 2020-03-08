#!/usr/bin/env python3

import sys
import urllib.request


FIB_NUM_INDEX = -1
BASE_URL = 'http://www.protocol5.com/Fibonacci/{}.htm'

EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAIL    = 1

BASE_DICT = {
      2: 'Base 2:</h4><div>'   ,
     10: 'Base 10:</h4><div>'  ,
     16: 'Radix 16:</h4><div>' }
BASE_END = '</div>'

def _ExtractToken(Source, BeginString, EndString):
    p = Source.find(BeginString) + len(BeginString)
    q = Source.find(EndString, p + 1)

    token = Source[p:q]

    return token

def _PrintErrorMessageAndExit(Msg):
    print(Msg)
    sys.exit(EXIT_CODE_FAIL)


def main():
    FIB_NUM_INDEX = '300'
    url = BASE_URL.format(FIB_NUM_INDEX)

    try:
        html = str(urllib.request.urlopen(url).read())
    except BaseException as E:
        _PrintErrorMessageAndExit("Could not access web page: '{}'".format(E))

    for base in sorted(BASE_DICT.keys()):
        fib_num = _ExtractToken(html, BASE_DICT[base], BASE_END)
        print('{} {}(base:{})'.format(FIB_NUM_INDEX, fib_num, base))

    sys.exit(EXIT_CODE_SUCCESS)


if __name__ == '__main__':
    main()
