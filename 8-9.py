# http://tinyurl.com/gvcdgxf #  ここで開くファイルは、 #  前のコード例を実行して
#  作られます。

import csv

with open("st.csv", "r") as f: 
	r = csv.reader(f, delimiter=",")
	for row in r:
		print("\n".join(row))
#  csv.readerは改行された各行を2次元のlistの構造として読み込む
#  よって、下記のコードを実行すると改行された各行は複数のlistとして
#  表示される。
#  print(row)
#  ['one', 'two', 'three']
#  ['four', 'five', 'six']
#


