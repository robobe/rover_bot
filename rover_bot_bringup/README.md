
```
cd /home/user/projects/rover_bot
tmuxp load ./rover_bot_bringup/config/tmux_sitl_and_gazebo.yaml
```

## mavros
```bash
ros2 launch mavros apm.launch fcu_url:=udp://:14550@
```