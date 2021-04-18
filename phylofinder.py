in1 = "B935 B2247 B4142 B1908 B2249 B2302 B75 B3926 B1489 B279 B1572 B3866 B4498 B1776 B345"
in2 = "B285 B3804 B2302 B1616 B1764 B2344 B2105 B2417 B3967 B2717 B206 B2153 B2197 B4498 B842"
in3 = "B652 B2197 B2276 B75 B4618 B2310 B2302 B1054 B4627 B3061 B932 B2175 B2518 B1359 B937"

with open("phylogroups_v2.txt","r") as in4:
	list1 = [line.split("\t") for line in in4.read().splitlines()]




o1 = in1.split()
o2 = in2.split()
o3 = in3.split()

for i in list1:
	if i[0] in o3:
		print(i)