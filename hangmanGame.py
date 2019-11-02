MAX_TRIES = 6
HANGMAN_PHOTOS = {
'picture 1':
 """    x-------x"""

,'picture 2':
 """    x-------x
    |
    |
    |
    |
    |"""

,'picture 3':
 """    x-------x
    |       |
    |       0
    |
    |
    |"""

,'picture 4':
 """    x-------x
    |       |
    |       0
    |       |
    |
    |"""

,'picture 5':
 """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""

,'picture 6':
 """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""

,'picture 7':
 """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""
}

def print_opening_page():
	
	"""
	function will print opening page.
	:param: 
	:type: 
	:return: None
	:rtype: 
	"""
	
	print("""
    _    _                                         
   | |  | |                                        
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/""")
	print("You have " + str(MAX_TRIES) + " strikes")
	
	return None

def print_hangman(num_of_tries):
	
	"""
	function will an int - num_of_tries and will print the right photo according to num_of_tries value.
	:param num_of_tries: number of tries the user has used
	:num_of_tries type: int
	:return: None
	:rtype:
	"""
	
	if num_of_tries == 1:
		print (HANGMAN_PHOTOS['picture 1'])
	if num_of_tries == 2:
		print (HANGMAN_PHOTOS['picture 2'])
	if num_of_tries == 3:
		print (HANGMAN_PHOTOS['picture 3'])
	if num_of_tries == 4:
		print (HANGMAN_PHOTOS['picture 4'])
	if num_of_tries == 5:
		print (HANGMAN_PHOTOS['picture 5'])
	if num_of_tries == 6:
		print (HANGMAN_PHOTOS['picture 6'])
	if num_of_tries == 7:
		print (HANGMAN_PHOTOS['picture 7'])
	
	return None

def choose_word(file_path, index):
	
	"""
	function will get a string and a number and return chosen word.
	:param file_path: a file path
	:param index: an index for word
	:type file_path: string
	:type index: int
	:return: chosen_word
	:rtype: string
	"""
	
	with open(file_path) as words:
		words = words.read()
	words = words.split('\n')
	if len(words) == 1:
		chosen_word = words[0]
	elif index > len(words):
		chosen_word = words[index % len(words) - 1]
	else:
		chosen_word = words[index - 1]
	
	return chosen_word

def show_hidden_word(secret_word, old_letters_guessed, letter_guessed):
	
	"""
	function will get a word, a string and a letter and return a string with the correct letters that the player guessed.
	:param secret_word: word to guess
	:param old_letters_guessed: list of guessed letters
	:param letter_guessed: last guessed letter
	:secret_word type: string
	:old_letters_guessed type: list
	:letter_guessed type: string
	:return: my_str
	:rtype: string
	"""
	
	flag = 0
	length = len(secret_word)
	length1 = len(old_letters_guessed)
	if old_letters_guessed == []:
		my_str = '_ ' * length
		my_str = my_str[0:length * 2 - 1]
		return my_str
	for x in range(length):
		if letter_guessed == secret_word[x]:
			flag += 1
	if flag >= 1:
		my_str = '_' * length
		for x in range(length):
			for y in range(length1):
				if old_letters_guessed[y] == secret_word[x]:
					l = list(my_str)
					l[x] = old_letters_guessed[y]
					my_str = ''.join(l)			
		my_str = ' '.join(l)
		return my_str
	else:
		print(':(')
		return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	
	"""
	function will check if the input is valid, return True if valid and False
    if else. In addition, function will update old_letters_guessed list if possible and return True if possible and False if else.	
	:param letter_guessed: a letter that the user will guess
	:param old_letters_guessed: a list of letters the user had already guessed
	:letter_guessed type: string
	:old_letters_guessed type: list
	:return: flag1 - True or False (validity of input)
	:rtype: boolean 
	"""
	
	flag = False
	length = len(letter_guessed)
	
	if length == 1:
			if (letter_guessed >= 'a' and letter_guessed <= 'z') or (letter_guessed >= 'A' and letter_guessed <= 'Z'):
					flag = True
	length1 = len(old_letters_guessed)
	if length1 >= 1:
		for x in range(length1):
			old_letters_guessed[x] = old_letters_guessed[x].lower()
	if (flag == True) and (old_letters_guessed.count(letter_guessed.lower()) == False):
		old_letters_guessed.append(letter_guessed)
		flag1 = True
	else:
		print('X')
		if len(old_letters_guessed) > 1:
			old_letters_guessed.sort()
			seperator = ' -> '
			print (seperator.join(old_letters_guessed))
		flag1 = False
	
	return flag1, old_letters_guessed

def check_win(secret_word, old_letters_guessed):
	
	"""
	function will get a word and a string and return True if the user guessed the word and False if else.
	:param secret_word: word to guess
	:param old_letters_guessed: list of guessed letters
	:secret_word type: string
	:old_letters_guessed type: list
	:return: result
	:rtype: boolean
	"""
	
	flag = 0
	length = len(secret_word)
	length1 = len(old_letters_guessed)
	for x in range(length):
		for y in range(length1):
			if old_letters_guessed[y] == secret_word[x]:
				flag += 1
	if flag == length:
		result = True
	else:
		result = False
	
	return result

def main(): 
	
	letter_guessed = ''
	num_of_tries = 1
	old_letters_guessed = []
	print_opening_page()
	file_path = "C:/Users/user/Documents/hangmanWords.txt"
	wrongInput = True
	
	while wrongInput:
		try:
			index = int(input("Enter index: "))
			wrongInput = False
		except:
			print("Enter numbers only.\n")
		
	secret_word = choose_word(file_path, index)
	print("\nLet's start!\n")
	print_hangman(num_of_tries)
	my_str = show_hidden_word(secret_word, old_letters_guessed, letter_guessed)
	print(my_str)
	
	while (num_of_tries < MAX_TRIES + 1):
		letter_guessed = input("\nGuess a letter: ")
		letter_guessed = letter_guessed.lower()
		valid, old_letters_guessed = try_update_letter_guessed(letter_guessed, old_letters_guessed)
		if valid == True:
			check = show_hidden_word(secret_word, old_letters_guessed, letter_guessed)
			if check == False:
				num_of_tries += 1
				print_hangman(num_of_tries)
				print("\n%s" % my_str)
			else:
				my_str = show_hidden_word(secret_word, old_letters_guessed, letter_guessed)
				print(my_str)
		result = check_win(secret_word, old_letters_guessed)
		if result == True:
			print('WIN')
			num_of_tries = 7
	if result == False:
		print(secret_word)
		print('LOSE')

if __name__ == "__main__": 
	main() 