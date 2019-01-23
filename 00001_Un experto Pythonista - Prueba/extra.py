import StringIO
import sys

capturedOutput = StringIO.StringIO()          # Create StringIO object
sys.stdout = capturedOutput