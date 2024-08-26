#include <ros/ros.h>
#include <turtlesim/Pose.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/String.h>

class GameEngine {
public:
  GameEngine();
  void run();

private:
  void poseCallback(const turtlesim::Pose::ConstPtr& msg, int turtle_id);
  void attackCallback(const std_msgs::String::ConstPtr& msg);

  ros::NodeHandle nh_;
  ros::Subscriber pose_subs_[2];
  ros::Subscriber attack_subs_[2];
  ros::Publisher game_state_pub_;

  float turtle_health_[2];
  int turtle_attacks_left_[2];
  turtlesim::Pose turtle_poses_[2];
};

GameEngine::GameEngine() {
  // Initialize health and attack counts
  turtle_health_[0] = 100.0;
  turtle_health_[1] = 100.0;
  turtle_attacks_left_[0] = 10;
  turtle_attacks_left_[1] = 10;

  // Subscribe to turtle positions and attack commands
  pose_subs_[0] = nh_.subscribe<turtlesim::Pose>("/turtle1/pose", 10, boost::bind(&GameEngine::poseCallback, this, _1, 0));
  pose_subs_[1] = nh_.subscribe<turtlesim::Pose>("/turtle2/pose", 10, boost::bind(&GameEngine::poseCallback, this, _1, 1));
  attack_subs_[0] = nh_.subscribe<std_msgs::String>("/turtle1/attack", 10, &GameEngine::attackCallback, this);
  attack_subs_[1] = nh_.subscribe<std_msgs::String>("/turtle2/attack", 10, &GameEngine::attackCallback, this);

  game_state_pub_ = nh_.advertise<std_msgs::String>("/game_state", 10);
}

void GameEngine::poseCallback(const turtlesim::Pose::ConstPtr& msg, int turtle_id) {
  turtle_poses_[turtle_id] = *msg;
}

void GameEngine::attackCallback(const std_msgs::String::ConstPtr& msg) {
  int attacker_id = (msg->data == "turtle1") ? 0 : 1;
  int target_id = 1 - attacker_id;

  if (turtle_attacks_left_[attacker_id] > 0) {
    float distance = sqrt(pow(turtle_poses_[attacker_id].x - turtle_poses_[target_id].x, 2) +
                          pow(turtle_poses_[attacker_id].y - turtle_poses_[target_id].y, 2));

    if (distance < 2.0) {
      turtle_health_[target_id] -= 10.0;
    }

    turtle_attacks_left_[attacker_id]--;

    if (turtle_attacks_left_[0] == 0 && turtle_attacks_left_[1] == 0) {
      std_msgs::String result;
      result.data = (turtle_health_[0] > turtle_health_[1]) ? "Turtle 1 wins!" : "Turtle 2 wins!";
      game_state_pub_.publish(result);
      ros::shutdown();
    }
  }
}

void GameEngine::run() {
  ros::spin();
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "game_engine_node");
  GameEngine game_engine;
  game_engine.run();
  return 0;
}
