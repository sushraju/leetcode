#!/usr/bin/env python
import sys

def writeout(text, times=1):
    for i in range(times):
        sys.stdout.write(text)

def decompress(text):
    times_str = ''
    i = 0
    while i < len(text):
        if text[i].isdigit():
            times_str += text[i]
            i += 1
            continue
        else:
            subtext = ''
            if text[i] == '[':
                for j in range(i+1, len(text)):
                    if text[j] != ']':
                        subtext += text[j]
                    else:
                        times = int(times_str)
                        writeout(subtext,times)
                        times_str = ''
                        i = j + 1
                        break


if __name__ == "__main__":
    decompress('10[abc4[xyz]]')