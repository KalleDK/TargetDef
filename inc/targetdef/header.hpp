#ifndef TARGETDEF_HEADER_HPP
#define TARGETDEF_HEADER_HPP

#if defined(TARGET_A)
#include "targeta/header.hpp"
#elif defined(TARGET_B)
#include "targetb/header.hpp"
#else
#error "No known TARGET defined"
#endif

#endif
