#rrbot_position_subscriber
import rclpy
from rclpy.node import Node
from control_msgs.msg import JointJog

class Listener(Node):
    def __init__(self,name):
        super().__init__(name)
        self.state_subscriber = self.create_subscription(JointJog, "my_controller/state", self.state_callback, 10) 

    def state_callback(self, msg):
        self.get_logger().info(f'time: {msg.header.stamp.sec} -------')
        for i in range(0, 2):
            self.get_logger().info(f'{msg.joint_names[i]}: {msg.displacements[i]}')
        self.get_logger().info('-------------------------------------')


def main(args=None):
    rclpy.init(args=args)
    node = Listener("rrbot_pos_sub")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
