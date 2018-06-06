import re
import string

fd = open("slabinfo.txt", 'r')
total_slab_mem = 0
for lines in fd.readlines():
    lines_str = ''.join(lines)
    args = re.split(r'\s+',lines_str)
    if len(args) > 5 and args[5].isdigit() and args[-3].isdigit():
        pagesperslab = float(args[5])
        slabnums = float(args[-3])
        slabmem = ((pagesperslab) * (slabnums) * 4)/1024
        print('Slabmem: %0.3fMb %s' % (slabmem, lines_str))
    else:
        print(lines_str)
        continue
    total_slab_mem = total_slab_mem + slabmem
print("Total slab mem is %0.3fMb" % total_slab_mem)
