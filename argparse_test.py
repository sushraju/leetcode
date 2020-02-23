#!/usr/bin/env python
import argparse
import sys

LOG_LEVELS = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]


def log(log_level_str, text):
    if LOG_LEVELS.index(log_level_str) <= LOG_LEVELS.index(_def_l_level):
        print(text)


def main(argv):
    global _def_l_level, _def_l_level_num, _min_l_level_num, _max_l_level_num
    _def_l_level = 'WARN'
    _def_l_level_num = LOG_LEVELS.index(_def_l_level)
    _min_l_level_num = 0
    _max_l_level_num = 4

    print(LOG_LEVELS)
    print('Initial default log level is ' + _def_l_level)

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
    for log_level in args.log_level:
        _def_l_level_num = _def_l_level_num + log_level

    if _def_l_level_num < _min_l_level_num:
        _def_l_level_num = _min_l_level_num

    if _def_l_level_num > _max_l_level_num:
        _def_l_level_num = _max_l_level_num

    _def_l_level = LOG_LEVELS[_def_l_level_num]

    print('Current default log level is ' + _def_l_level)

    # test log levels
    log('DEBUG', "This is DEBUG message")
    log('INFO', "This is INFO message")
    log('WARN', "This is WARN message")
    log('ERROR', "This is ERROR message")
    log('FATAL', "This is FATAL message")


if __name__ == "__main__":
    main(sys.argv)
