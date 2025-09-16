#  ╔═══════════════════════════════════════════════════════════════════════╗
#  ║ CPP_UNIT_TEST ● lx* = Prefix for linux                                ║
#  ╚═══════════════════════════════════════════════════════════════════════╝

cpp_unit_test: cpp_unit_test/src/main.cpp 
	./cpp_unit_test/bin/main.exe

run: compile
	cls
	./bin/pa1.exe
	
compile: src/evalenum.c bin
	g++ -Iinclude -Wall cpp_unit_test/src/main.cpp -o cpp_unit_test/bin/main.exe
	
clean:
	del -f bin\*.exe obj\*.o

lxrun: lxcompile
	clear
	./bin/pa1.out

lxcompile: src/evalenum.c bin_
	gcc src/evalenum.c -o bin/pa1.out

lxclean:
	rm -rf bin/*.exe obj/*.o 


#  ╔═══════════════════════════════════════════════════════════════════════╗
#  ║ DATA_STRUCTURES ●                                                     ║
#  ╚═══════════════════════════════════════════════════════════════════════╝
