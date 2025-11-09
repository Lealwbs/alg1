import time

BOLD = '\033[1m'
RESET = '\033[0m'
GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ORANGE = '\033[93m'
GREY = '\033[90m'

class Test:
    def __init__(self, title: str = "PY_UNIT_ASSERT REPORT") -> None:
        self.results: list[dict] = []
        self.start_time: float = time.time()
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
            f"{BOLD}{GREY}{'ID':<5}{'STATUS':<9}{'DURATION':<11}{'DETAILS'}{RESET}\n"\
            f"{GREY}{'-'*40}{RESET}"


    def print_details(self):
        total_time: float = time.time() - self.start_time
        failed_tests: int = self.tests_amount - self.tests_passed
        print(f"\n{BOLD}{CYAN}Total time: {total_time:.3f} seconds{RESET}")

        if not failed_tests:
            print(f"{BOLD}{GREEN}\nAll {self.tests_amount} tests passed!{RESET}")
            return
        
        print(f"{BOLD}{ORANGE}\n{failed_tests} test(s) failed out of {self.tests_amount}:{RESET}")
        for result in self.results:
            if not result['passed']: 
                print(f"\n{BOLD}Test {result['id']}: {GREY}{result['message']}\n {RESET}{result['error']}")
        
    def error_text(self, exp: str, act: str) -> str:
        return f"{BOLD}{GREEN}EXP:{RESET} {exp}\n"\
               f"{BOLD}{RED} ACT:{RESET} {act}"

    def assert_equals(self, exp, act, msg: str = "") -> None:
        self.tests_amount += 1
        test_id = self.tests_amount
        start_time: float = time.time()

        try:
            assert exp == act, self.error_text(exp, act)
            duration = time.time() - start_time
            status = f"{GREEN}PASSED{RESET}"
            self.tests_passed += 1
            self.results.append({
                "id": test_id,
                "passed": True,
                "message": msg or "OK",
                "error": None,
                "duration": duration
            })
        except AssertionError as e:
            duration = time.time() - start_time
            status = f"{RED}FAILED{RESET}"
            self.results.append({
                "id": test_id,
                "passed": False,
                "message": msg,
                "error": str(e),
                "duration": duration
            })

        print(f"{GREY}#{test_id:<3}{RESET} {status:<10} "
              f"{duration:>9.5f}s   {msg or ''}")




if __name__ == "__main__":
    R = Test()

    R.assert_equals(time.sleep(1), "Hello, World!", "opa")
    R.assert_equals("Foo", "Foao", "Testing string mismatch")
    R.assert_equals(123, 123, "Numeric equality")
    R.assert_equals("opa", "opa", "Another greeting")
    R.assert_equals('123', 123, "Str equality")
    R.assert_equals("test", "test1", "Final test")