from grakn.client import *

from PDDL_generation import *

def write_to_KB(product_name, product_type):
    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA) as session:

            ## Insert a Person using a WRITE transaction
            with session.transaction(TransactionType.WRITE) as write_transaction:
                insert_iterator = write_transaction.query().insert(
                    f'insert $prod isa {product_type}, has name "{product_name}";')
                concepts = [ans.get("prod") for ans in insert_iterator]
                # print("Inserted a product with name: {0}, and storage type: {1}".format(
                #     concepts[0].get_value(), concepts[0].get("st")))
                print("Inserted a product")
                ## to persist changes, write transaction must always be committed (closed)
                write_transaction.commit()

def read_from_KB(product_name):

    # option to enable inferrence
    opt = GraknOptions.core()
    opt.infer = True

    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA, opt) as session:

            ## Read the person using a READ only transaction
            with session.transaction(TransactionType.READ) as read_transaction:

                answer_iterator = read_transaction.query().match(f"match $prod1 isa product, has name '{product_name}', has storage_type $st, has needs_packaging $np; get $st, $np;")

                for answer in answer_iterator:
                    # print(answer)
                    storage_type = answer.get("st")
                    needs_packaging = answer.get("np")
                    # print(product.get_value())
                    print(product_name, "is stored in/on the: ",  storage_type.get_value(), "| needs_packaging?: ", needs_packaging.get_value())
                    return storage_type.get_value(), needs_packaging.get_value()


def read_all_products_in_KB():
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


def interactive_demo_run():
    # list all products in the KB
    print("All the products currently in the knowledgebase are:")
    read_all_products_in_KB()

    # ask user input
    new_product_yes_no = input("Do you want to add a new product? (y/n): ")

    if new_product_yes_no == "y":
        new_product_name = input("What is the name of the new product?: ")
        new_product_type = input(
            "What is the product group of the new product? (regular_product/freezer_product/fresh_product): ")

        write_to_KB(new_product_name, new_product_type)
        print("All the products currently in the knowledgebase are:")
        read_all_products_in_KB()

    iterations = input("how many items are in the simulation? (int) :")

    product_names = []
    simulation_names = []
    storage_locations = []
    packaging_bools = []
    for i in range(int(iterations)):
        print("for product", (i + 1),":")

        product_name = input("What is the name of product " + str(i+1) + "?: ")

        storage_type, needs_packaging = read_from_KB(product_name)
        storage_locations.append(storage_type)
        packaging_bools.append(needs_packaging)
    	        
        cube_number = input("Which cube number do you want to assign to the product? (111, 222, 333, 444, 582):")
        simulation_name = "aruco_cube_" + cube_number 

        product_names.append(product_name)
        simulation_names.append(simulation_name)

    generate_pddl(product_names, simulation_names, storage_locations, packaging_bools)


def static_demo_run():
    # list all products in the KB
    print("All the products currently in the knowledgebase are:")
    read_all_products_in_KB()

    # ask user input
    # new_product_yes_no = input("Do you want to add a new product? (y/n): ")
    new_product_yes_no = "y"

    if new_product_yes_no == "y":
        # new_product_name = input("What is the name of the new product: ")
        new_product_name = "kip1"

        # new_product_type = input(
        #     "What is the product group of the new product? (regular_product/freezer_product/fresh_product): ")
        group_of_new_product = "freezer_product"

        write_to_KB(new_product_name, group_of_new_product)
        # write_to_KB(new_product_name, new_product_type)
        print("All the products currently in the knowledgebase are:")
        read_all_products_in_KB()

    # iterations = input("how many items are in the simulation? (int) :")
    iterations = 3

    product_names = []
    simulation_names = []
    storage_locations = []
    packaging_bools = []
    for i in range(int(iterations)):
        print("for product", (i + 1),":")

        # product_name = input("What is the name of the product: ")
        debug_products = ["kroket1", "hagelslag1", "kip1"]
        product_name = debug_products[i]

        storage_type, needs_packaging = read_from_KB(product_name)
        storage_locations.append(storage_type)
        packaging_bools.append(needs_packaging)
    	        
        # simulation_name = input("What is the of the simulated item (e.g. aruco_cube_XXX):")
        debug_simulation_name = ["aruco_cube_222", "aruco_cube_444", "aruco_cube_582"]
        simulation_name = debug_simulation_name[i]

        product_names.append(product_name)
        simulation_names.append(simulation_name)

    generate_pddl(product_names, simulation_names, storage_locations, packaging_bools)



# if __name__ == "__main__":
#     # execute only if run as a script

#     static_demo_run()
#     interactive_demo_run()
