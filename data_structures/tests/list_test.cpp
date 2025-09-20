#include "assert.hpp"
#include "../list/list.hpp"

int main(){
    
    CPP_UNIT_ASSERT t = CPP_UNIT_ASSERT();


    t.assert_equals("AAA", "AAA");
    t.assert_equals("BBB", "BBB");

    return 0;
};
