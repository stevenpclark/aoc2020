class Word:
    def __init__(self):
        self.t_new = None
        self.t_old = None

    def speak(self, t):
        self.t_old = self.t_new
        self.t_new = t

    def get_next(self):
        if self.t_old is None:
            return 0
        else:
            return self.t_new - self.t_old

def init_game(inp):
    d = dict()
    t = 1
    for v in inp:
        word = Word()
        d[v] = word
        word.speak(t)
        t += 1

    return d, t, d[inp[-1]]

#inp = [0,3,6]
#inp = [2,1,3]
inp = [1,0,16,5,17,4]

d, t, last_word = init_game(inp)

while t <= 30000000:
    n = last_word.get_next()
    next_word = d.get(n, Word())
    d[n] = next_word
    next_word.speak(t)
    t += 1
    last_word = next_word
print(n)

