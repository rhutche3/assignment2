import data
import cashier
import sandwich_maker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)#####
cashier_instance = cashier.Cashier()######


def main():
    size = input("What size sandwhich would you like (small/medium/large)?: ").lower()

    if size in recipes:
        ingredients = recipes[size]["ingredients"]
        cost = recipes[size]["cost"]

        if sandwich_maker_instance.check_resources(ingredients):
            print(f"Your {size} sandwich will cost: ${cost:.2f}")

            coins_inserted = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins_inserted, cost):
                sandwich_maker_instance.make_sandwich(size, ingredients)
                print(f"Here is your {size} sandwich! Enjoy!")
            else:
                print("Sorry, that is not enough money.")
        else:
            print(f"Sorry, not enough ingredients for a {size} sandwich.")
    else:
        print("Invalid sandwich size. Please select from small/medium/large.")

if __name__=="__main__":
    main()
