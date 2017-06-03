import random

import requests

# Pobieramy info o pro grach, o konkretnych meczach i tworzymy dwójkę gracza i jego osiągnięć w meczu
if __name__ == "__main__":
	pro_players = random.sample(requests.get_pro_players(), 50)
	player_recent_matches = list(map(lambda x: requests.get_player_recent_history(x['account_id']), pro_players))

	print("pobrano {0} statystyk".format((len(player_recent_matches))))
