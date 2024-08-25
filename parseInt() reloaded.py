# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/python
# parseInt() reloaded

def parse_int(string):

    dict_word_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
        'eleven': '11',
        'twelve': '12',
        'thirteen': '13',
        'fourteen': '14',
        'fifteen': '15',
        'sixteen': '16',
        'seventeen': '17',
        'eighteen': '18',
        'nineteen': '19',
        'twenty': '20',
        'forty': '4',
        'fifty': '5',
        'sixty': '6',
        'seventy': '7',
        'eighty': '8',
        'ninety': '9'
        #'thousand': '000'
        #'hundred': '00'
    }

    line_ = ''
    result = []
    string = string.lower()
    if '-' in string:
        line_ = (string.split('-'))
    else:
        line_ = [string]
    for i in line_:
        result += (i.split())
    num_ = ''
    for word in result:
        num_ += (dict_word_num.get(word, ''))
    return int(num_)

print(parse_int('Five hundred thousand three hundred')) # 500300
print(parse_int('seven hundred eighty-three thousand nine hundred and nineteen'))
print(parse_int('seven nine')) # 783919
