#include "../include/assert.hpp"


CPP_UNIT_ASSERT::CPP_UNIT_ASSERT(){
    total_tests = 0;
    failed_tests = 0;
    log_messages = "";
};

CPP_UNIT_ASSERT::~CPP_UNIT_ASSERT(){
    std::cout << "\n|#########################################|"
              << "\n|#|     CPP_UNIT_ASSERT TEST REPORT     |#|"
              << "\n|#########################################|";

    if(log_messages != "") std::cout << log_messages << std::endl;

    std::cout << "\n|#########################################|\n";
    std::cout << "|#|\tFAILED " << failed_tests << " / " << total_tests << " TOTAL";
    std::cout << "\t\t|#|";
    std::cout << "\n|#########################################|\n";
};

void CPP_UNIT_ASSERT::assert_equals(const std::string act, const std::string exp){
    total_tests++;

    if(act != exp){
        failed_tests++;
        log_messages += 
            "\n\n" + std::to_string(total_tests) + " failed test |#| ASSERT_EQUALS\n"
            "EXP: " + exp + " \nACT: " + act;
    }
};
