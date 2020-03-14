#!/usr/bin/env python
import sys
import getopt

LOG_LEVELS = {
    'DEBUG': 4,
    'INFO': 3,
    'WARN': 2,
    'ERROR': 1,
    'FATAL': 0,
}


def usage():
    print('This is to test verbose and quite log levels. Levels are DEBUG, INFO, WARN, ERROR, FATAL')
    print('Usage: ' + sys.argv[0])
    print('       -v verbose levels, -vv, -vvv, DEFAULT is WARN.')
    print('       -q suppress logs, DEFAULT is WARN.')
    print('       -h help')


def log(log_level_str, text):
    if LOG_LEVELS[log_level_str] <= LOG_LEVELS[_def_l_level]:
        print(text)


def init(argv):
    global _def_l_level, _def_l_level_num, _min_l_level_num, _max_l_level_num
    _def_l_level = 'ERROR'
    _def_l_level_num = LOG_LEVELS[_def_l_level]
    _min_l_level_num = 0
    _max_l_level_num = 4

    print('Initial default log level is set to ' + _def_l_level + '\n')
    if len(argv) > 0:
        try:

            for arg in argv:
                if arg == '-h':
                    usage()
                    sys.exit(0)
                elif arg == '-v':
                    if (_def_l_level_num + 1) <= _max_l_level_num:
                        _def_l_level_num = _def_l_level_num + 1
                elif arg == '-q':
                    if (_def_l_level_num - 1) >= _min_l_level_num:
                        _def_l_level_num = _def_l_level_num - 1
                else:
                    usage()
                    sys.exit(1)

            for levels in LOG_LEVELS.items():
                if levels[1] == _def_l_level_num:
                    _def_l_level = levels[0]

        except getopt.GetoptError:
            print('ERROR: Invalid flag passed. Please see valid input below.')
            usage()
            sys.exit(1)
    else:
        print("\nNo arguments passed, continuing...\n")

def main(argv):
    init(argv)

    # test logs
    print('Modified log verbosity to ' + _def_l_level + ' per args.  Logging anything ' + _def_l_level + ' and higher\n')
    log('DEBUG', "This is DEBUG message")
    log('INFO', "This is INFO message")
    log('WARN', "This is WARN message")
    log('ERROR', "This is ERROR message")
    log('FATAL', "This is FATAL message")


if __name__ == "__main__":
    main(sys.argv[1:])
