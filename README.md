KRR-project

# requirements
- tested on python 3.7.6
- Java Runtime Environment 11 required for GRAKN server and console
- GRAKN 2.0 

# how to run
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

# info
the data aka instances are contained in `KRR_data.gql`

the ontology is contained in `KRR_schema.gql`

 