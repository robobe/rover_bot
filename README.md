
# Pre config and Setup
- Clone Ardopilot gazebo classic plugin [github](git clone https://github.com/khancyr/ardupilot_gazebo
)
- Build and install in `rover_bot_gazebo` folder
- Run SITL with mavproxy


# usage
- source `env.sh` to fix all gazebo environment variables

!!! tip "tmuxp"
    Using tmux session manage to open multiple pane in once

    ```
    sudo apt install tmuxp
    ```
     

```
./rover_bot_bringup/bin/ardurover -S --model gazebo-rover \
--speedup 1 \
--defaults /home/user/projects/rover_bot/rover_bot_bringup/config/rover.parm \
-I0
```

# plane
```
sim_vehicle.py -v ArduPlane -f gazebo-zephyr  -m --mav10 --map --console -I0

```

```
MANUAL> mode fbwa
FBWA> arm throttle
FBWA> rc 3 1800
FBWA> mode circle
```