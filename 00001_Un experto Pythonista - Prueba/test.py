import sys
from cStringIO import StringIO

# setup the environment
backup = sys.stdout

# ####
sys.stdout = StringIO()     # capture output
/*...content...*/
output = sys.stdout.getvalue() # release output
# ####
output = output.strip()
sys.stdout.close()  # close the stream 
sys.stdout = backup # restore original stdout

class Test(unittest.TestCase):
  def test_description_example(self):
    print "hola"
    self.assertTrue(output == 'Hola Bioinformatica!!', 'Tu solucion no esta bien. La salida obtenida es {0}'.format(output))
      
