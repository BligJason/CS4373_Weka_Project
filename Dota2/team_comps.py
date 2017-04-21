# Script for creating the team compositions existing in 
# the data set.

# output -> txt file with all winning team compositions and number of wins for that composition
import csv
import itertools

with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
	reader = csv.reader(file)
	first = next(reader)
	wteams = list()
	team_record = list()
	dc = 0
	rc = 0
	gamecount = 0
	for line in file.readlines():
		current_rad_team = list()
		current_dire_team = list()
		line.strip()
		gamecount += 1
		index = 0
		rad_win = 0
		dire_win = 0
		# iterate through each row and build up the current teams
		for item in line.split(','):
			item.strip()
			if index == 0 and int(item) == 1:
				rad_win = 1
				rc += 1
			if index == 0 and int(item) == -1:
				dire_win = 1
				dc += 1
			if index > 3 and int(item) == 1:
				current_rad_team.append(first[index])
			if index > 3 and int(item) == -1:
				current_dire_team.append(first[index])
			index += 1
		# add current radiant team to winning if radiant win	
		if rad_win == 1:
			check = 0
			for item in wteams:
				if list(item) == current_rad_team:
					check = 1
					team_record[wteams.index(current_rad_team)] += 1
					break
			if check != 1:
				wteams.append(current_rad_team)
				team_record.append(1)
			check = 0
		# add current dire team to winning if dire win	
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
	with open("d:datamining/datasets/datasets/dota2Dataset/win_teamcomp.txt", 'w+') as output:		
		#iterate through and print out each winning team composition and their win record
		for team, record in itertools.zip_longest(wteams, team_record): 
				output.write("{} {}\n".format(team, record))