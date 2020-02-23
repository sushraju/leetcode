#!/usr/bin/env python

def log_restrict(source_fd, max_files, max_size, prefix):
    line = source_fd.readline(max_size)
    linesize = 0
    fn_ctr = 1
    output_file = './' + 'prefix' + '_' + str(fn_ctr) + '.log'
    op = open(output_file, 'a')
    op.truncate(0)
    while line:
        linesize = linesize + len(line)
        #print(linesize)
        if linesize <= max_size:
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
            linesize = 0
	
        line = source_fd.readline(max_size)


def main():
    source_fd = open("./input_text.log", 'r')
    log_restrict(source_fd, 5, 1000, 'app')
    source_fd.close()


if __name__ == "__main__":
    main()
