cmake_minimum_required(VERSION 3.20)

project(exampleABC)

# see cmaker-config.json for additional config flags
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic -std=c++17")
endif()

add_subdirectory(extern)
add_subdirectory(src)

QT_INIT()

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(${CMAKE_PROJECT_NAME}
        MANUAL_FINALIZATION
        ${APP_SOURCE}
    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET ${CMAKE_PROJECT_NAME} APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(${CMAKE_PROJECT_NAME} SHARED
            ${APP_SOURCE}
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(${CMAKE_PROJECT_NAME}
            ${APP_SOURCE}
        )
    endif()
endif()

target_link_libraries(${CMAKE_PROJECT_NAME}
    PRIVATE
    ${QT_LIBS}
    )

target_include_directories(${CMAKE_PROJECT_NAME}
    PRIVATE
    ${APP_INCLUDE}
    )

QT_SETUP_EXE()
