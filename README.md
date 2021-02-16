# Obstacle-Avoidance-Simulation

Hello everyone, this is a project on simulating (using Gazebo) an algorithm (https://www.researchgate.net/publication/221105331_Stereovision-Based_Algorithm_for_Obstacle_Avoidance#pf8) to avoid obstacles for any automobile with a stereo camera attached in the front.
Specifically it is designed to suit the needs of a Rover that I'm working on as a developer part of a team in my college. 

In order to run this you need to have the following dependencies installed (as of Feb 16, 2021) :
1. Python3
2. ROS Melodic Morenia (Python version) (http://wiki.ros.org/melodic/Installation) 
3. Gazebo

Once you have these dependecies successfully installed, clone the repository into your local workspace. After that in a new terminal run the following command :

roslaunch obstacle_avoidance obs_avoid.launch

This will launch Gazebo with the a rover model. And once you have done till here go ahead and some obstacles around in the environment and then in another new terminal run this command :

python3 opencv_to_ros.py

And you will see the the rover move staright unless an obstacle is seen infront of it.

[This file is incomplete as of Feb 16, 2021, I'm actually new to mainting a project in this manner and so I would like to take my time and put it together in a clean way]
