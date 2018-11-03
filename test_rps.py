import game
#import pytest
import subprocess
import sys

def test_is_rock_valid():
	"""Muze byt ret. 'rock' jako input."""

	assert game.is_val('rock') is True # muze byt jenom 'True', vsechny True stejne ID i False


def test_is_scissors_valid():
	assert game.is_val('scissors') is True


def test_is_paper_valid():
	assert game.is_val('paper') is True


def test_is_lizard_valid():
	assert game.is_val('lizard') is False


def test_ai_turn_is_valid():
	for _ in range(2000):
		turn = game.ai_turn()
		assert game.is_val(turn)


def test_ai_playes_randomly():
	"""Snazim se dostat predpoklad pro nahodne tahy AIs."""

	played = [game.ai_turn() for _ in range(5000)]

	rocks = played.count('rock')
	papers = played.count('paper')
	scissors = played.count('scissors')

	print('Rocks: ', rocks,'\nPaper: ', papers,'\nScissors: ', scissors)

	assert played.count('rock') > 200
	assert played.count('paper') > 200
	assert played.count('scissors') > 200


def test_if_paper_beats_rock():
	"""
	Potrebuji otestovat, zda dostanu spravny result pro vitezstvi
	u "paper" vs. "rock".
	"""
	result = game.evaluate_game('paper', 'rock')
	assert result == 'User'


def input_fake_rock(prompt):
	"""Simuluji chovani built-in fce input()."""

	print(prompt)
	return 'rock'


# @pytest.fixture # tvorba vlastni fixtury potrebuje importovat pytest
# def fake_inp_rock(monkeypatch):
# 	monkeypatch.setattr('builtins.input', input_fake_rock)
	

def test_full_game(capsys):
	"""Vezmi input() a vloz do nej fci "input_fake_rock()"."""
		
	game.main(input=input_fake_rock) # implementuji fixture
	catch = capsys.readouterr() # precti stdin a stdout
	
	# kontroluj obsah stdout s input() textem
	assert 'Choice: rock, scissors, paper: ' in catch.out


def test_wrong_turn_results_in_inf_loop():
	"""
	Se subprocesem overime druhy vstup. Spustim python3.5 a vlozim vstup, 
	ktery kontroluji.

	Prvne vlozim "doggie", zopakuje se input() a vlozim "rock".
	"""
	
	# chceme vystup v citelny podobe pro PIPE
	cp = subprocess.run([sys.executable, 'game.py'],
						# misto encoding, kvuli Python3.5, pouziju univ_new
						universal_newlines=True,
						stdout=subprocess.PIPE,
						input='doggie\nrock\n',
						check=True)

	assert cp.stdout.count('Choice: rock, scissors, paper: ') == 2 # 2x True value
