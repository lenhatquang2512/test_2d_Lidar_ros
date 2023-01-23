# ROS Object Obstacle Cartesian Data obtained from 2D LiDAR (A1 RPLidar)


---


### Requirements
* Ubuntu 20.04
* ROS Noetic
* Eigen

### Install (without catkin)
* `mkdir -p /catkin_ws/src`
* `cd ..`
* `catkin_make`
* `cd src`
* `git clone https://github.com/lenhatquang2512/test_2d_Lidar_ros.git`
* `git clone https://github.com/robopeak/rplidar_ros.git`
* `cd .. & catkin_make`
* `source devel/setup.bash`


### Usage
* roslaunch test_2d_lidar test_lidar.launch 

* How to check :

`rostopic echo /obstacle_points`

 `rosrun rqt_graph rqt_graph`


### Reason I created this package

Just want to play with 2D Lidar. I will implement DWA navigation method in the future using this repo.
