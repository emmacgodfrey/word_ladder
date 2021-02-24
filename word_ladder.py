#!/bin/python3

from copy import copy, deepcopy
from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny',
    'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey',
    'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    with open('words5.dict') as f:
        lines = [line.strip() for line in f]

    stack = []
    stack.append(start_word)
    q = deque()
    q.append(stack)

    while not len(q) == 0:
        current_stack = q.popleft()
        copylines = copy(lines)
        for word in copylines:
            if _adjacent(word, current_stack[-1]):
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                copystack = deepcopy(current_stack)
                copystack.append(word)
                q.append(copystack)
                lines.remove(word)
    return None
    f.close()


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder is None or len(ladder) == 0:
        return False

    if len(ladder) == 1:
        return True

    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False

    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if not len(word1) == len(word2):
        return False

    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count == 1
