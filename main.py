import random

import requests

# Pobieramy info o pro grach, o konkretnych meczach i tworzymy dwójkę gracza i jego osiągnięć w meczu
if __name__ == "__main__":
	pro_games = random.sample(requests.request_pro_matches(90000000), 5)
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

	print("pobrano {0} wierszy".format((len(data))))
