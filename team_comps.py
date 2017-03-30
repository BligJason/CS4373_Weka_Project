import csv

with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
	reader = csv.reader(file)
	first = next(reader)
	teams = dict()
	dc = 0
	rc = 0
	for line in file.readlines():
		current_rad_team = list()
		current_dire_team = list()
		line.strip()
		index = 0
		rad_win = 0
		dire_win = 0
		for item in line.split(','):
			item.strip()
			if index == 0 and int(item) == 1:
				rad_win = 1
				rc += 1
			if index == 0 and int(item) == -1:
				dire_win = 1
				dc += 1
			if index > 0 and int(item) == 1:
				current_rad_team.append(first[index])
			if index > 0 and int(item) == -1:
				current_dire_team.append(first[index])
			index += 1
		print(current_dire_team)
		break
			