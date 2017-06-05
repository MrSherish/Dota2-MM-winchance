from scipy import random
from sklearn import svm

import requests


def classify(_train_data: list, _test_data: list) -> list:
	svc = svm.SVC(kernel='poly', degree=3)
	dota_x = list()
	dota_y = list()
	for _entry in _train_data:
		dota_x.append(_entry[1:-1])
		dota_y.append(_entry[-1])
	svc.fit(X=dota_x, y=dota_y)
	print("uczenie zakończone")
	dota_x = list()
	dota_y = list()
	for _entry in _test_data:
		dota_x.append(_entry[1:-1])
		dota_y.append(_entry[-1])
	predicted = svc.predict(dota_x).tolist()
	print("predicted: " + str(predicted))
	print("ref:" + str(dota_y))
	return predicted


# Pobieramy info o pro grach, o konkretnych meczach i tworzymy dwójkę gracza i jego osiągnięć w meczu
if __name__ == "__main__":
	pro_games = random.choice(requests.request_pro_matches(90000000), 5)
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

	random.shuffle(data)
	train_data = data[:-10]
	test_data = data[-10:]
	classify(train_data, test_data)
