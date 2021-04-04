from grakn.client import *

from PDDL_writer_test import *

def write_to_KB(product_name, storage_type):
    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA) as session:

            ## Insert a Person using a WRITE transaction
            with session.transaction(TransactionType.WRITE) as write_transaction:
                insert_iterator = write_transaction.query().insert(
                    f'insert $prod isa product, has name "{product_name}", has storage_type "{storage_type}";')
                concepts = [ans.get("prod") for ans in insert_iterator]
                # print("Inserted a product with name: {0}, and storage type: {1}".format(
                #     concepts[0].get_value(), concepts[0].get("st")))
                print("Inserted a product")
                ## to persist changes, write transaction must always be committed (closed)
                write_transaction.commit()

def read_from_KB(product_name):
    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA) as session:

            ## Read the person using a READ only transaction
            with session.transaction(TransactionType.READ) as read_transaction:

                answer_iterator = read_transaction.query().match(f"match $prod1 isa product, has name '{product_name}', has storage_type $st; get $st;")

                for answer in answer_iterator:
                    # print(answer)
                    product = answer.get("st")
                    # print(product.get_value())
                    print(product_name, "is stored in/on the: " + product.get_value())
                    return product.get_value()


def read_all_from_KB():
    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA) as session:

            ## Read the person using a READ only transaction
            with session.transaction(TransactionType.READ) as read_transaction:

                answer_iterator = read_transaction.query().match(
                    f"match $prod1 isa product, has name $name; get $name;")

                for answer in answer_iterator:
                    # print(answer)
                    product = answer.get("name")
                    # print(product.get_value())
                    print("- " + product.get_value())

if __name__ == "__main__":
    # execute only if run as a script

    # list all products in the KB
    print("All the products currently in the knowledgebase are:")
    read_all_from_KB()

    # ask user input
    new_product_yes_no = input("Do you want to add a new product? (y/n): ")
    # new_product_yes_no = "y"

    if new_product_yes_no == "y":
        new_product_name = input("What is the name of the new product: ")
        # new_product_name = "kip"
        new_product_storage_type = input(
            "What is the storage type of the new product? (shelf/freezer): ")
        # new_product_storage_type = "freezer"

        write_to_KB(new_product_name, new_product_storage_type)


    # TODO: print all objects in the database
    # product_name = input("Enter the product name (brood, kroket, hagelslag): ")
    iterations = input("how many items are in the simulation? (int) :")
    product_names = []
    simulation_names = []
    storage_locations = []
    for i in range(int(iterations)):
    	print("for product", (i + 1),":")
    	product_name = input("What is the name of the product: ")
    	storage_locations.append(read_from_KB(product_name))
    	simulation_name = input("What is the name of the simulated item (e.g. aruco_cube_[number]):")
    	product_names.append(product_name)
    	simulation_names.append(simulation_name)
    # product_name = 'hagelslag'

    


    generate_pddl(product_names, simulation_names, storage_locations)
