project(PackageTest CXX)
cmake_minimum_required(VERSION 3.5)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(testdef test.cpp)

if(true)
	target_link_libraries(testdef PRIVATE CONAN_PKG::TargetDef)
else()
	find_package(targetdef REQUIRED)
	target_link_libraries(testdef PRIVATE targetdef)
endif()

