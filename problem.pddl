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


		 444 - object 

    )
    (:init
        (robot-at tiago wp0)
        (free rightgrip)
        (can_move tiago)

		(object-at 444 wp_table_1) 

    )
    (:goal (and
  

		(object-at 444 wp_cabinet_1) 
)) 
) 
