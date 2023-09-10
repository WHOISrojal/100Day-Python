# Using Function to add items into the dictionary in list
travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lillie"],
        "visits": 12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg"],
        "visits": 5
    }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"]= cities_visited
    new_country["visits"]= times_visited
    travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)
print(travel_log)