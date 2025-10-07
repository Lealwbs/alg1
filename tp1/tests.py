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


tests_path = ".\\tests\\"
tests = [ (i, f"{tests_path}in{i:02}.txt", f"{tests_path}out{i:02}.txt")
    for i in range(1, 14) ]

errors = []

if __name__ == "__main__":
    for i, in_file, out_file in tests:
        print(f"{BOLD}{CYAN}Running test {i}/{len(tests)}...{RESET}")
        try:
            actual = main.main(argv=["tests.py", in_file])
            with open(out_file, "r") as f:
                expected = f.read()
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