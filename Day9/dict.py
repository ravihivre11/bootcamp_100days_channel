programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",    
    "Loop" : "The action of doing something over and over again."
}
print(programming_dictionary["Loop"])
print(type(programming_dictionary))

programming_dictionary["Loop"] = "hello ravi"

print(programming_dictionary["Loop"])

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary)


travel_log = {
    "India": ["mumbai", "delhi", "bangalore"],
    "Italy": ["rome", "venice", "florence"],
}

print(travel_log["India"][0])

list = [1,2,[2,3]]
print(list[2][1])

travel_data = {
    "India": {
        "cities_visited": ["mumbai", "delhi", "bangalore"],
        "total_visits": 3
    },
    "Italy": {
        "cities_visited": ["rome", "venice", "florence"],
        "total_visits": 3
    },
}

print(travel_data["India"]["cities_visited"][2])