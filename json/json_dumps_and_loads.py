import json                                         # Import the JSON library
food = [ "Taco Bell", "Shake Shack", "Chipotle" ]   # Make a list of fast food chains
# print( type( food ) )                             # <class 'list'>
jsondumps = json.dumps( food )
print( type( jsondumps ) ) # <class 'str'>
print( jsondumps )
print()                                             # пропуск строки
jsonloads = json.loads( jsondumps )
print( type( jsonloads ) ) # <class 'str'>
print( jsonloads )
print()
dict = { "Subway": 24722, "McDonals": 14098, "Starbucks": 10821, "Pizza Hut": 7600 }
# print( type( dict ) )                             # <class 'dict'> 
jsondumps = json.dumps( dict )
print( type( jsondumps ) ) # <class 'str'>
print( jsondumps )
print()                                             # пропуск строки
jsonloads = json.loads( jsondumps )
print( type( jsonloads ) ) # <class 'str'>
print( jsonloads )


'''
# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
fast_food_franchise_2 = json.loads(fast_food_franchise_string)
'''