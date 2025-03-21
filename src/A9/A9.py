def food_recommendation(user_preferences, food_data):
    """
    Recommends food items based on user preferences.

    Args:
        user_preferences: A dictionary of user preferences (e.g., {"cuisine": "Italian", "dietary_restrictions": ["vegetarian"]}).
        food_data: A list of dictionaries representing food items.
    Returns:
        A list of recommended food items (dictionaries).
    """

    recommendations = []

    for food in food_data:
        match = True  # Assume a match until proven otherwise

        # Check cuisine preference
        if "cuisine" in user_preferences and user_preferences["cuisine"].lower() != food["cuisine"].lower():
            match = False

        # Check dietary restrictions
        if "dietary_restrictions" in user_preferences:
            for restriction in user_preferences["dietary_restrictions"]:
                if restriction.lower() in food["dietary_restrictions"]:
                    pass #restriction is met
                else:
                    match = False
                    break # if any restriction is not met, break

        if match:
            recommendations.append(food)

    return recommendations

# Sample food data (list of dictionaries)
food_data = [
    {
        "name": "Pasta Primavera",
        "cuisine": "Italian",
        "dietary_restrictions": ["vegetarian"],
        "rating": 4.5,
        "ingredients": ("pasta", "vegetables", "sauce")
    },
    {
        "name": "Chicken Tikka Masala",
        "cuisine": "Indian",
        "dietary_restrictions": [],
        "rating": 4.8,
        "ingredients": ("chicken", "spices", "yogurt")
    },
    {
        "name": "Vegetable Curry",
        "cuisine": "Indian",
        "dietary_restrictions": ["vegetarian", "vegan"],
        "rating": 4.2,
        "ingredients": ("vegetables", "spices", "coconut milk")
    },
    {
        "name": "Pizza Margherita",
        "cuisine": "Italian",
        "dietary_restrictions": ["vegetarian"],
        "rating": 4.6,
        "ingredients": ("dough", "tomato sauce", "mozzarella")
    },
    {
        "name": "Beef Stir-fry",
        "cuisine": "Chinese",
        "dietary_restrictions": [],
        "rating": 4.0,
        "ingredients": ("beef", "vegetables", "soy sauce")

    }
]

# Sample user preferences (dictionary)
user_preferences = {
    "cuisine": "Italian",
    "dietary_restrictions": ["vegetarian"]
}

# Get recommendations
recommended_foods = food_recommendation(user_preferences, food_data)

# Display recommendations
if recommended_foods:
    print("Recommended foods:")
    for food in recommended_foods:
        print(f"- {food['name']} ({food['cuisine']}), Rating: {food['rating']}")
else:
    print("No matching foods found.")

#Example of a user with no restrictions or cuisine preference.
user_preferences_2 = {}
recommended_foods_2 = food_recommendation(user_preferences_2, food_data)

if recommended_foods_2:
    print("\nRecommended foods for user without preferences:")
    for food in recommended_foods_2:
        print(f"- {food['name']} ({food['cuisine']}), Rating: {food['rating']}")
else:
    print("No matching foods found.")

#Example of a user with a vegan restriction.
user_preferences_3 = {"dietary_restrictions": ["vegan"]}
recommended_foods_3 = food_recommendation(user_preferences_3, food_data)

if recommended_foods_3:
    print("\nRecommended foods for vegan user:")
    for food in recommended_foods_3:
        print(f"- {food['name']} ({food['cuisine']}), Rating: {food['rating']}")
else:
    print("No matching foods found.")