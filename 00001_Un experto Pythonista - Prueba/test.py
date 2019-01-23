sys.stdout = sys.__stdout__       # Reset redirect. 
    
class Test(unittest.TestCase):
  def test_description_example(self):
    print('Captured', capturedOutput.getvalue())
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
      self.assertTrue(output == 'Hola Bioinformatica!!')
