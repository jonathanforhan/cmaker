cmake_minimum_required(VERSION 3.2)

project(--CMAKER_REPLACE)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(OUTPUT "debug" CACHE STRING "binary output, default: debug")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin/${OUTPUT}")

# -- Do not remove tags below if you desire cmkr dependency building -- #
#CMAKER_SET
#CMAKER_FIND
# -- End CMaker -- #

add_subdirectory(src)
