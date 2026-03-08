def break_words(sentence):
    words = sentence.split()
    return words

def sort_words(words):
    sortt = sorted(words)
    return sortt

def print_first_and_last_words(words):
    first_word = words[0]
    last_word = words[-1]
    return first_word, last_word

def words_stats(words, sentence):
    number_of_words = len(words)
    number_of_letters = 0
    for u in words:
        number_of_letters += len(u)
    return number_of_letters, number_of_words


def main():
    sentence = input("Enter a sentence: ")
    words = break_words(sentence)
    sortt = sort_words(words)
    first_word, last_word = print_first_and_last_words(words)
    number_of_letters, number_of_words = words_stats(words, sentence)
    print("Words :", words)
    print("Sortted words :", sortt)
    print("First and last word :", first_word,"...",  last_word)
    print("Word count :", number_of_words, " , Characters count: ", number_of_letters)

main()

