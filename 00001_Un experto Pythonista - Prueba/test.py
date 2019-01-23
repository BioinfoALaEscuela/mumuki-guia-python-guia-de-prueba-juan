# redirect sys.stdout to a buffer
import sys, io
stdout = sys.stdout
sys.stdout = io.StringIO()

# call module that calls print()
/*...content...*/

# get output and restore sys.stdout
output = sys.stdout.getvalue()
sys.stdout = stdout

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
