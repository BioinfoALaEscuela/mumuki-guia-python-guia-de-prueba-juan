# importo librerías necesarias
import sys
from cStringIO import StringIO 

# guardo el stdout existente para restaurarlo después
backup = sys.stdout

sys.stdout = StringIO()     # capturo el output
/*...content...*/           # esto es la interpolación, acá está el código que el alumno ponga en la solución.

output = sys.stdout.getvalue() # guardo lo que salió en consola, o sea en stdout, en la variable output

output = output.strip()    # acá le sacó caracteres extraños como el \n de nueva línea que se agrega al capturar el stdout
sys.stdout.close()  # cierro la captura
sys.stdout = backup # restauro el stdout original

#Ahora abajo defino el unit test que prueba si esta todo bien o no.
class Test(unittest.TestCase):
  def test_description_example(self):
    self.assertTrue(output == 'Hola Bioinformatica!!', 'Tu solucion no esta bien. La salida obtenida es {0}'.format(output)) #esta línea devuelve True si output es == a 'Hola Bioinformatica!!' y lo que está después de la coma si no.
      
