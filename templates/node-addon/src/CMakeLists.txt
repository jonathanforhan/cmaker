add_library(${CMAKE_PROJECT_NAME} SHARED lib.cc ${CMAKE_JS_SRC})
set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "" SUFFIX ".node")
target_link_libraries(${CMAKE_PROJECT_NAME} ${CMAKE_JS_LIB})
target_include_directories(${PROJECT_NAME} PRIVATE ${NODE_ADDON_API_DIR})

if(MSVC AND CMAKE_JS_NODELIB_DEF AND CMAKE_JS_NODELIB_TARGET)
  # Generate node.lib
  execute_process(COMMAND ${CMAKE_AR} /def:${CMAKE_JS_NODELIB_DEF} /out:${CMAKE_JS_NODELIB_TARGET} ${CMAKE_STATIC_LINKER_FLAGS})
endif()

if(MSVC)
  target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE /W4 /WX)
else()
  target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -Wall -Wextra -Wpedantic)
endif()
