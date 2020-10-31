#!/usr/bin/env python


def log_restrict(source_fd, max_files, max_size, prefix):
    """Reads and writes to log files based on max bytes read"""
    line = source_fd.readline(max_size)
    line_size = 0
    fn_ctr = 1
    output_file = './' + 'prefix' + '_' + str(fn_ctr) + '.log'
    op = open(output_file, 'a')
    op.truncate(0)
    while line:
        line_size = line_size + len(line)

        if line_size <= max_size:
            op.write(line)
        else:
            op.close()
            if fn_ctr < max_files:
                fn_ctr = fn_ctr + 1
            else:
                fn_ctr = 1

            output_file = './' + 'prefix' + '_' + str(fn_ctr) + '.log'
            op = open(output_file, 'a')
            op.truncate(0)
            op.write(line)
            line_size = 0

        line = source_fd.readline(max_size)


def main():
    source_fd = open("./input_text.log", 'r')
    log_restrict(source_fd, 5, 1000, 'app')
    source_fd.close()


if __name__ == "__main__":
    main()
