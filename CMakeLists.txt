cmake_minimum_required(VERSION 3.5)
project(targetdef)

include(GNUInstallDirs)

option(BUILD_SHARED_LIBS "Build Shared Libs" ON)

if(BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

set(TARGET_TYPE "A" CACHE STRING "TARGET_TYPE chosen by the user at CMake configure time")
set_property(CACHE TARGET_TYPE PROPERTY STRINGS "A" "B")

add_library(${PROJECT_NAME} src/dummy.cpp)

if (${TARGET_TYPE} STREQUAL "A")
	target_sources(${PROJECT_NAME} PRIVATE src/targeta/header.cpp)
	target_compile_definitions(${PROJECT_NAME} PUBLIC TARGET_A)
else()
    target_sources(${PROJECT_NAME} PRIVATE src/targetb/header.cpp)
	target_compile_definitions(${PROJECT_NAME} PUBLIC TARGET_B)
endif()


target_include_directories(${PROJECT_NAME} PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/inc>  
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Config
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
	COMPONENT libraries
	)
	
install(DIRECTORY inc/
	DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
	COMPONENT headers
	)
	
install (EXPORT ${PROJECT_NAME}Config DESTINATION share/${PROJECT_NAME}/cmake)