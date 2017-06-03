import json
import urllib
import urllib.request


def request_pro_matches(_max_id: int) -> dict:
	url = "https://api.opendota.com/api/proMatches?less_than_match_id={0}".format(_max_id)
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'super happy dosBot')
	pro_players_games = urllib.request.urlopen(req).read()  # gry zagrane o mniejszym id od wpisanego
	data = json.loads(pro_players_games.decode('utf8'))

	print("Wczytano dane o {0} meczach".format(len(data)))
	return data


def get_pro_players() -> list:
	url = "https://api.opendota.com/api/proPlayers"
	pro_players_games = urllib.request.urlopen(url).read().decode('utf8')
	data = json.loads(pro_players_games)
	return data


def get_match_info(_match_id: int) -> dict:
	url_match = "https://api.opendota.com/api/matches/{0}".format(_match_id)
	req = urllib.request.Request(url_match)
	req.add_header('User-Agent', 'super happy dosBot')
	match = urllib.request.urlopen(req).read().decode('utf8')
	return json.loads(match)


def get_player_recent_history(_player_id: int) -> dict:
	url = "https://api.opendota.com/api/players/{0}/recentMatches".format(_player_id)
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'super happy dosBot')
	history = urllib.request.urlopen(req).read().decode('utf8')
	return json.loads(history)
