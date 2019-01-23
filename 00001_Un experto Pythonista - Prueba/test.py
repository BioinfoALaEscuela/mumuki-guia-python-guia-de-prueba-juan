# importo librerias necesarias
import sys
from cStringIO import StringIO 

# guardo el stdout existente para restaurarlo despues
backup = sys.stdout

sys.stdout = StringIO()     # capturo el output
/*...content...*/           # esto es la interpolacion, aca está el codigo que el alumno ponga en la solucion.

output = sys.stdout.getvalue() # guardo lo que salio en consola, o sea en stdout, en la variable output

output = output.strip()    # aca le saco caracteres extranos como el \n de nueva linea que se agrega al capturar el stdout
sys.stdout.close()  # cierro la captura
sys.stdout = backup # restauro el stdout original

#Ahora abajo defino el unit test que prueba si esta todo bien o no.
class Test(unittest.TestCase):
  def test_description_example(self):
    self.assertTrue(output == 'Hola Bioinformatica!!', 'Tu solucion no esta bien. La salida obtenida es {0}'.format(output)) #esta linea devuelve True si output es == a 'Hola Bioinformatica!!' y lo que esta despues de la coma si no.
      
