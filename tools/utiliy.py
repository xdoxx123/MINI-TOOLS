import os
from colorama import Fore,Back
import io
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Error(txt):
    print(f"{Fore.RED}[ERROR] {txt}")



def capture_printed_output(func, *args, **kwargs):
  
    
    original_stdout = sys.stdout
    
   
    captured_output = io.StringIO()
    
    
    sys.stdout = captured_output
    
    try:
       
        func(*args, **kwargs)
    finally:
   
        sys.stdout = original_stdout

   
    return captured_output.getvalue()
