# QDAA-AWS-Deep-Racer-Competition
AWS Deep Racer Competition with Reinforcement Learning

In this project, we participated in the AWS DeepRacer Competition by developing a custom reward function for an autonomous racing car using reinforcement learning. Our team experimented with different parameters for the car, such as speed, angle, and other performance factors, to optimize its performance on the race track.

## Background
AWS DeepRacer is a fully autonomous 1/18th scale race car driven by reinforcement learning, which provides a platform for developers to learn about machine learning and apply their knowledge in a fun and engaging competition. The goal of the competition is to develop a reward function that guides the car to complete a race track as quickly and accurately as possible.

Reinforcement learning is a type of machine learning where an agent learns to make decisions by interacting with its environment. The agent's actions are guided by a reward function, which quantifies the desirability of different actions or states. By learning to maximize the cumulative reward, the agent becomes better at navigating the environment and achieving its objectives.

## Reward Function
We developed a custom reward function to optimize the DeepRacer car's performance. The reward function takes into account various parameters, such as the car's distance from the center of the track, speed, steering angle, and progress along the track.

### Components of the Reward Function
* On-track or not: Penalizes the car if it goes off the track or if not all wheels are on the track.
* Distance from center: Rewards the car for staying close to the center of the track.
* Penalize sharp turns: Penalizes the car if it takes sharp turns by considering the angle between the car's heading and the direction to the next waypoint.
* Reward faster speed: Encourages the car to maintain a faster speed by rewarding higher speeds, while also considering the angle of the turn.
* Reward progress: Rewards the car based on the percentage of the track completed.

By combining these components, our reward function encourages the DeepRacer car to follow the optimal racing line, maintain a fast speed, avoid sharp turns, and complete the track as efficiently as possible.

# Results and Future Work
By fine-tuning the parameters and experimenting with different reward function designs, our team was able to improve the DeepRacer car's performance and achieve competitive results in the AWS DeepRacer Competition. Our team won the 8th place by using the model trained with 6 hours.

Future work could explore additional factors to further optimize the car's performance, such as incorporating telemetry data or using more advanced machine learning techniques like deep Q-learning or policy gradient methods.
