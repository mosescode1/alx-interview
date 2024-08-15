#!/usr/bin/python3
'''
Log parsing
'''
import sys


if __name__ == "__main__":
    '''
    Run only when not imported
    '''
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0
    size = 0

    def print_res(status, size):
        '''
        Print result
        '''
        print("File size: {}".format(size))
        status = dict(sorted(status.items()))
        for k, v in status.items():
            if v > 0:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            ln = line.split(" ")
            try:
                code = ln[-2]
                size += int(ln[-1])
                if code in status.keys():
                    status[code] += 1
            except BaseException:
                pass
            if count == 10:
                print_res(status, size)
                count = 0

    except KeyboardInterrupt:
        print_res(status, size)
    print_res(status, size)
