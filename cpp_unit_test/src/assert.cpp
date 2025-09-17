#include "../include/assert.hpp"


CPP_UNIT_ASSERT::CPP_UNIT_ASSERT(){
    total_tests = 0;
    success_tests = 0;
    log_messages = "";
};

CPP_UNIT_ASSERT::~CPP_UNIT_ASSERT(){
    std::cout << "Total de testes: " << total_tests << std::endl;
    std::cout << "Testes com sucesso: " << success_tests << std::endl;
    std::cout << "Testes com falha: " << total_tests - success_tests << std::endl;
    if(log_messages != ""){
        std::cout << "Log de falhas: " << std::endl;
        std::cout << log_messages << std::endl;
    }
};

void CPP_UNIT_ASSERT::assert_equals(const std::string act, const std::string exp){
    total_tests++;
    if(act == exp){
        std::cout << "CERTO" << std::endl;
        success_tests++;
    } else {
        std::cout << "ERRADO" << std::endl;
        log_messages += "ERRO! Esperado: " + exp + " | Recebido: " + act + "\n";
    }
};