import sys
import os
import time
import tp2
sys.path.append(os.path.abspath('D:\\Code\\alg1\\tp2'))

BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
GREY = '\033[90m'

# def assertionErrorText(exp: str, act: str) -> str:
#     return f"""{BOLD}{GREEN}\nExpected:\n{RESET}{exp}{BOLD}{RED}\nActual:\n{RESET}{act}\n"""

def assertionErrorText(exp: str, act: str) -> str:
    return f"{BOLD}{GREEN} EXP:{RESET}\n  {exp}"\
           f"{BOLD}{RED} ACT:{RESET}\n  {act}"

header: str = f"{BOLD}{CYAN}"\
    f"========================================\n" f"#{WHITE}"\
    f"         PY_UNIT_ASSERT REPORT        "     f"{CYAN}#\n"\
    f"========================================\n" f"{RESET}"

tests_path_inp = ".\\tests\\inp_moodle\\"
tests_path_out = ".\\tests\\out_moodle\\"

tests = [ (i, f"{tests_path_inp}in{i:02}.txt", f"{tests_path_out}out{i:02}.txt")
    for i in [1, 2] + list(range(11, 21)) ]

errors = []

if __name__ == "__main__":
    start_time: float = time.time()

    print(header)

    for i, in_file, out_file in tests:
        print(f"{BOLD}{CYAN}Running test {i}/{len(tests)}...{RESET}")
        try:
            actual = tp2.main(argv=["tests.py", in_file])
            with open(out_file, "r") as f:
                expected = f.read()
            assert expected == actual, assertionErrorText(expected, actual)
        except AssertionError as e:
            errors.append(f"{BOLD}{GREY}Test {i} failed:\n{e}{RESET}")

    end_time: float = time.time()
    print(f"\n{BOLD}{CYAN}Total time: {end_time - start_time:.3f} seconds{RESET}")
    print(f"{BOLD}{YELLOW}\n{len(errors)} test(s) failed out of {len(tests)}:{RESET}\n")
  
    if errors:
        for err in errors:
            print(err, "\n")
    else:
        print(f"\n{BOLD}{GREEN}All tests passed!{RESET}")
