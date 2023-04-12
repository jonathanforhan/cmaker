cmake_minimum_required(VERSION 3.20)

project(--CMAKER_REPLACE)

# see cmaker-config.json for additional config flags
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++17")
endif()

add_subdirectory(src)

add_executable(${CMAKE_PROJECT_NAME}
    ${APP_SOURCE}
    )

# target_link_libraries(${CMAKE_PROJECT_NAME}
#     PRIVATE
#     )

target_include_directories(${CMAKE_PROJECT_NAME}
    PRIVATE
    ${APP_INCLUDE}
    )

