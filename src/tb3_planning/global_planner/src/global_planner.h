//
// Created by jintain on 12/14/18.
//

#ifndef PROJECT_GLOBAL_PLANNER_H
#define PROJECT_GLOBAL_PLANNER_H

#include <ros/ros.h>
#include <costmap_2d/costmap_2d.h>
#include <nav_core/base_global_planner.h>
#include <geometry_msgs/PoseStamped.h>
#include <angles/angles.h>
#include <base_local_planner/world_model.h>
#include <base_local_planner/costmap_model.h>


using namespace std;

namespace global_planner {


    class GlobalPlanner: public nav_core::BaseGlobalPlanner {

    public:

        GlobalPlanner();
        GlobalPlanner(string name, costmap_2d::Costmap2DROS &costmap_ros);

        // override interfaces of nav_core::BaseGlobalPlanner
        void initialize(std::string name, costmap_2d::Costmap2DROS* costmap_ros);
        // set start and goal, result saved into a series of points (Pose)
        bool makePlan(const geometry_msgs::PoseStamped& start, const geometry_msgs::PoseStamped& goal,
                std::vector<geometry_msgs::PoseStamped> &plan);
    };
}


#endif //PROJECT_GLOBAL_PLANNER_H
