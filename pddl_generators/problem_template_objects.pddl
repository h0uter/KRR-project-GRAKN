(define (problem pick_place)
    (:domain pick_place)
    (:requirements :strips :typing)

    (:objects   tiago - robot
                leftgrip rightgrip - gripper
                wp_table_2 - waypoint
                wp_table_1 - waypoint
                wp_table_3 - waypoint
		wp_cabinet_1 - waypoint
		wp_cabinet_2 - waypoint
                wp0 - waypoint
                aruco_cube_582 - object


