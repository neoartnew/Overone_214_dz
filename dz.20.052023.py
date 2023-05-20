class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print("Alphabet:", self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26
    def __init__(self):
        super().__init__("En", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        return "My husband bought me this bag"

# Тесты
eng_alphabet = EngAlphabet()
eng_alphabet.print()
print("Number of letters:", eng_alphabet.letters_num())
print("Is 'F' an English letter?", eng_alphabet.is_en_letter('F'))
print("Is 'Щ' an English letter?", eng_alphabet.is_en_letter('Щ'))
print("Example sentence:", EngAlphabet.example())
