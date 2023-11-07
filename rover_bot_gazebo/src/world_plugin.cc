#include <gazebo/gazebo.hh>
#include <gazebo/common/common.hh>

namespace gazebo
{
    class WorldPluginTutorial : public WorldPlugin
    {
    public:
        WorldPluginTutorial() : WorldPlugin()
        {
            gzmsg << "gazebo message \n";
            gzdbg << "gazebo debug \n";
            gzwarn << "gazebo warning \n";
            gzerr << "gazebo error \n";
        }

    public:
        void Load(physics::WorldPtr _world, sdf::ElementPtr _sdf)
        {
        }
    };
    GZ_REGISTER_WORLD_PLUGIN(WorldPluginTutorial)
}