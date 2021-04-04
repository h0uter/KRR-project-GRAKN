from grakn.client import *


def read_from_KB(product_name):
    with Grakn.core_client("localhost:1729") as client:
        with client.session("KRR", SessionType.DATA) as session:

            ## Read the person using a READ only transaction
            with session.transaction(TransactionType.READ) as read_transaction:

                answer_iterator = read_transaction.query().match(
                    f"match $prod1 isa product, has name '{product_name}', has storage_type $st; get $st;")

                for answer in answer_iterator:
                    # print(answer)
                    product = answer.get("st")
                    # print(product.get_value())
                    print(product_name, "is stored in/on the: " +
                          product.get_value())
                    return product.get_value()


if __name__ == "__main__":

  product_name = 'cola1'

  # GraknOptions.core({"infer": True})
  opt = GraknOptions.core()
  opt.infer = True
  print(opt.infer)


  with Grakn.core_client("localhost:1729") as client:
    with client.session("KRR", SessionType.DATA, opt) as session:

      ## Read the person using a READ only transaction
      # with session.transaction(TransactionType.READ, GraknOptions.core({"infer": True, "explain": True})) as read_transaction:
      with session.transaction(TransactionType.READ) as read_transaction:

        # answer_iterator = read_transaction.logic().getRule(String "drink-never-in-freezer")
        # print(read_transaction.as_remote(read_transaction))

        answer_iterator = read_transaction.query().match(
          f"match $prod isa product, has name '{product_name}', has storage_type $st; get $st;")

        print("hi")

        for answer in answer_iterator:
          print(answer)
          product = answer.get("st")
          # print(product.get_value())
          print(product_name, "is stored in/on the: " +
                product.get_value())
          # return product.get_value()

