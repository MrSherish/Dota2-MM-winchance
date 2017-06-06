import csv

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.preprocessing import scale
from sklearn.svm import SVC

import requests


def classify(_train_data: list, _test_data: list):
	dota_x = list()
	dota_y = list()
	for _entry in _train_data:
		dota_x.append((_entry[1:-1]))
		dota_y.append(_entry[-1])
	for _entry in _test_data:
		dota_x.append((_entry[1:-1]))
		dota_y.append(_entry[-1])
	dota_x = scale(dota_x)
	svc = BaggingClassifier(SVC(kernel="rbf", class_weight='balanced', shrinking=True, probability=False))
	scores = cross_val_score(svc, dota_x, dota_y, cv=10)
	print(scores)


def get_from_file(_filename="data.csv") -> list:
	with open(_filename, 'r') as file:
		reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
		return list(reader)


def write_to_csv(_data: list):
	with open("data.csv", mode='w') as file:
		for _row in _data:
			data_row = str(_row[0])
			for _entry in _row[1:]:
				data_row += "," + str(_entry)
			print(data_row, file=file)


def get_from_web() -> list:
	pro_games = requests.request_pro_matches(90000000)
	pro_matches = map(lambda x: requests.get_match_info(x['match_id']), pro_games)
	pro_players = [item['players'] for item in pro_matches]
	pro_players = [item for sublist in pro_players for item in sublist]

	benchmarks = [player['benchmarks'] for player in pro_players]
	players = [player['account_id'] for player in pro_players]
	wins = [player['win'] for player in pro_players]
	player_benchmarks_tuple = list(zip(players, benchmarks, wins))

	data = list()
	for entry in player_benchmarks_tuple:
		row = list()
		row.append(entry[0])
		for benchmark in entry[1].values():
			if 'raw' in benchmark.keys():
				row.append(benchmark['raw'])
			else:
				row.append(0)  # nikt nie bije wież :(
		row.append(entry[2])
		data.append(row)
	return data


# Pobieramy info o pro grach, o konkretnych meczach i tworzymy dwójkę gracza i jego osiągnięć w meczu
if __name__ == "__main__":
	data = get_from_file()
	# random.shuffle(data)
	train_data = data[:-10]
	test_data = data[-10:]
	classify(train_data, test_data)
