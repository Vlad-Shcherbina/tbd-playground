#include "sample.h"

#include <algorithm>


std::vector<int> reverse(std::vector<int> xs) {
    std::reverse(xs.begin(), xs.end());
    return xs;
}
