cmake_minimum_required(VERSION 3.16.3)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_definitions(-std=c++11)

set(CXX_FLAGS "-Wall")
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} "-std=c++11")

project(binary_tree)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/")
# find_package(gvc REQUIRED)

add_executable(example example.cpp include/node.h include/binary_tree.h)
# target_link_libraries(binary_tree PUBLIC cgraph gvc)