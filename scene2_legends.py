legend_items = {
    "Player": "[@]",
    "Enemy": "[☠️]",
    "Surprise": "[?]",
    "Tree": "[#]", 
    "Boundary": "[,]", 
    "Room": "R",
    "Wall": "|",
}

def display_legend():
    for row in castle_map:
        print("\nMap Legends:".join(row))
    for item, symbol in legend_items.items():
        print(f"{item}: {symbol}")

display_legend()
