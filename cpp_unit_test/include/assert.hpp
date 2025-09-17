#ifndef ASSERT_HPP
#define ASSERT_HPP

#include <string>
#include <iostream>

class CPP_UNIT_ASSERT {
    private: 
        int total_tests;
        int failed_tests;

        std::string log_messages;
    
    public:
        CPP_UNIT_ASSERT();
        ~CPP_UNIT_ASSERT();
        
        void assert_equals(const std::string act, const std::string exp);
};


#endif