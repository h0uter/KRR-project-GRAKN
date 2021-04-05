database delete KRR
database create KRR
transaction KRR schema write
source KRR_grakn/KRR_schema.gql
commit
transaction KRR data write
source KRR_grakn/KRR_data.gql
commit