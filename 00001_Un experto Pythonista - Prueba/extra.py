# redirect sys.stdout to a buffer
import sys, io
stdout = sys.stdout
sys.stdout = io.StringIO()



print(output)