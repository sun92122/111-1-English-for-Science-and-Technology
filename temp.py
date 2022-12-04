try:
    with open("pi_10M.txt") as f:
        pi = f.read()
except:
    print('err')

pi = pi[2:].replace('\n', '').replace(' ', '')\
           .replace('2', '0').replace('6', '0')\
           .replace('3', '1').replace('7', '1')\
           .replace('4', '0').replace('8', '0')\
           .replace('5', '1').replace('9', '1')

with open('pi_10M', 'r+') as f:
    f.write(pi)
