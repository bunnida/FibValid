#!/usr/bin/env python3

EXIT_PROG_FAIL, EXIT_ANSWER_INCORRECT, EXIT_ANSWER_CORRECT = 2, 1, 0
def _Exit(ErrCode, Msg=None):
    if Msg: print(Msg)

    import sys
    sys.exit(ErrCode)

def _LoadWebPageAndExtractBaseNumberPair(FibNumberIndex):
    url = 'http://www.protocol5.com/Fibonacci/{}.htm'.format(FibNumberIndex)

    import urllib.request as url_req
    try: html = url_req.urlopen(url).read().decode('utf-8')
    except BaseException as E: _Exit(EXIT_PROG_FAIL, "Could not access web page: '{}'".format(E))

    pairs = []
    import re
    for line in re.findall('<li><h4>.*?</li>', html):
        pairs.append(  re.findall(' ([0-9]*):.*v>(.*)</d', line)[0]  )

    return pairs

def main():
    pairs = _LoadWebPageAndExtractBaseNumberPair(300)
    for p in pairs: print(p)

    _Exit(EXIT_ANSWER_CORRECT)

if __name__ == '__main__':
    main()
