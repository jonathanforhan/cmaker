cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(--CMAKER_REPLACE)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set (CMAKE_VERBOSE_MAKEFILE 0) # 1 should be used for debugging
set (CMAKE_SUPPRESS_REGENERATION TRUE) # Suppresses ZERO_CHECK
if(MSVC)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++17")
    set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)
    if(CMAKE_BUILD_TYPE STREQUAL Release)
        set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin/release)
    elseif(CMAKE_BUILD_TYPE STREQUAL Debug)
        set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin/debug)
    endif()
  if(NOT WIN32)
    set(GLAD_LIBRARIES dl)
  endif()
endif()

include_directories(extern/glad/include/
                     extern/glfw/include/
                     extern/glm/
                     extern/stb/)

# GLFW config
option (GLFW_INSTALL OFF)
option (GLFW_BUILD_DOCS OFF)
option (GLFW_BUILD_EXAMPLES OFF)
option (GLFW_BUILD_TESTS OFF)
add_subdirectory (extern/glfw)

set(GLAD_SOURCE "${CMAKE_SOURCE_DIR}/extern/glad/src/glad.c")

add_subdirectory(src)

target_link_libraries (${PROJECT_NAME}
                       glfw
                       ${GLFW_LIBRARIES}
                       ${GLAD_LIBRARIES})
