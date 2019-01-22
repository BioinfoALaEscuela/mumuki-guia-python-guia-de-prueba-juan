
class Test(unittest.TestCase):

  def test_description_example(self):
    # get output and restore sys.stdout
    output = sys.stdout.getvalue()
    sys.stdout = stdout
    print(output)
    self.assertTrue(output == 'Hola Bioinformatica!!')
