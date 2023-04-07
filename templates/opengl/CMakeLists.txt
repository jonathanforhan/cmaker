cmake_minimum_required(VERSION 3.20)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(--CMAKER_REPLACE)

if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++17")
  if(NOT WIN32)
    set(GLAD_LIBRARIES dl)
  endif()
endif()

include_directories(extern/glad/include/
                    extern/glfw/include/
                    extern/glm/
                    extern/stb/)

# GLFW config
option(GLFW_INSTALL OFF)
option(GLFW_BUILD_DOCS OFF)
option(GLFW_BUILD_EXAMPLES OFF)
option(GLFW_BUILD_TESTS OFF)
add_subdirectory(extern/glfw)

set(GLAD_SOURCE "${CMAKE_SOURCE_DIR}/extern/glad/src/glad.c")

add_subdirectory(src)

# EXTERN DEPENDENCIES
target_link_libraries (${PROJECT_NAME}
                       PRIVATE
                       glfw
                       ${GLFW_LIBRARIES}
                       ${GLAD_LIBRARIES})
