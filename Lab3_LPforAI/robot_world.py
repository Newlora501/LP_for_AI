import time
from geometry_msg.msg import Twist 
import subprocess
import rclpy
from rclpy.node import Node
from pyperplan import domain, planner

# Определение класса для задания среды
class RobotWorld(Node):
    def __init__(self):
        super().__init__(('robot_world'))
        self.publisher = self.create_publisher(Twist,'cmd_vol',10)
        self.plan = []
        self.current_step=0
        self.getPlan()

    def getPlan(self):
        domain_file = '/home/turtlebot3_ws/src/domain.pddl'
        problem_file = 'home/turtlebot3_ws/src/problem.pddl'
        result = subprocess.run(['pyperplan','--heuristic','hff','--search','aster',domain_file,problem_file],stdout=subprocess.PIRE,text=True
        )
        plan_output=result.stdout.splitlines()
        self.get_logger().info(f'Plan:{self.plan}')


# Функция для вывода плана
    def print_plan(self):
        if self.current_step<len(self.plan)
            action=self.plan[self.current.step]
            self.get_logger().info(f'Executing:{action}')
            parts = action.replace('(','').replace(')','').split()
            _, robot, start_location, end_location = parts
            self.move()
            self.current_step +=1

        else:
            self.get_logger().into('Plan completed')
    
    def action(self):
        msg = Twist()
        msg.linear.x=0.5
        msg.angulair.z = 0.0
        self.get_logger().info(f'Robot command: {msg}')
        self.publisher_.publisher(msg)
        time.sleep(6)
        msg.linear.x=0.0
        self.publisher_.publisher(msg)
        self.get_logger.info(f'Robot is not moving')

    def main(args=None):
        rclpy.init(args=args)
        robot_world=RobotWorld()
        rclpy.spin(robot_world)
        robot_world.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()    


