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

**Sample illustration of competition grid: Red polygon is the flight boundary. Blue polygon is the search grid.Yellow cylinders are the stationary obstacles. The green line is the waypoint path.**

![CompetitionGrid](https://user-images.githubusercontent.com/41211324/111226905-279cdb80-85b8-11eb-974c-b36faf2976c2.png)

[Here is the link to the competition rules.](https://static1.squarespace.com/static/5d554e14aaa5e300011a4844/t/600835a2dca4d066508885e8/1611150754642/auvsi_suas-2021-rules.pdf)

## Problem
Although ArduPilot's autonomous mode (i.e. `AUTO`) can connect waypoints, it cannot directly (as far as we know) avoid obstacles. As such, we have to put together some software that will be capable of putting together a trajectory that satisfies all of the waypoints while avoiding all of the stationary obstacles. The ideal first step solution would consist of a Stationary Obstacle Avoidance ROS Node that is subscribed to topics from which it recieves the set of waypoints and obstacle specifications, and publishes the new set of waypoints to another topic. To make things easy while we are learning ROS, we will avoid including MAVROS control in the Stationary Obstacle Avoidance Node. This means that the actual control of the drone is abstracted away from this Node.

[Here is the link to`AUTO` modes](https://ardupilot.org/plane/docs/auto-mode.html)

**A general descripton of the node and the topics to which it should connect:**

![StationaryOBSIO](https://user-images.githubusercontent.com/41211324/111229728-cdeae000-85bc-11eb-9dfb-edf9bcf12cfa.png)

## Boeing Design Review
*Week of March 29th*

### Deliverables 
-Brief overview of problem context
- Discussion of various path finding algorithms considered
  - Simple examples of algorithms seriously using matplotlib 
- Discussion of selected algorithm
  -Comparison of runtimes/computational needs of algorithm
- Demo of alorithm working in a region w/ layout similar to competition (can be nonROS)
  - Read sample waypoint list from a JSON 
- Present how this will be implemented in ROS 

### Goals
Get feedback on selected path finding algorithm. 
