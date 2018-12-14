execute_process(COMMAND "/media/jintain/wd/ros/wps/catkin_ws_my_robot/build/turtlebot3_example/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/media/jintain/wd/ros/wps/catkin_ws_my_robot/build/turtlebot3_example/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
