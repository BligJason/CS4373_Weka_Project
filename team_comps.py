import csv

with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
	reader = csv.reader(file)
	first = next(reader)
	wteams = list()
	team_record = list()
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
		#if rad_win == 1:
			#current_rad_team.append(1)
			#wteams.append(current_rad_team)
			#for item in wteams:
			#	print(item)
			#	break	
				#if item[0:4] == current_rad_team:	
				#	item[5] += 1
				#else:
				#	current_rad_team.append(1)
				#	wteams.append(current_rad_team)	
			#if current_rad_team in list:
			#	wteams[wteams.index(current_rad_team)][5] += 1
		if dire_win == 1:
			check = 0
			for item in wteams:
				if list(item) == current_dire_team:
					check = 1
					team_record[wteams.index(current_dire_team)] += 1
					break	
			if check != 1:
				wteams.append(current_dire_team)
				team_record.append(1)
			check = 0		
			#if current_dire_team not in list:
		#	current_dire_team.append(1)
		#	wteams.append(current_dire_team)
			#if current_dire_team in list:
			#	wteams[wteams.index(current_dire_team)][5] += 1
	print(wteams)
			