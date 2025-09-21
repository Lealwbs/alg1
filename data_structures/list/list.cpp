#include "list.hpp"

List::List(){};  
List::~List(){};
List::List(const List& other){}
List& List::operator=(const List& other){}

int List::Size(){};
bool List::Empty(){};
std::string List::ToString(){};

int List::Get(int pos){}; 
void List::Set(int value, int pos){};

void List::PushFront(int value){};
void List::PushBack(int value){};
void List::PushAt(int value, int pos){};

int List::PopFront(){};
int List::PopBack(){};
int List::PopAt(int pos){};

int List::Search(int value){};
void List::Clear(){};