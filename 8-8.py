# http://tinyurl.com/gvcdgxf

#  ここで開くファイルは、
#  前のコード例を実行して
#  作られます。

import csv

with open("st.csv", "r") as f:
	r = csv.reader(f, delimiter=",")
	for row in r:
		print(",".join(row))
