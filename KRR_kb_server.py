from grakn.client import *

with Grakn.core_client("localhost:1729") as client:
    with client.session("KRR", SessionType.DATA) as session:
      
        # ## Insert a Person using a WRITE transaction
        # with session.transaction(TransactionType.WRITE) as write_transaction:
        #     insert_iterator = write_transaction.query().insert(
        #         'insert $x isa person, has $email "x@email.com";')
        #     concepts = [ans.get("x") for ans in insert_iterator]
        #     print("Inserted a person with ID: {0}".format(
        #         concepts[0].get_iid()))
        #     ## to persist changes, write transaction must always be committed (closed)
        #     write_transaction.commit()

        ## Read the person using a READ only transaction
        with session.transaction(TransactionType.READ) as read_transaction:
            answer_iterator = read_transaction.query().match(
                "match $prod1 isa product, has name 'kroket', has storage_type $st; get $st;")

            for answer in answer_iterator:
                print(answer)
                product = answer.get("st")
                print(product)
                print("Retrieved product storage loc " + product.get_value())

        # ## Or query and consume the iterator immediately collecting all the results
        # with session.transaction(TransactionType.READ) as read_transaction:
        #     answer_iterator = read_transaction.query().match(
        #         "match $x isa person; get $x; limit 10;")
        #     persons = [ans.get("x") for ans in answer_iterator]
        #     for person in persons:
        #         print("Retrieved person with id " + person.get_iid())

        ## if not using a `with` statement, then we must always close the session and the read transaction
        # read_transaction.close()
        # session.close()
        # client.close()
