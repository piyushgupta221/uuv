# CMake generated Testfile for 
# Source directory: /home/pgupta/catkin_ws/src/lauv_gazebo/lauv_description
# Build directory: /home/pgupta/catkin_ws/build/lauv_description
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_lauv_description_rostest_test_test_urdf_files.test "/home/pgupta/catkin_ws/build/lauv_description/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/noetic/share/catkin/cmake/test/run_tests.py" "/home/pgupta/catkin_ws/build/lauv_description/test_results/lauv_description/rostest-test_test_urdf_files.xml" "--return-code" "/usr/bin/python3 /opt/ros/noetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/pgupta/catkin_ws/src/lauv_gazebo/lauv_description --package=lauv_description --results-filename test_test_urdf_files.xml --results-base-dir \"/home/pgupta/catkin_ws/build/lauv_description/test_results\" /home/pgupta/catkin_ws/src/lauv_gazebo/lauv_description/test/test_urdf_files.test ")
set_tests_properties(_ctest_lauv_description_rostest_test_test_urdf_files.test PROPERTIES  _BACKTRACE_TRIPLES "/opt/ros/noetic/share/catkin/cmake/test/tests.cmake;160;add_test;/opt/ros/noetic/share/rostest/cmake/rostest-extras.cmake;52;catkin_run_tests_target;/home/pgupta/catkin_ws/src/lauv_gazebo/lauv_description/CMakeLists.txt;19;add_rostest;/home/pgupta/catkin_ws/src/lauv_gazebo/lauv_description/CMakeLists.txt;0;")
subdirs("gtest")
