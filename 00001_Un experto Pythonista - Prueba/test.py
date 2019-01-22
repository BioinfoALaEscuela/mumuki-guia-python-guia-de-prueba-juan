class Test(unittest.TestCase):
  def test_description_example(self):
    try:
      output
    except NameError:
      output_exists = False
      
    if output_exists:
      print(output)
      self.assertTrue(output == 'Hola Bioinformatica!!')
