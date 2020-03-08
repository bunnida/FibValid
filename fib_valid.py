#!/usr/bin/env python3

import sys


EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAIL    = 1
def _ExitError(Msg=None):
    if Msg: print(Msg)
    sys.exit(EXIT_CODE_FAIL)
def _ExitNormal(Msg=None):
    if Msg: print(Msg)
    sys.exit(EXIT_CODE_SUCCESS)


def _ExtractToken(Source, BeginString, EndString):
    p = Source.find(BeginString) + len(BeginString)
    q = Source.find(EndString, p + 1)

    return '-1' if p < 0 or q < 0 else Source[p:q]


def main():
    FIB_NUM_INDEX = '300'
    BASE_DICT = {
         2: 'Base 2:</h4><div>'   ,
        10: 'Base 10:</h4><div>'  ,
        16: 'Radix 16:</h4><div>' }
    BASE_END = '</div>'
    BASE_URL = 'http://www.protocol5.com/Fibonacci/{}.htm'

    url = BASE_URL.format(FIB_NUM_INDEX)

    try:
        import urllib.request as url_req
        html = str(url_req.urlopen(url).read())
    except BaseException as E:
        _ExitError("Could not access web page: '{}'".format(E))

    for base in sorted(BASE_DICT.keys()):
        fib_num = _ExtractToken(html, BASE_DICT[base], BASE_END)
        print('{} {}(base:{})'.format(FIB_NUM_INDEX, fib_num, base))

    _ExitNormal()


if __name__ == '__main__':
    main()
