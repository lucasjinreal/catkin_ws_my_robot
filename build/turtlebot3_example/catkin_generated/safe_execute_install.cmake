execute_process(COMMAND "/media/jintain/sg/ai/career/robot/ctirobot/ros_sp/catkin_ws_my_robot/build/turtlebot3_example/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/media/jintain/sg/ai/career/robot/ctirobot/ros_sp/catkin_ws_my_robot/build/turtlebot3_example/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
