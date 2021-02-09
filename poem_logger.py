#!/usr/bin/env python
from io import StringIO


def poem_log(source_fd, max_files, max_lines, prefix):
    line = source_fd.readline()
    fn_ctr = 1
    output_file = './' + prefix + '_' + str(fn_ctr) + '.log'
    op = open(output_file, 'a')
    op.truncate(0)
    line_count = 0
    while line:
        if line_count < max_lines:
            op.write(line)
            line_count += 1
        else:
            op.close()
            if fn_ctr < max_files:
                fn_ctr = fn_ctr + 1
            else:
                fn_ctr = 1
            output_file = './' + prefix + '_' + str(fn_ctr) + '.log'
            op = open(output_file, 'a')
            op.truncate(0)
            op.write(line)
            line_count = 1
            
        line = source_fd.readline()


def main():
    source_poem = """It little profits that an idle king,
By this still hearth, among these barren crags,
Match'd with an aged wife, I mete and dole
Unequal laws unto a savage race,
That hoard, and sleep, and feed, and know not me.
I cannot rest from travel: I will drink
Life to the lees: All times I have enjoy'd
Greatly, have suffer'd greatly, both with those
That loved me, and alone, on shore, and when
Thro' scudding drifts the rainy Hyades
Vext the dim sea: I am become a name;
For always roaming with a hungry heart
Much have I seen and known; cities of men
And manners, climates, councils, governments,
Myself not least, but honour'd of them all;
And drunk delight of battle with my peers,
Far on the ringing plains of windy Troy.
"""
    source_fd = StringIO(source_poem)
    poem_log(source_fd, 4, 4, 'poem')

    
if __name__ == "__main__":
    main()