execute_process(COMMAND "/home/pgupta/catkin_ws/build/uuv_simulation_wrapper/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/pgupta/catkin_ws/build/uuv_simulation_wrapper/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
