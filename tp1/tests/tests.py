import sys
import os
sys.path.append(os.path.abspath('D:\\Code\\alg1\\tp1'))

import main
import string

exp1: string = """ 
Parte 1: 10
Parte 2: 2
Parte 3: 2
"""

exp2: string = """ 
Parte 1: 11
Parte 2: 1 3 4 6 7
Parte 3: 7
""" 

exp3: string = """ 
Parte 1: 4
Parte 2: 1 3 4 6
Parte 3: -1
""" 

BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'

def assertionErrorText(exp: string, act: string) -> string:
    return f"""{BOLD}{GREEN}\nExpected: {RESET}{exp}{BOLD}{RED}\nActual: {RESET}{act}"""

if __name__ == "__main__":
    act1: string = main.main(argv = [".\\tp1\\tests.py", "testCase01.txt"])
    assert exp1 == act1, assertionErrorText(exp1, act1)

    act2: string = main.main(argv = [".\\tp1\\tests.py", "testCase02.txt"])
    assert exp2 == act2, assertionErrorText(exp2, act2)

    act3: string = main.main(argv = [".\\tp1\\tests.py", "testCase03.txt"])
    assert exp3 == act3, assertionErrorText(exp3, act3)

    print(f"{BOLD}{GREEN}All tests passed!{RESET}")
