import json
import urllib.request


def request_pro_matches(_max_id: int) -> dict:
	url = "https://api.opendota.com/api/proMatches?less_than_match_id={0}".format(_max_id)
	pro_players_games = urllib.request.urlopen(url).read()  # gry zagrane o mniejszym id od wpisanego
	data = json.loads(pro_players_games.decode('utf8'))

	print("Wczytano dane o {0} meczach".format(len(data)))
	return data


def get_match_info(_match_id: int) -> dict:
	url_match = "https://api.opendota.com/api/matches/{0}".format(_match_id)
	match = urllib.request.urlopen(url_match).read().decode('utf8')
	return json.loads(match)
