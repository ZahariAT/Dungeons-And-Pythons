import unittest
from DungeonsAndPythons_TheGame import TheGame
import mock

'''
def yes_or_no():
    answer = input("Do you want to quit? > ")
    if answer == "yes":
        return("Quitter!")
    elif answer == "no":
        return("Awesome!")
    else:
        return("BANG!")


def test_quitting():

    with mock.patch('builtins.input', return_value="yes"):
        assert yes_or_no() == "Quitter!"

    with mock.patch('builtins.input', return_value="no"):
        assert yes_or_no() == "Awesome!"
'''
class testTheGame(unittest.TestCase):
    def test_(self):
        'Hello there'

if __name__=='__main__':
    unittest.main()