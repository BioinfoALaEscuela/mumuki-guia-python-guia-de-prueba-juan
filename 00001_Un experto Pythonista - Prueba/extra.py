class writer :
    def __init__(self, *writers) :
        self.writers = writers

    def write(self, text) :
        for w in self.writers :
            w.write(text)

import sys

saved = sys.stdout
fout = file('out.log', 'w')
sys.stdout = writer(sys.stdout, fout)

