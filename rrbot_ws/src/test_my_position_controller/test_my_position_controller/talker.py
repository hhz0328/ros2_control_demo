# rrbot_position_publisher
import rclpy
from rclpy.node import Node
from control_msgs.msg import JointJog

class Talker(Node):
    def __init__(self,name):
        super().__init__(name)
        self.position_publisher = self.create_publisher(JointJog, 'my_controller/reference', 10)
        self.msg = JointJog()
        self.msg.joint_names = ['joint1', 'joint2']
        self.dates = [[0.0, 0.0], [-1.0, -1.0], [0.0, 0.0], [1.0, 1.0]]
        self.i = 0
        self.timer = self.create_timer(3, self.timer_callback)

    def timer_callback(self):
        self.msg.displacements = self.dates[self.i % 4]
        self.i += 1
        self.position_publisher.publish(self.msg)


def main(args=None):
    rclpy.init(args=args)
    node = Talker("rrbot_pos_pub")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()