import sys
import os
sys.path.append(os.path.abspath('D:\\Code\\alg1\\tp1'))

import main
import string

BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'

def assertionErrorText(exp: string, act: string) -> string:
    return f"""{BOLD}{GREEN}\nExpected:\n{RESET}{exp}{BOLD}{RED}\nActual:\n{RESET}{act}\n"""

exp1: string = "Parte 1: 10\nParte 2: 2\nParte 3: 2"
exp2: string = "Parte 1: 11\nParte 2: 1 3 4 6 7\nParte 3: 7"
exp3: string = "Parte 1: 4 \nParte 2: 1 3 4 6 \nParte 3: -1"

tests = [
    (exp1, [".\\tp1\\tests.py", ".\\tests\\testCase01.txt"]),
    (exp2, [".\\tp1\\tests.py", ".\\tests\\testCase02.txt"]),
    (exp3, [".\\tp1\\tests.py", ".\\tests\\testCase03.txt"])
]

errors = []

if __name__ == "__main__":
    for i, (expected, argv) in enumerate(tests, 1):
        try:
            actual = main.main(argv=argv)
            assert expected == actual, assertionErrorText(expected, actual)
        except AssertionError as e:
            errors.append(f"{BOLD}{CYAN}Test {i} failed:{e}{RESET}")

    print(f"{BOLD}{CYAN}"
          f"========================================\n" f"#{WHITE}"
          f"         PY_UNIT_ASSERT REPORT        "     f"{CYAN}#\n"
          f"========================================\n" f"{RESET}")

    if errors:
        for err in errors:
            print(err)
    else:
        print(f"{BOLD}{GREEN}All tests passed!{RESET}")