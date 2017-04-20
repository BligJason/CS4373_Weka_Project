import csv
import itertools
import hero_roles

#with open("d:datamining/datasets/datasets/dota2Dataset/dota2Test.csv", 'r') as file:
with open("/home/dha861/courses/cs/4373/dota2Test.csv", 'r') as file:
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
            if index > 3 and int(item) == 1:
                current_rad_team.append(hero_roles.Role[first[index]])
            if index > 0 and int(item) == -1:
                current_dire_team.append(hero_roles.Role[first[index]])
            index += 1
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

    for team, record in itertools.zip_longest(wteams, team_record):
        if int(record) >= 2: 
            print(team, record)


