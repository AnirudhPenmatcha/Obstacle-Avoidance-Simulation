# Obstacle-Avoidance-Simulation

Hello everyone, this is a project on simulating (using Gazebo) an algorithm (https://www.researchgate.net/publication/221105331_Stereovision-Based_Algorithm_for_Obstacle_Avoidance#pf8) to avoid obstacles for any automobile with a stereo camera attached in the front.
Specifically, it is designed to suit the needs of a rover that I'm working on as a member of the developer domain in a tech team at my college. 

In order to run this you need to have the following dependencies installed (as of Feb 16, 2021) :
1. Python3 
2. ROS Melodic Morenia (Python version) (http://wiki.ros.org/melodic/Installation) 
3. Gazebo
4. opencv-python 4.4.0.42 (https://pypi.org/project/opencv-python/4.4.0.42/)
5. numpy 1.17.2 (https://pypi.org/project/numpy/1.17.2/)

Once you have these dependecies successfully installed, clone the repository into your local workspace. After that in a new terminal run the following command :

`roslaunch obstacle_avoidance obs_avoid.launch`

This will launch Gazebo with the model of a rover. And once you have come till here go ahead and place some obstacles around in the environment and then in another new terminal run this command :

`python3 opencv_to_ros.py`

And you will see that the rover will move staright unless an obstacle is seen infront of it.


[Have decided to take an approach using LIDAR instead of Stereo camera as it turned out to be more reliable for our use case hence I won't be continuing to update this]
