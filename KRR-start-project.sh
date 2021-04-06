# You need to set the path to the singularity image manually in each terminal command. 
# I tried to find a way to pass it as an argument with the var below, but I could not get it to work :(
# SINGULARITY_PATH=~/KRR

# gnome-terminal -- /bin/sh -c '
# echo "terminal0: start GRAKN SERVER";
# ~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/grakn server;
# /bin/sh
# '

# sleep 5

# gnome-terminal -- sh -c '
# echo "terminal0: start GRAKN console to load schema and data";
# ~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/grakn console --script=GRAKN_console_script.sh
# '

# sleep 5

# python3 ~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/KRR_kb_interface.py;

# wait

# gnome-terminal -- /bin/sh -c '
# echo "terminal1: Python GRAKN-PDDL interface";
# python3 ~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/KRR_kb_interface.py;
# "' 

# FIX SINGULARITY_PATH=~/KRR BELOW
gnome-terminal -- /bin/sh -c '
echo "terminal2: start simulation environment";
singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
source ~/ro47014_ws/devel/setup.bash;

cd ~/ro47014_ws/src/retail_store_lightweight_sim_students/retail_store_planning/;
roslaunch retail_store_simulation tiago_simulation.launch world:=multiple_cubes use_aruco:=false;
/bin/sh
"'

# sleep 5

# # FIX SINGULARITY_PATH=~/KRR BELOW
# gnome-terminal -- /bin/sh -c '
# echo "terminal3: launch planner";
# singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
# source ~/ro47014_ws/devel/setup.bash;

# roslaunch retail_store_planning rosplan_pick_place.launch;
# /bin/sh
# "'

# sleep 5

# # FIX SINGULARITY_PATH=~/KRR BELOW
# gnome-terminal -- /bin/sh -c '
# echo "terminal4: plan executor";
# singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
# source ~/ro47014_ws/devel/setup.bash;

# ~/ro47014_ws/src/retail_store_lightweight_sim_students/retail_store_planning/rosplan_executor.bash;
# /bin/sh
# "'

