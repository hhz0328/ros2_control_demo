# ros2_control_demo
ros2_control——hardware编写测试

**1.rrbot_demo-main(差速小车模型），启动gazebo，用ros2_control命令行控制**

参考：https://github.com/WMGIII/bbot_demo
```
//启动launch
ros2 launch bbot_bringup bbot_bringup.launch.py
```
```
// 查看hardware_interfaces
ros2 control list_hardware_interfaces
// 查看controllers
ros2 control list_controllers
// 话题
ros2 topic list
```
```
//重定向/diff_drive/cmd_vel_unstamped话题到键盘话题/cmd_vel，使用键盘去控制车轮速度
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_drive/cmd_vel_unstamped

```
**2.rrbot_ws（简化机械臂模型）**

参考：https://github.com/ros-controls/roscon2022_workshop/tree/7-robot-hardware-interface/solution
```
// 启动一个即可，推荐第一个

// 老版本gazebo环境
ros2 launch controlko_bringup rrbot_sim_gazebo_classic.launch.py
// 新版本gazebo环境
ros2 launch controlko_bringup rrbot_sim_gazebo.launch.py
```
```
//在gazebo环境启动的基础上，启动控制launch（每4s发布一次目标位置）
ros2 launch controlko_bringup test_joint_trajectory_controller.launch.py
```

