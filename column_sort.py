import csv

reader = csv.DictReader(open('online_news_pop_TRAIN.csv', 'r'))
result = sorted(reader, key=lambda d: float(d['shares']))

writer = csv.DictWriter(open('online_news_pop_TRAIN.csv', 'w'), reader.fieldnames)
writer.writeheader()
writer.writerows(result)
