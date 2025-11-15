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
ORANGE = '\033[93m'
GREY = '\033[90m'

class TP2Test:
    def __init__(self, title: str = "TP2 TEST REPORT") -> None:
        self.results: list[dict] = []
        self.start_time: float = time.time()
        self.last_time: float = self.start_time
        self.tests_amount: int = 0
        self.tests_passed: int = 0
        print(self.header(title))

    def __del__(self) -> None:
        self.print_details()

    def header(self, title) -> str:
        return \
            f"{BOLD}{CYAN}"\
            f"========================================\n"\
            f"#{WHITE}{title:^38}{CYAN}#\n"\
            f"========================================{RESET}\n\n"\
            f"{BOLD}{GREY}{'ID':<5}{'STATUS':<9}{'DURATION':>7}{'DETAILS':>10}{RESET}\n"\
            f"{GREY}{'-'*40}{RESET}"

    def print_details(self):
        total_time: float = time.time() - self.start_time
        failed_tests: int = self.tests_amount - self.tests_passed
        print(f"\n{BOLD}{CYAN}Total time: {total_time:.3f} seconds{RESET}")

        if not failed_tests:
            print(f"{BOLD}{GREEN}\nAll {self.tests_amount} tests passed!{RESET}")
            return
        
        print(f"{BOLD}{ORANGE}\n{failed_tests} test(s) failed out of {self.tests_amount}:{RESET}\n")
        for result in self.results:
            if not result['passed']: 
                print(f"{BOLD}{GREY}Test {result['id']}: {RESET}{GREY}{result['message']}{RESET}")
                print(f"{result['error']}")
        
    def error_text(self, exp: str, act: str) -> str:
        return f"{BOLD}{GREEN}EXP:{RESET}\n{exp}"\
               f"{BOLD}{RED}ACT:{RESET}\n{act}"

    def assert_equals(self, exp, act, msg: str = "") -> None:
        self.tests_amount += 1
        current_time = time.time()
        duration = current_time - self.last_time
        self.last_time = current_time

        try:
            assert exp == act, self.error_text(exp, act)
            status = f"{GREEN}PASSED{RESET}"
            self.tests_passed += 1
            self.results.append({
                "id": self.tests_amount,
                "passed": True,
                "message": msg or "OK",
                "error": None,
                "duration": duration
            })
        except AssertionError as e:
            status = f"{RED}FAILED{RESET}"
            self.results.append({
                "id": self.tests_amount,
                "passed": False,
                "message": msg,
                "error": str(e),
                "duration": duration
            })

        print(f"{GREY}#{self.tests_amount:<3}{RESET} {status:<10} "
              f"{duration*1000:>8.0f}ms   {msg or ''}")


if __name__ == "__main__":
    tests_path_inp = ".\\tests\\inp_moodle\\"
    tests_path_out = ".\\tests\\out_moodle\\"

    tests = [(i, f"{tests_path_inp}in{i:02}.txt", f"{tests_path_out}out{i:02}.txt")
        for i in [1, 2] + list(range(11, 21))]

    T = TP2Test()

    for i, in_file, out_file in tests:
        actual = tp2.main(argv=["tests.py", in_file])
        with open(out_file, "r") as f:
            expected = f.read()
        
        T.assert_equals(expected, actual, f"Test {i:02}")