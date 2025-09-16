#include "assert.hpp"
#include <iostream>

int CPP_UNIT_ASSERT::assert_equals(const string act, const string exp){
    if(strcmp(act, exp) == 0){
        std::cout << "CERTO" << std::endl;
        return 0;
    } else {
        std::cout << "ERRADO" << std::endl;
        return 1;
    }
}