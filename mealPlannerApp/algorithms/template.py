import random

def generate_mealplan(foods, macros):

    recommendations = []
    for food in foods:
        recommendations.append({
            'name': food.name,
            'amount_to_eat': round(random.uniform(0, 10), 2),
            'units': food.units,
        })

    return recommendations
