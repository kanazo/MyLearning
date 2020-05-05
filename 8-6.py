# http://tinyurl.com/hkzhxdz

my_list = []

with open("st.txt", "r") as f:
	my_list.append(f.read())

for i, new in enumerate(my_list):
	new = my_list[i]
	i += 1
	print(new)

 
