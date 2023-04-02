import math
def reward_function(params):
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    waypoints = params['waypoints']
    next_waypoint = waypoints[params['closest_waypoints'][1]]
    heading = params['heading']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
        
    angle = abs(heading - math.atan2(next_waypoint[1] - params['y'], next_waypoint[0] - params['x'])) % (2 * math.pi)

    # 1. ontrack or not
    if (not all_wheels_on_track) or (is_offtrack):
        return float(1e-3)

    # 2. distance from center
    reward_center = math.exp(-15 * (distance_from_center / (0.5 * track_width)))

    # 3. penalize sharp returns
    # if the angle is small
    if (angle > math.pi / 3) and (angle < 2 * math.pi / 3):
        abs_steering = abs(params['steering_angle'])
        steering_penalty = 0.5 * abs_steering / 30
        reward_steering = 1-steering_penalty
    else:
        reward_steering = 1

    # 4. reward faster speed
    normalized_angle = angle / (2 * math.pi)
    normalized_speed = (speed - 0.5) / (4-0.5)
    # penalize larger angle
    reward_speed = (2 - normalized_angle) * normalized_speed + 1e-3

    # 5. reward by progress
    reward_progress = progress / 100.0

    return float(reward_center * reward_steering * reward_speed + 0.1 * reward_progress)

