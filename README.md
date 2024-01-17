# bbot_ros2_control_demo
ros2_control——hardware编写测试

**1.rrbot_demo-main模型，启动gazebo，用ros2_control命令行控制**

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
//重定向/diff_drive/cmd_vel_unstamped到键盘话题/cmd_vel，使用键盘去控制车轮速度
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_drive/cmd_vel_unstamped

```
