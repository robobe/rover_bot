
. /usr/share/gazebo/setup.sh
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`pwd`/rover_bot_description/models
export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:`pwd`/rover_bot_gazebo/worlds
export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:`pwd`/rover_bot_gazebo/bin