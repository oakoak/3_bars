import json


def get_seat_count(data):
	return data['properties']['Attributes']['SeatsCount']


def load_data(filepath):
	f = open(filepath, 'r')
	return json.loads(f.read())


		
def get_biggest_bar(data):
	return max(data['features'], key=get_seat_count)


def get_smallest_bar(data):
	return min(data['features'], key=get_seat_count)


def get_closest_bar(data, longitude, latitude):
  	def distance(data):
  		return ((data["geometry"]["coordinates"][0] - longitude)**2 + (data["geometry"]["coordinates"][1] - latitude)**2)**0.5

  	return min(data['features'], key = distance)


if __name__ == '__main__':
	pass
