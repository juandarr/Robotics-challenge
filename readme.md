# Purpose
This repository contains the solutions to the problems defined in the Kiwi robotics challenge. 

# Guidelines to explore each solution
In this section I present some general comments and tips to explore the solutions

## Task 2.1
See *Task2_1.png* to visualize the setting used to solve the task. All the topics are store in the bag file *Task2_1.bag* and the topic /odom can be used the see the linear and angular speed of the entity. 

```bash
rostopic echo /odom
```

## Task 2.2
See *Task2_2.png* to visualize proof of solution. 
To install the package to teleoperate the entity the following command was used:

```bash
sudo apt-get install ros-kinetic-teleop-twist-keyboard
```

To see the linear and angular speed use **rostopic echo** as in the previous task.

## Task 3.1 
See *Task3_1.png* to visualize proof of the solution. 
To visualize the robot in motion given the messages stored in the bag file *Task3_1.bag* follow the next commands in different terminals:

```bash
roscore
```
```bash
roslaunch turtlebot_gazebo turtlebot_world.launch
```
```bash
rosbag play Task3_1.bag
```

## Task 3.3
See *Task3_3.png* to visualize proof of the solution. 
The created node (location_monitoring) publishes the requested information to three different topics: *robotPosition*, *closestObject* and *targetLandmark*. This node was packaged in a python script and can be executed with the command `rosrun location_monitor location_monitor.py` which will create the three topics mentioned before. 
To visualize the robot in motion given the messages stored in the bag file Task3_3.bag and see the published topics showing the requested information for the task follow the next commands in different terminals:

```bash
roscore
```
```bash
roslaunch turtlebot_gazebo turtlebot_world.launch
```
```bash
rosbag play Task3_3.bag
```
To see the x and y position of the robot:
```bash
rostopic echo /robotPosition
```
To see the which is closest landmark to the robot and the distance at any moment use:
```bash
rostopic echo /closestObject
```
To see whether the robot is in a specific landmark region use:
```bash
rostopic echo /targetLandmark
```

## Task 3.4
See *Task3_4.png* to visualize proof of the solution. 
To install a Lidar to the robot the instructions provided in the following link were used: [Lidar with hokuyo for Slam](http://wiki.ros.org/turtlebot/Tutorials/indigo/Adding%20a%20lidar%20to%20the%20turtlebot%20using%20hector_models%20%28Hokuyo%20UTM-30LX%29#CA-a4b8247611cab5be4c2262f31aa20c7f471977fc_2) and [Adding Lidar to turtlebot and gazebo](http://amanbreakingthings.blogspot.com.co/2014/11/adding-hokuyo-lidar-to-turtlebot-in-ros.html) and many others (such as turtlebot and intermediate ROS tutorials).
When all the launch files and modification were created, the following commands are used to map the simulated map using SLAM and LIDAR (each one in a different command window):
```bash
roscore
```
```bash
roslaunch turtlebot_gazebo turtlebot_world.launch
```
This command uses SLAM 
```bash
roslaunch turtlebot_navigation gmapping_demo_hokuyo.launch
```
This command open the RVIZ environment to visualize the location and mapping of the robot with LIDAR and SLAM
```bash
roslaunch turtlebot_rviz_launchers view_navigation.launch
```
This command provides teleoperation function to control the turtlebot in simulated worlds
```bash
roslaunch turtlebot_teleop keyboard_teleop.launch
```

Given this setting, the command rosbag is used for 60 seconds and stores the data associated to the mapping and location. The file *Task3_4.bag* stores the requested data for the task. To play and visualize the map data open **RVIZ** with `rosrun rviz rviz`, then add components for the map, robotModel, laserscan, costmap and run the bag file with
```bash
rosbag play Task3_4.bag
``` 
Don't forget to add the topics relevants for each component, such as `/map` for map and  `scan` for laserscan.