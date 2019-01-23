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
    try:
      output
      output_exists = True
      print('output exists!')
      print('output is:',output)
    except NameError:
      output_exists = False
      print('output does not exist!')
    if output_exists:
      print(output)
    self.assertTrue(1 == 2)
