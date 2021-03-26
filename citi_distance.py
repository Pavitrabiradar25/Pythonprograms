from geopy.geocoders import Nominatim
from geopy import distance

#initialize Nomination API
geolocator = Nominatim(user_agent="geoapiExercises")

citi1 = input('City 1: ')
citi2 = input('Citi 2: ')

print('Output: City 1 and City 2 are',distance.distance(citi1,citi2).km,'apart')