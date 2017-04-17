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
	with open("d:datamining/datasets/datasets/dota2Dataset/output.txt", 'w+') as output:		
		pop_champs = dict()
		index = 0
		for item in first:
			pop_champs[item] = count[int(index)]
			index += 1
		output.write("Champion GamesPlayed\n")	
		for item in reversed(sorted(pop_champs.items(), key=lambda x:x[1])):
			#if item[1] >= pop_champs['radiant_victory_yes_no']*.2:
			if item[1] == pop_champs['radiant_victory_yes_no']:
				continue
			output.write(" ".join(map(str, item)))
			output.write("\n")