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
        (active ?obj - object)
        (requires-packaging ?obj - object)
        (packaged-at ?obj - object ?wp - waypoint)
        (robot-at ?v - robot ?wp - waypoint)
        (object-at ?obj - object ?wp - waypoint)
        (is_holding ?g - gripper ?obj - object)
        (free ?g - gripper)
        (can_move ?v - robot)
        (can_work_here ?v - robot ?wp - waypoint)
    )
    (:functions 
        (efficiency)
        (object_function)
    )

    (:durative-action move
        :parameters (?v - robot ?from ?to - waypoint)
        :duration ( = ?duration 2)
        :condition (and
            (at start (robot-at ?v ?from))
            (at start (can_move ?v))
        )
        :effect (and
            (at end(increase (object_function) (efficiency)))
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
            (at start(active ?obj))
        )
        :effect (and
            (at end(increase (object_function) (efficiency)))
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
            (over all(>=(object_function) 2))
        )
        :effect (and
            (at end(increase (object_function) (efficiency)))
            (at end (not(active ?obj)))
            (at end (free ?g))
            (at end (not(is_holding ?g ?obj)))
            (at end (object-at ?obj ?wp))
            (at end (can_move ?v))
        )
    )
    (:durative-action packaging
        :parameters (?obj - object ?wp - waypoint )
        :duration (= ?duration 6)
        :condition (and
            (at start(requires-packaging ?obj))
            (over all(object-at ?obj ?wp))
        )
        :effect (and
            (at start(assign (object_function) 0))
            (at start(assign (efficiency) 1))
            (at end(assign (efficiency) 0))
            (at end (active ?obj))
            (at end (packaged-at ?obj ?wp))
            (at end (not(requires-packaging ?obj)))
        )
    )
    
)
