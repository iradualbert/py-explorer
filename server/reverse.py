import reverse_geocoder as rg

if __name__ == "__main__":
    coordinates = (40.801846, 29.908571)
    results = rg.search(coordinates)
    print(results)
