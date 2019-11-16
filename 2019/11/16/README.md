# Playing with C++ std::variant

[std::variant](https://en.cppreference.com/w/cpp/utility/variant) is a
type-safe union. The following [blog
post](https://www.bfilipek.com/2018/06/variant.html) already gives a lot of
details and examples related to `std::variant`. In this short blog post, I want
to discuss interesting behavior when non-class types `std::variant` is
initialized with an object.

[valueless_by_exception](https://en.cppreference.com/w/cpp/utility/variant/valueless_by_exception)
gives an interesting example of what happens if an exception is thrown from
`operator int()`. It's also interesting what happens if an exception is not
thrown. Even though `std::variant` might be declared to hold only non-class
types, it's still possible to assign an object of a class that implements e.g.
`operator int()`. In that case, the operator is going to be called, and value
is going to be copied to the `std::variant`. Take a look at the following
example:

```
struct Struct {
  operator int() { return foo; }
  int foo;
}
std::variant<int, float> bar = Struct();
```

You can find the full `std::variant` experimental code
[here](https://github.com/gitbuda/education/blob/master/programming_languages/cpp/variant/main.cpp).
