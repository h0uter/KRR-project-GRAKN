# KRR-project

## requirements
- tested on python 3.7.6
  - grakn-client (`pip3 install grakn-client`)
- Java Runtime Environment 11 required for GRAKN server and console
- GRAKN 2.0 -> unzipped in the root of this repo

## How to Run

### option A: all in one shell script
assuming all files are in ro47014_ws:

edit the directory of the singularity image in RUNME_TO_START_DEMO.sh (it needs to be changed in 3 locations)

run the `RUNME_TO_START_DEMO.sh` shell script from the terminal.

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


### option B: manual
to start the grakn server run `./grakn server` from the root

to setup the knowledge base start the grakn console with `./grakn console` and run the following commmands:

TO CREATE DATABASE
```
database create KRR
```

TO WRITE SCHEMA
```
transaction KRR schema write
source KRR_grakn/KRR_schema.gql
commit
```

TO LOAD DATASET 
```
transaction KRR data write
source KRR_grakn/KRR_data.gql
commit
```

Now we can run the python file `KRR_kb_interface.py` to input a new product or select a product and generate pddl code base based on it.

after that start the simulation as usual

## info
the data aka instances are contained in `KRR_data.gql`

the ontology is contained in `KRR_schema.gql`

 