add_executable(${CMAKE_PROJECT_NAME} main.cpp)

#add_library(foolib STATIC foo.cpp)
#target_include_directories(foolib PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/src")
#target_link_libraries(${CMAKE_PROJECT_NAME} PUBLIC foolib)

if(MSVC)
  target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE /W4 /WX)
else()
  target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic)
endif()
