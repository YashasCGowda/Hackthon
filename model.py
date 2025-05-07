def predict_reduction_suggestions(emissions):
    # Validate input
    if not isinstance(emissions, dict) or 'breakdown' not in emissions:
        return ["Invalid emissions data. Please provide a breakdown."]

    breakdown = emissions["breakdown"]
    if not breakdown or not all(key in breakdown for key in ["transport", "energy", "diet"]):
        return ["Breakdown must include transport, energy, and diet categories."]

    # Find the category with the highest emissions
    max_value = max(breakdown.values())
    max_categories = [category for category, value in breakdown.items() if value == max_value]
    # If there's a tie, prioritize transport > energy > diet
    max_category = max_categories[0] if len(max_categories) == 1 else (
        "transport" if "transport" in max_categories else
        "energy" if "energy" in max_categories else "diet"
    )

    suggestions = []

    if max_category == "transport":
        suggestions.extend([
            "Consider using public transportation or carpooling.",
            "Switch to an electric vehicle if possible."
        ])
    elif max_category == "energy":
        suggestions.extend([
            "Switch to energy-efficient appliances.",
            "Use renewable energy sources like solar power."
        ])
    elif max_category == "diet":
        suggestions.extend([
            "Reduce meat consumption and try plant-based meals.",
            "Support local and sustainable food sources."
        ])

    return suggestions  # Already limited to 2 suggestions per category