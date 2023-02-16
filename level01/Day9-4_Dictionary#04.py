travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(visit_country,visit_count,visit_cities):
    # travel_log.append({"country":visit_country,"visits":visit_count,"cities":visit_cities})
    # return
    new_country = {}
    new_country["country"] = visit_country
    new_country["visits"] = visit_count
    new_country["cities"] = visit_cities
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# travel_log.append({"country":"Russia","visits":2,"cities":["Moscow","Saint Petersburg"]})
add_new_country("Korea",16,["Seoul","Busan","Ulsan","Bundang"])
print(travel_log)

