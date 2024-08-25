# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
# RGB To Hex Conversion
def rgb(r, g, b):
    max_range = lambda a: 0 if a < 0 else 255 if a > 255 else a
    return '{:02X}{:02X}{:02X}'.format(*list(map(max_range, [r, g, b])))

# Clever
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))