
# 6 kyu Highest Scoring Word


def high(x):
    worth = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,
        'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
        'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 
        'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
    totals = []
    words = x.split(' ')
    total_words = len(words)
    for y in range (0,total_words):

          total = 0
          for char in words[y]:
              if char in worth:
                  total += worth[char]
          totals.append(total)

    for a in range (0,total_words):
      if totals[a] == max(totals):
        return(words[a])