def encode(incoming):
    """Accepts a sentence and returns a sentence with encrypted words"""
    words = []
    incoming_list = incoming.split()
    for word in incoming_list:
        if len(word) > 2:
            if word[-1].isalpha() == False:
                new_word = f'{word[0] + word[3:-1] + word[1:3]}'[::-1] + word[-1]
                words.append(new_word)
            else:
                new_word = f'{word[0] + word[3:] + word[1:3]}'[::-1]
                words.append(new_word)
        else:
            word = word[::-1]
            words.append(word)
    result = ' '.join(words)
    return result

def decode(incoming):
    """Accepts an encrypted sentence and decrypts it"""
    words = []
    incoming_list = incoming.split()
    for word in incoming_list:
        if len(word) > 2:
            if word[-1].isalpha() != True:
                word = word[:-1][::-1] + word[-1]
                words.append(word[0] + word[-3:-1] + word[1: -3] + word[-1])
            else:
                word = word[::-1]
                words.append(word[0] + word[-2:] + word[1: -2])
        else:
            word = word[::-1]
            words.append(word)
    result = ' '.join(words)
    return result

def word_encode(incoming):
    """Takes a word, and shuffles letters in even/odd order"""
    index = 0
    even = []
    odd = []
    for letter in incoming:
        if index % 2 == 0:
            even.append(letter)
        else:
            odd.append(letter)
        index += 1
    return ''.join(even + odd)

def word_decode(incoming):
    """Accepts a shuffled word and restores letter order"""
    middle = int(len(incoming) / 2)
    result = []
    x = 0
    if len(incoming) % 2 == 0:
        odd = incoming[middle:]
        even = incoming[:middle]
    else:
        odd = incoming[1 + middle:]
        even = incoming[:1 + middle]
    for _ in range(0,len(odd)):
        result.append(even[x])
        result.append(odd[x])
        x += 1
    if len(even) > len(odd):
        result.append(even[-1])
    return ''.join(result)