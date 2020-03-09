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


def _LoadWebPageAndExtractBaseNumberPair(FibNumberIndex):
    BASE_URL = 'http://www.protocol5.com/Fibonacci/{}.htm'
    url = BASE_URL.format(FibNumberIndex)
    try:
        import urllib.request as url_req
        html = url_req.urlopen(url).read().decode('utf-8')
    except BaseException as E:
        _ExitError("Could not access web page: '{}'".format(E))

    pairs = []
    import re
    first_screen = re.findall('<li><h4>.*?</li>', html)
    for line in first_screen:
        base, num = re.findall(' ([0-9]*):.*v>(.*)</d', line)[0]
        pairs.append([base, num])

    return pairs


def main():
    pairs = _LoadWebPageAndExtractBaseNumberPair(300)
    for p in pairs: print(p)


if __name__ == '__main__':
    main()
