// Playing with C++ std::variant
//
// https://en.cppreference.com/w/cpp/utility/variant
//
// Compile command: clang++ -std=c++1z main.cpp
#include <iostream>
#include <variant>

struct Struct {
  operator int() { return foo; }
  int foo;
};

int main() {
  std::variant<int, float> bar = Struct{.foo = 10};
  std::cout << std::get<int>(bar) << std::endl;
  return 0;
}
