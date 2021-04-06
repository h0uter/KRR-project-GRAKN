# You need to set the path to the singularity image manually in each terminal command. 
# I tried to find a way to pass it as an argument with the var below, but I could not get it to work :(
# SINGULARITY_PATH=~/KRR

gnome-terminal -- /bin/sh -c '
echo "terminal0: start GRAKN SERVER";
~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/grakn server;
/bin/sh
'

sleep 5

gnome-terminal -- sh -c '
echo "terminal0: start GRAKN console to load schema and data";
~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/grakn console --script=GRAKN_console_script.sh
'

sleep 5

python3 ~/ro47014_ws/src/retail_store_lightweight_sim_students/KRR-project-GRAKN/demo_static.py;

wait

./SET_SING_DEST_HERE_launch_sim.sh