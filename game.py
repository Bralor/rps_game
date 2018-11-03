import random

"""
#--------------------------------------------------------------------------
1. Nacist vstup                       (negativni fce)
2. Kontrola vstupu od usr             (korektni fce)
3. Vzit inpt od AI (import random)    (negat.f.)
4. Vypsat                             (negat.f.)
5. Vyhodnotit vysledek                (korektni fce)
6. Vypsat vysledek                    (negat.f.)
#--------------------------------------------------------------------------
"""

def inp_usr(input=input):
	"""Returns index from list."""
	turn = input('Choice: rock, scissors, paper: ')

	while not is_val(turn):
		turn = input('Choice: rock, scissors, paper: ')

	return turn


def is_val(turn):
	"""Evaluate if the first fnc is correct."""

	return turn in ['rock', 'paper', 'scissors'] 


def ai_turn():
	"""Import the turn for AI."""
	return random.choice(['rock', 'paper', 'scissors'])


def evaluate_game(turn, ai):
	"""Eval for results from AI and USER."""

	if turn == ai:
		return 'Tie'

	elif turn == 'rock':
		if ai == 'paper':
			return 'AI'
		else:
			return 'User'

	elif turn == 'paper':
		if ai == 'scissors':
			return 'AI'
		else:
			return 'User'
	  
	else:
		if ai == 'rock':
			return 'AI'
		else:
			return 'User'


def main(input=input):
	usr = inp_usr(input)
	ai = ai_turn()
	game = evaluate_game(usr, ai)

	if game == 'Tie':
		print('It\'s a tie!')
	else:
		print('{} has won'.format(game))

if __name__ == '__main__':
	main()
