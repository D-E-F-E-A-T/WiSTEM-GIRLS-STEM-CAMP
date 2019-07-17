from geopy import distance

accra = (5.6037, 0.1870)
kumasi = (6.6666, 1.6163)

distance = distance.distance(accra, kumasi).kilometers

print (str(distance) + " km")