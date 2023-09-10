## Nesting ##

capitals = {"France" : "Paris",
             "Germany" : "Berlin"}

# Nesting a list in dictionary
travel_log = {"France" : ["Paris", "Lillie", "Dijon"], 
              "Germany" : ["Berlin", "Ham", "Stuttgart"]}

# Nesting dictionary in a dictionary
travel_log = {"France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12}, 
"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}}
print(travel_log) 

# Nesting dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lillie"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg"],
        "total_visits": 5
    }
]
print(travel_log)