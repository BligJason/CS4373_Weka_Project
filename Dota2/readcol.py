#Script for calculating how much each champ was played

#output -> champion list and amount of games played. List only those played more than
#1/5 of all games
import csv

with open("d:datamining/datasets/datasets/dota2Dataset/dota2Train.csv", 'r') as file:
    reader = csv.reader(file)
    first = next(reader)
    count = list()
    for item in first:
        count.append(0)
	#iterate through each row and count the number of times each champion was played	
    for line in file.readlines():
        line.strip()
        index = 0
        for item in line.split(','):
            item.strip()
            if int(item) == 1 or int(item) == -1:
                count[index] += 1
            index += 1
    with open("d:datamining/datasets/datasets/dota2Dataset/pchamps.txt", 'w+') as output:		    
        pop_champs = dict()
        index = 0
        #iterate through dictionary and add games played to their respective champions
		for item in first:
            pop_champs[item] = count[int(index)]
            index += 1
        output.write("Champion GamesPlayed\n")
		#sort and iterate trough dicitionary and print out champions that meet criteria
        for item in reversed(sorted(pop_champs.items(), key=lambda x:x[1])):
            if item[1] >= pop_champs['radiant_victory_yes_no']*.2:
                if item[1] == pop_champs['radiant_victory_yes_no']:
                    continue
                output.write(" ".join(map(str, item)))
                output.write("\n")
