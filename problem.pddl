(define (problem pick_place)
    (:domain pick_place)
    (:requirements :strips :typing)

    (:objects   tiago - robot
                leftgrip rightgrip - gripper
                wp_table_2 - waypoint
                wp_table_1 - waypoint
                wp_table_3 - waypoint
                wp0 - waypoint
                aruco_cube_444 - object
                aruco_cube_582 - object
    )
    (:init
        (=(efficiency)0)
        (=(object_function)2)
        (robot-at tiago wp0)
        (object-at aruco_cube_444 wp_table_1)
        (object-at aruco_cube_582 wp_table_1)
        (requires-packaging aruco_cube_582)
        (free rightgrip)
        (active aruco_cube_444)
        (active aruco_cube_582)
        (can_move tiago)
        
    )
    
    (:goal (and

		(object-at aruco_cube_444 wp_cabinet_2) 
)) 
) 
