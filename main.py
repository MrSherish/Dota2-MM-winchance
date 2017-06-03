from itertools import chain

import requests

# Pobieramy info o pro grach, o konkretnych meczach i tworzymy dwójkę gracza i jego osiągnięć w meczu
if __name__ == "__main__":
	max_game_id = int(input("wpisz maksymalne id meczu: "))
	pro_matches = requests.request_pro_matches(max_game_id)
	pro_match_game_data = map(lambda x: requests.get_match_info(x['match_id']), pro_matches)
	pro_players = list(chain.from_iterable(map(lambda x: (x['players']), pro_match_game_data)))
	player_benchmark_list = list()
	for entry in pro_players:
		player_benchmark_list.append((entry['account_id'], entry['benchmarks']))
	print("pobrano {0} statystyk".format((len(player_benchmark_list))))
