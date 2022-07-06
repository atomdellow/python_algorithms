# Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant 
# sound is transposed to the end of the word and an ay is affixed 
# (Ex.: "banana" would yield anana-bay). 
# Read Wikipedia for more information on rules.

def main():
        lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
        sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
        sentence = sentence.split()
        for k in range(len(sentence)):
                i = sentence[k]
                if i[0] in ['a', 'e', 'i', 'o', 'u']:
                        sentence[k] = i+'ay'
                elif t(i) in lst:
                        sentence[k] = i[2:]+i[:2]+'ay'
                elif i.isalpha() == False:
                        sentence[k] = i
                else:
                        sentence[k] = i[1:]+i[0]+'ay'
        return ' '.join(sentence)

def t(str):
        return str[0]+str[1]

if __name__ == "__main__":
        x = main()
        print(x)
