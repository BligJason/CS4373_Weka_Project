import csv
with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
	reader = csv.reader(file)
	first = next(reader)
	count = list()
	for item in first:
		count.append(0)
	for line in file.readlines():
		line.strip()
		index = 0
		for item in line.split(','):
			item.strip()
			if int(item) == 1 or int(item) == -1:
				count[index] += 1
			index += 1
	print(count)
	
			