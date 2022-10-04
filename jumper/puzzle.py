import random

class Puzzle:

    def __init__(self):

        self._word_list = ['apple', 'banana', 'orange']
        self._word_selected = ''
        self.place = 0

    
    def _select_word(self):
        self._word_selected = self._word_list[random.randint(0, 2)]
        return


    def word_guess(self):
        self._word_guess = ['_ '] * len(self._word_selected)
        print(f'{self._word_guess}')
        return


    def process_guess (self, guess_letter):
        if guess_letter in self._word_selected:
            for i in self._word_selected:
                if i == guess_letter:
                    self._word_guess[self.place] = guess_letter
                else:
                    self._word_guess[self.place] = '_'
                self.place = self.place + 1
            print(f'{self._word_guess}')
            

        else:
            
            print('no letter in name sorry.')

        return
                
                
    def can_keep_guessing(self):
        pass