import sys
import os
import re

def usage():
    print "[Usage]: python grep.py filename grepString."



if len(sys.argv) != 3:
    usage()
    sys.exit(1)

if os.path.isfile(sys.argv[1]):
    pass
else:
    usage()
    sys.exit(2)

f = open(sys.argv[1])
content = f.read()
f.close()
s = "\n".join(re.findall(sys.argv[2]+'.*', content))
print s
