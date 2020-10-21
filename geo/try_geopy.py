from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Albert")
locations = geolocator.geocode(
    "arızlı", language="en")

for location in locations:
    pass
    # print(location.latitude)

reversed_locations = geolocator.reverse("40,29", exactly_one=False)
for reversed_location in reversed_locations:
    print(reversed_location.address)
    print(type(str(reversed_location.address)))

