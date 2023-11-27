# export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

import asyncio
import pygazebo

def cb(data):
    poses_stamped = pygazebo.msg.world_stats_pb2.WorldStatistics()
    poses_stamped.ParseFromString(data)
    print(poses_stamped)

async def publish_loop():
    manager = await pygazebo.connect()
    subscriber = await manager.subscribe("/gazebo/default/world_stats", 
    'gazebo.msgs.WorldStatistics', cb)
    while True:
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(publish_loop())