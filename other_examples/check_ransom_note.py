#!/user/bin/env python

def ransom_note(magazine, ransom):
    answer = True
    if (len(ransom) or len(magazine)) < 1 or (
        len(ransom) or len(magazine)) > 30000:
        answer = False
    else:
        for ea_word in ransom:
            if len(ea_word) > 5 or len(ea_word) < 1:
                answer = False
            elif not isAlpha(ea_word):
                answer = False
            elif ea_word not in magazine:
                answer = False
    return answer


def isAlpha(word):
    alpha = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'
    for ea in word:
        if ea not in alpha:
            return False
        else:
            return True

if __name__ == '__main__':
    magazine = 'test me one more test'
    ransom = 'me one more test'
    a_ransom = []
    a_ransom = ransom.split(' ')
    a_magazine = []
    a_magazine = magazine.split(' ')
    answer = ransom_note(magazine=a_magazine, ransom=a_ransom)
    if (answer):
        print "Yes"
    else:
        print "No"
