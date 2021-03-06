# You need to set the path to the singularity image manually in each terminal command. 
# I tried to find a way to pass it as an argument with the var below, but I could not get it to work :(
# SINGULARITY_PATH=~/KRR

sleep 10

gnome-terminal -- /bin/sh -c '
echo "terminal2: start simulation environment";
singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
source ~/ro47014_ws/devel/setup.bash;

cd ~/ro47014_ws/src/retail_store_lightweight_sim_students/retail_store_planning/;
roslaunch retail_store_simulation tiago_simulation.launch world:=multiple_cubes use_aruco:=false;
/bin/sh
"'

sleep 10

gnome-terminal -- /bin/sh -c '
echo "terminal3: launch planner";
singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
source ~/ro47014_ws/devel/setup.bash;

roslaunch retail_store_planning rosplan_pick_place.launch;
/bin/sh
"'

sleep 15

gnome-terminal -- /bin/sh -c '
echo "terminal4: plan executor";
singularity shell -p --nv ~/KRR/ro47014-20-10-3.simg -c "
source ~/ro47014_ws/devel/setup.bash;

~/ro47014_ws/src/retail_store_lightweight_sim_students/retail_store_planning/rosplan_executor.bash;
/bin/sh
"'
