import geocoder

ip = geocoder.ip("169.7.147.0")
print(ip.city)
print(ip.country)
