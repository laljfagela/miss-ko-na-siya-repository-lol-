legend_items = {
    "Player": "[@]",
    "Enemy": "[☠️]",
    "Surprise": "[?]",
    "Tree": "[#]", 
    "Boundary": "[,]", 
}

def display_legend():
    for row in island_map:
        print("\nMap Legends:".join(row))
    for item, symbol in legend_items.items():
        print(f"{item}: {symbol}")

display_legend()
