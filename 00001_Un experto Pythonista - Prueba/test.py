
class Test(unittest.TestCase):

  def test_description_example(self):
    self.assertTrue(fout == 'Hola Bioinformatica!!')
    sys.stdout = saved
    fout.close()
