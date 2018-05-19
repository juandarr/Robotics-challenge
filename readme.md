# Purpose
This repository contains the solutions to the problems defined in the Kiwi robotics challenge. 

# Guidelines to explore each solution
In this section I present some general comments and tips to explore the solutions

## Task 2.1
See Task2_1.png to visualize the setting used to solve the task. All the topics are store in the bag file Task2_1.bag and the topic /odom can be used the see the linear and angular speed of the entity. 

```bash
rostopic echo /odom
```

## Task 2.2
See Task2_2.png to visualize proof of solution. 
To install the package to teleoperate the entity the following command was used:

```bash
sudo apt-get install ros-kinetic-teleop-twist-keyboard
```

To see the linear and angular speed use **rostopic echo** as in the previous task.

## Task 3.1 
See Task3_1.png to visualize proof of the solution. 
To visualize the robot in motion given the messages stored in the bag file Task3_1.bag follow the next commands in different terminals:

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
See Task3_3.png to visualize proof of the solution. 
The created node (location_monitoring) publishes the requested information to three different topics: *robotPosition*, *closestObject* and *targetLandmark*.
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
To see wether the robot is in a specific landmark region use:
```bash
rostopic echo /targetLandmark
```

## Task 3.4