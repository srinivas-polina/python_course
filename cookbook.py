# I am importing recipes list from recipes.py
from recipes import recipes

# I am defining a function to list all recipes
def list_recipes():
    # I am looping through each recipe and printing its name
    for recipe in recipes:
        print(recipe["name"])

# I am defining a function to search recipes by name
def query_recipes():
    # I am taking recipe name input from the user
    name = input("Enter recipe name: ").strip().lower()

    # I am creating an empty list to store matched recipes
    found = []

    # I am looping through recipes
    for r in recipes:
        # I am converting recipe name to lowercase
        recipe_name_lower = r["name"].lower()

        # ✅ this must be INSIDE the loop
        if name in recipe_name_lower:
            found.append(r)

    # ✅ this must be INSIDE the function
    if not found:
        print("No matching recipes found.")
        return

    # I am printing each matched recipe details
    for r in found:
        ingredients = []
        for i in r["ingredients"]:
            ingredients.append(i["name"])

        print("\nRecipe:", r["name"])
        print("Ingredients:", ", ".join(ingredients))
        print("Instructions:")
        for step in r["instructions"]:
            print("-", step)

# I am defining a function to search recipes by ingredients
def find_by_ingredients():
    # I am taking ingredients input from the user
    items = input("Enter ingredients (comma-separated): ")

    # ✅ spelling: available (not avalible)
    available = []
    for x in items.split(","):
        if x.strip():
            available.append(x.strip().lower())

    # I am storing matched recipes here
    matches = []

    # I am looping through each recipe
    for r in recipes:
        recipe_ings = []
        for i in r["ingredients"]:
            recipe_ings.append(i["name"].lower())

        all_present = True
        for a in available:
            if a not in recipe_ings:
                # ✅ spelling: False (not Flase)
                all_present = False
                break

        if all_present:
            matches.append(r)

    # ✅ this must be INSIDE the function
    if matches:
        print("You can make:")
        for r in matches:
            print("-", r["name"])
    else:
        print("No recipes found with those ingredients.")

# I am defining the main menu function
def main():
    while True:
        print("\n1) List recipes")
        print("2) Search by name")
        print("3) Search by ingredients")
        print("4) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            list_recipes()
        elif choice == "2":
            # ✅ function name should match: query_recipes()
            query_recipes()
        elif choice == "3":
            # ✅ you must CALL the function using ()
            find_by_ingredients()
        elif choice == "4":
            break
        else:
            print("Invalid Choice")

# ✅ this block must be OUTSIDE main() and must have :
if __name__ == "__main__":
    main()
