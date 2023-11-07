# First run
- Run gazebo with Rover
- Run sitl
- Run mavproxy
- Set mode: GUIDED
- Send Attitude command

```bash title="Terminal1 - Gazebo"
gazebo --verbose rover_world.sdf
```

```bash title="Terminal2 - SITL"
./rover_bot_bringup/bin/ardurover -S \
--model gazebo-rover \
--speedup 1 \
--defaults /home/user/projects/rover_bot/rover_bot_bringup/config/rover.parm \
-I1
```

```bash title="mavproxy"
mavproxy.py --master tcp:127.0.0.1:5770
```

| Example MAVProxy/SITL Command | Description                             |
| ----------------------------- | --------------------------------------- |
| attitude 1 0 0 0 1            | face North, move forward at WP_SPEED    |
| attitude 1 0 0 0 -1           | face North, move in reverse at WP_SPEED |

```

```