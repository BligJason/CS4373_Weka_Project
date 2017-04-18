import csv

with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
	reader = csv.reader(file)
	first = next(reader)
	count = list()
	win = 0
	win_record = list()
	
	for item in first:
		count.append(0)
		win_record.append(0)
	for line in file.readlines():
		line.strip()
		index = 0
		for item in line.split(','):
			item.strip()
			if int(item) == 1 or int(item) == -1:
				count[index] += 1
			if index == 0:	
				win = int(item)
			if int(item) == win:
				win_record[index] += 1
			index += 1
			
	with open("d:datamining/datasets/datasets/dota2Dataset/output.txt", 'w+') as output:		
		pop_champs = dict()
		index = 0
		for item in first:
			if win_record[index] == 0:
				pop_champs[item] = [count[index],win_record[index], win_record[index]]
			else:
				pop_champs[item] = [count[index],win_record[index],(win_record[index]/count[index])]
			index += 1
		del pop_champs['idk']
		del pop_champs['idk1']
		del pop_champs['idk2']
				
		output.write("{},{},{},{}\n".format('Champion','GamesPlayed','GamesWon','WinRate'))
		for item in reversed(sorted(pop_champs.items(), key=lambda x:x[1][2])):
			if item[1] == pop_champs['radiant_victory_yes_no']:
				continue
			output.write("{:s},{:d},{:d},{:.3g}\n".format(item[0], item[1][0], item[1][1], item[1][2]))