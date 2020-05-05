# http://tinyurl.com/hg9sw3u

import re

string = "Two too."

m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

