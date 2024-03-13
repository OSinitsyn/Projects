#include <iostream>
#include <chrono>

class scoped_timer
{
public:
    using clock_type = std::chrono::steady_clock;
    using time_units = std::chrono::microseconds;

    scoped_timer(const char* func)
    : func_{func},
      start_{clock_type::now()}
    {}

    ~scoped_timer()
    {
        auto stop = clock_type::now();
        auto duration = stop - start_;
        auto microsec = std::chrono::duration_cast<time_units>(duration).count();
        std::cout << "Function " << func_ << " took " << microsec << " us\n";
    }
private:
    const char* func_{};
    const clock_type::time_point start_{};
};
