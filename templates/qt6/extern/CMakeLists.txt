###############################################################################
###                                QT6 Setup                                ###
###############################################################################

macro(QT_INIT)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets)

set(QT_LIBS Qt${QT_VERSION_MAJOR}::Widgets)
endmacro()

macro(QT_SETUP_EXE)
if(APPLE)
    set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES
        MACOSX_BUNDLE_GUI_IDENTIFIER cmaker.--CMAKER_REPLACE.com
        MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
        MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
        MACOSX_BUNDLE TRUE
        )
elseif(WIN32)
    set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES
        WIN32_EXECUTABLE TRUE
        )
endif()

install(TARGETS ${CMAKE_PROJECT_NAME}
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR})

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(${CMAKE_PROJECT_NAME})
endif()
endmacro()
