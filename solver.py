import sys
from enum import Enum, auto
from typing import List
from random import choice 

class LetterResult(Enum):
    NOT_IN_WORD = auto()
    WRONG_POSITION = auto()
    RIGHT_POSITION = auto()

def score_guess(guessed_word: str, target_word: str) -> List[LetterResult]:
    result = []
    for index, letter in enumerate(guessed_word):
        if target_word[index] == letter:
            result.append(LetterResult.RIGHT_POSITION)
        elif letter in target_word:
            result.append(LetterResult.WRONG_POSITION)
        else:
            result.append(LetterResult.NOT_IN_WORD)
    return result

def get_filtered_corpus(guessed_word: str, score: List[LetterResult], corpus: List[str]) -> List[str]:
    filtered_corpus = []
    for candidate in corpus:
        if candidate == guessed_word:
            continue
        should_include = True
        for index in range(len(guessed_word)):
            if score[index] == LetterResult.RIGHT_POSITION and candidate[index] != guessed_word[index]:
                should_include = False
                break
            elif score[index] == LetterResult.WRONG_POSITION and guessed_word[index] not in candidate:
                should_include = False
                break
            elif score[index] == LetterResult.NOT_IN_WORD and guessed_word[index] in candidate:
                should_include = False
                break
        if should_include:
            filtered_corpus.append(candidate)
    return filtered_corpus

def solver_loop(corpus: List[str], target_word: str) -> List[str]:
    guesses = []
    filtered_corpus = corpus.copy()
    guessed_word = None
    while guessed_word != target_word:
        guessed_word = choice(filtered_corpus)
        guesses.append(guessed_word)
        score = score_guess(guessed_word, target_word)
        filtered_corpus = get_filtered_corpus(guessed_word, score, filtered_corpus)
    return guesses

def solve_wordle(corpus_filename: str, target_word: str) -> List[str]:
    corpus = []
    with open(corpus_filename, 'r') as corpus_file:
        while(line := corpus_file.readline().rstrip()):
            corpus.append(line)
    guesses = solver_loop(corpus, target_word)
    for guess in guesses:
        print(guess)
    print(len(guesses))

if __name__ == "__main__":
    corpus_filename = sys.argv[1]
    target_word = sys.argv[2]
    solve_wordle(corpus_filename, target_word)