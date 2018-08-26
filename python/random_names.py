import random
import re
import sys

names = ["oliver", "gwendolyn", "callum", "evangeline", "everett", "cora", "henry", "evelina", "landon", "zoey", "elijah", "jane", "felix", "aria", "hudson", "autumn", "levi", "grace", "nathaniel", "amelia", "alaric", "caroline", "finn", "emilia", "grayson", "julia", "abel", "margaret", "arthur", "mila", "caspian", "nadia", "gavin", "sophia", "lachlan", "abrielle", "lorcan", "aerilyn", "owen", "amara", "holden", "aurora", "jonah", "celeste", "oscar", "clara", "august", "cordelia", "daniel", "ella", "declan", "felicity", "silas", "freya", "bryson", "kira", "cian", "lucy", "eli", "mae", "emmett", "melody", "hendrix", "olivia", "jedidiah", "charlotte", "liam", "juliet", "lucas", "maeve", "miles", "naomi", "weston", "violet", "caleb", "abigail", "edison", "eliza", "elian", "lana", "griffin", "scarlett", "judson", "vivian", "leo", "abilene", "milo", "adalynn", "nico", "adriana", "roman", "alaina", "theo", "alexandria", "atlas", "aliza", "elias", "amalie", "isaac", "amira"]

#Pick a random name, and get the first letter of that. Add it to name
#Then, pick a random name, search through it for the last letter in name, and add the next 1-3 letters. If it's blankspace and the word is longer than 5 letters, end.

#When running, send a number as an argument to get that many names without the y/n prompt box

def rand_name_from_list():
		return names[random.randint(0, len(names)-1)]

def random_name(): 
	name = "" #the name to be returned
	_current_name = "" #the real name currently being processed
	_current_index = 0 #the index of the first match
	min_name_length = 6 
	max_name_length = 12
	quit = False
	strikes = 0 
	max_strikes = 3
	
	name = rand_name_from_list()[0]

	while not quit:
		_current_name = rand_name_from_list() #sets _current_name
		_current_index = _current_name.find(name[-1]) #finds index of the last letter of name
		if _current_index == -1: #if there isn't that letter
			strikes += 1
			if len(name) >= min_name_length and strikes > max_strikes:
				quit = True
		else: 
			for x in range(random.randint(1, 3)):
				if _current_index + x >= len(_current_name): #if you reached the end
					strikes += 1
					if len(name) >= min_name_length and strikes > max_strikes: #if it's not too short and you have enough strikes
						quit = True
					break #in any case, stop the loop
				else:
					name += _current_name[_current_index + x] #else add one letter
					
		if len(name) >= max_name_length:
			quit = True
		name = re.sub(r'([a-z])\1+', r'\1', name) #regex magic that removes double letters
	
	return(name.capitalize())
	
if len(sys.argv) > 1:
	for x in range(0, int(sys.argv[1])):
		print(random_name())
else:
	quit = False
	while not quit:
		print(random_name())
		if not re.search(r'[y|yes]', input("Another name? [y/n] ")):
			quit = True




