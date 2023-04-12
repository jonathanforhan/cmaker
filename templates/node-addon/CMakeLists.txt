cmake_minimum_required(VERSION 3.20)
cmake_policy(SET CMP0091 NEW)
cmake_policy(SET CMP0042 NEW)

project(--CMAKER_REPLACE)

# see cmaker-config.json for additional config flags
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++17")
endif()

# NAPI includes
add_definitions(-DNAPI_VERSION=3)
include_directories(${CMAKE_JS_INC})
execute_process(COMMAND node -p "require('node-addon-api').include"
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        OUTPUT_VARIABLE NODE_ADDON_API_DIR
        )
string(REPLACE "\n" "" NODE_ADDON_API_DIR ${NODE_ADDON_API_DIR})
string(REPLACE "\"" "" NODE_ADDON_API_DIR ${NODE_ADDON_API_DIR})

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

