#!/python/python3.4/bin/python3

## Function: pow, return a number to a power
#  Parameters: base, power
#   base: base number to pow
#   power: number of pow
def pow(base, power):
    result = 1
    while(power > 0):
        power-=1
        result = result * base
    
    return result


if __name__ == '__main__':
   print("For next level, go to http://www.pythonchallenge.com/pc/def/%s.html" % pow(2, 38))
