# KRR-project

## requirements
- tested on python 3.7.6
- grakn-client (`pip3 install grakn-client`)
- [Java Runtime Environment 11 required for GRAKN server and console](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html)
- [GRAKN 2.0](https://grakn.ai/download#core) -> unzipped in the root of this repo

## How to Run


### option A: all in one shell script
---
assuming all files are in ro47014_ws:

1. Verify our shell scripts. Once you trust them set execution permissions on all the shell scripts in the `DEMO` folder.
2. Edit the directory of the singularity image in `SET_SING_DEST_HERE_launch_sim.sh` (it needs to be changed in 3 locations)

3. Run the `RUNME_TO_START_INTERACTIVE_DEMO.sh` shell script from the terminal.

What will happen then:
1. The grakn server will start
2. The grakn console will start and the schema and data will be loaded
3. The python GRAKN-PDDL inteface is launched !!!IN THE ORIGINAL TERMINAL!!!
    1. Answer if you want to add a new product
    2. Answer nr of items in simulation
    3. Answer name of items
    4. Answer name of aruo cube corresponding to item -> PDDL will be generated
4. The simulation is launched
5. The planner is launched
6. The plan executor is launched


There is also the `RUNME_TO_START_STATIC_DEMO.sh` demo.
This file does the above with the following presets.
- product `kip1` is added to KB with product group `freezer_product`
- 3 products are assigned in the sim
  - `kroket1` to `aruco_cube_222`
  - `hagelslag1` to `aruco_cube_444`  
  - `kip1` to `aruco_cube_582`


### option B: manual
---
To start the grakn server run `./grakn server` from the root

To setup the knowledge base start the grakn console with `./grakn console` and run the following commmands:

TO CREATE DATABASE
```
database create KRR
```

TO WRITE SCHEMA
```
transaction KRR schema write
source KRR_grakn_ontology/KRR_schema.gql
commit
```

TO LOAD DATASET 
```
transaction KRR data write
source KRR_grakn_ontology/KRR_data.gql
commit
```

Now we can run the python file `PDDL_GRAKN_interface.py` to input a new product or select a product and generate pddl code base based on it. BECAUSE OF THE RELATIVE PATH IN pddl_generator.py THE INTERFACE HAS TO BE RAN FROM THE DEMO FOLDER

After that start the simulation with `SET_SING_DEST_HERE_launch_sim.sh`

## info
the data aka instances are contained in `KRR_data.gql`

the ontology is contained in `KRR_schema.gql`

 