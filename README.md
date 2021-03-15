# Stationary Obstacle Avoidance 

## Context
The teams will be given a sequence of waypoints that should be flown in order during the mission. The waypoint path may be up to 6 miles in length. Teams may attempt the waypoints multiple times, and the highest scoring sequence will be used. To receive points for waypoint accuracy, teams must upload telemetry to the Interoperability System at an average of 1Hz while airborne. Each waypoint will be weighted equally, and the ratio of points received per waypoint will be:

```python
max(0, (100ft - distance) / 100ft)
```

Through the Interoperability System, the teams will be given a set of stationary obstacles. Each stationary obstacle will be a cylinder, with height axis perpendicular to the ground, and bottom face on the ground. The cylinders will have a radius between 30ft and 300ft, and there is no constraint on height. There can be up to 20 stationary obstacles. The ratio of points received for will be:

```python
(obstacles avoided / total obstacles)^3
```


**Sample illustration of competition grid:**

## Problem
Although ArduPilot's autonomous mode (i.e. AUTO) can connect waypoints, it cannot directly (as far as we know) avoid obstacles. As such, we have to put together some software that will be capable of putting together a trajectory that satisfies all of the waypoints while avoiding all of the stationary obstacles. The ideal first step solution would consist of a Stationary Obstacle Avoidance ROS Node that is subscribed to topics from which it recieves the set of waypoints and obstacle specifications, and publishes the new set of waypoints to another topic. To make things easy while we are learning ROS, we will avoid including MAVROS control in the Stationary Obstacle Avoidance Node. This means that the actual control of the drone is abstracted away from this Node.

## Boeing Design Review
*Week of March 29th*

### Deliverables 
- Brief overview of problem context
- Discussion of various path finding algorithms considered
- Discussion of selected algorithm
- Demo of alorithm working in a region w/ layout similar to competition (can be nonROS)
- Present how this will be implemented in ROS 

### Goals
Get feedback on selected path finding algorithm. 
