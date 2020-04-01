#!/usr/bin/env python
import argparse
import sys

LOG_LEVELS = ["FATAL", "ERROR", "WARN", "INFO", "DEBUG"]


# log messages of severity default log level and lower
# for e.g., if set to WARN, messages of type WARN, ERROR and FATAL will be logged.
def log(log_level_str, text):
    if LOG_LEVELS.index(log_level_str) <= LOG_LEVELS.index(_def_l_level):
        print(text)


def main(argv):
    global _def_l_level, _def_l_level_num, _min_l_level_num, _max_l_level_num
    _def_l_level = 'WARN'
    _def_l_level_num = LOG_LEVELS.index(_def_l_level)
    _min_l_level_num = 0
    _max_l_level_num = 4

    print('\nLog levels in increasing order of verbosity: ' + str(LOG_LEVELS))
    print('\nInitial default log level is set to ' + _def_l_level + '\n')

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--verbose", "-v",
        dest="log_level",
        action="append_const",
        const=1,
    )
    parser.add_argument(
        "--quiet", "-q",
        dest="log_level",
        action="append_const",
        const=-1,
    )

    args = parser.parse_args(argv[1:])
    if args.log_level is not None:
        for log_level in args.log_level:
            _def_l_level_num = _def_l_level_num + log_level

        if _def_l_level_num < _min_l_level_num:
            _def_l_level_num = _min_l_level_num

        if _def_l_level_num > _max_l_level_num:
            _def_l_level_num = _max_l_level_num

    _def_l_level = LOG_LEVELS[_def_l_level_num]

    print('Modified log verbosity to ' + _def_l_level + ' per args. Logging ' + _def_l_level + ' and lower.\n')

    # test log levels
    log('DEBUG', "This is DEBUG message")
    log('INFO', "This is INFO message")
    log('WARN', "This is WARN message")
    log('ERROR', "This is ERROR message")
    log('FATAL', "This is FATAL message")


if __name__ == "__main__":
    main(sys.argv)
