import sys
import os
import time
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

header: string = \
    f"{BOLD}{CYAN}"\
    f"========================================\n" f"#{WHITE}"\
    f"         PY_UNIT_ASSERT REPORT        "     f"{CYAN}#\n"\
    f"========================================\n" f"{RESET}"

tests_path = ".\\tests\\"

tests = [ (i, f"{tests_path}in{i:02}.txt", f"{tests_path}out{i:02}.txt")
    for i in range(1, 14) ]

errors = []

if __name__ == "__main__":
    start_time: float = time.time()

    print(header)

    for i, in_file, out_file in tests:
        print(f"{BOLD}{CYAN}Running test {i}/{len(tests)}...{RESET}")
        try:
            actual = main.main(argv=["tests.py", in_file])
            with open(out_file, "r") as f:
                expected = f.read()
            assert expected == actual, assertionErrorText(expected, actual)
        except AssertionError as e:
            errors.append(f"{BOLD}{CYAN}Test {i} failed:{e}{RESET}")

    if errors:
        for err in errors:
            print(err)
    else:
        print(f"\n{BOLD}{GREEN}All tests passed!{RESET}")

    end_time: float = time.time()
    print(f"{BOLD}{CYAN}Total time: {end_time - start_time:.3f} seconds{RESET}")