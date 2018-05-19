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
