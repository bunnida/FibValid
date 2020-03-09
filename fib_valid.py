#!/usr/bin/env python3


EXIT_CODE_SUCCESS, EXIT_CODE_FAIL = 0, 1
def _Exit(Msg=None, ErrCode=None):
    if Msg: print(Msg)

    import sys
    sys.exit(EXIT_CODE_FAIL if ErrCode else EXIT_CODE_SUCCESS)


def _LoadWebPageAndExtractBaseNumberPair(FibNumberIndex):
    BASE_URL = 'http://www.protocol5.com/Fibonacci/{}.htm'
    url = BASE_URL.format(FibNumberIndex)
    try:
        import urllib.request as url_req
        html = url_req.urlopen(url).read().decode('utf-8')
    except BaseException as E:
        _Exit("Could not access web page: '{}'".format(E), EXIT_CODE_FAIL)

    pairs = []
    import re
    first_screen = re.findall('<li><h4>.*?</li>', html)
    for line in first_screen:
        base, num = re.findall(' ([0-9]*):.*v>(.*)</d', line)[0]
        pairs.append([base, num])

    return pairs


def main():
    pairs = _LoadWebPageAndExtractBaseNumberPair(999001)
    for p in pairs: print(p)

    _Exit()


if __name__ == '__main__':
    main()
