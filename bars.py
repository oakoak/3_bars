import json


def load_data(filepath):
	f = open(filepath, 'r')
	return json.loads(f.read())


		
def get_biggest_bar(bars_json):
	get_seat_count = lambda bar: bar['properties']['Attributes']['SeatsCount']
	return max(bars_json['features'], key=get_seat_count)


def get_smallest_bar(bars_json):
	get_seat_count = lambda bar: bar['properties']['Attributes']['SeatsCount']
	return min(bars_json['features'], key=get_seat_count)


def get_closest_bar(bars_json, longitude, latitude):
	def distance(bar):
		return ((bar["geometry"]["coordinates"][0] - longitude)**2 +
				(bar["geometry"]["coordinates"][1] - latitude)**2)**0.5
	return min(bars_json['features'], key = distance)


if __name__ == '__main__':
	pass
