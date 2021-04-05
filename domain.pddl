(define (domain pick_place)

    (:requirements :typing :durative-actions :fluents
        )

    (:types
        waypoint
        robot
        object
        gripper
    )
    
    (:predicates
        (packaged-at ?obj - object ?wp - waypoint)
        (robot-at ?v - robot ?wp - waypoint)
        (object-at ?obj - object ?wp - waypoint)
        (is_holding ?g - gripper ?obj - object)
        (free ?g - gripper)
        (can_move ?v - robot)
    )
    
    (:durative-action move
        :parameters (?v - robot ?from ?to - waypoint)
        :duration ( = ?duration 2)
        :condition (and
            (at start (robot-at ?v ?from))
            (at start (can_move ?v))
        )
        :effect (and
            (at end (robot-at ?v ?to))
            (at start(not(robot-at ?v ?from)))
            (at end(not(can_move ?v)))
        )
    )

    (:durative-action pick
        :parameters (?v - robot ?wp - waypoint ?obj - object ?g - gripper)
        :duration (= ?duration 2)
        :condition (and
            (over all(free ?g))
            (at start(object-at ?obj ?wp))
            (over all(robot-at ?v ?wp))
        )
        :effect (and
            (at end (not (object-at ?obj ?wp)))
            (at end (not (free ?g)))
            (at end (is_holding ?g ?obj))
            (at end (can_move ?v))
        )
    )
    
    (:durative-action place
        :parameters (?v - robot ?wp - waypoint ?obj - object ?g - gripper)
        :duration (= ?duration 2)
        :condition (and
            (at start(is_holding ?g ?obj))
            (over all(robot-at ?v ?wp))
        )
        :effect (and
            (at end (free ?g))
            (at end (not(is_holding ?g ?obj)))
            (at end (object-at ?obj ?wp))
            (at end (packaged-at ?obj ?wp))
            (at end (can_move ?v))
        )
    )    
)

