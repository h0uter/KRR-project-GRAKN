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


		 aruco_cube_444 - object 

    )
    (:init
        (=(efficiency)0)
        (=(object_function)2)
        (robot-at tiago wp0)
        (requires-packaging aruco_cube_582)
        (free rightgrip)
        (can_move tiago)

		(object-at aruco_cube_444 wp_table_1) 
		(active aruco_cube_444 wp_table_1) 

    )
    (:goal (and
  

		(object-at aruco_cube_444 wp_cabinet_2) 
)) 
) 
