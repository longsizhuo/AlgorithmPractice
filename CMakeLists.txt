cmake_minimum_required(VERSION 3.29)
project(AlgorithmPractice)

set(CMAKE_CXX_STANDARD 14)

include_directories("loong's code/small_tools")

add_executable(AlgorithmPractice
        "loong's code/small_tools/remove_element.cpp"
        "loong's code/small_tools/remove_element.h")
