mood_color = {
    "happy": "yellow",
    "sad": "blue",
    "angry": "red",
    "stressed": "blue",
    "relaxed": "green",
    "romantic": "pink",
    "confident": "black"
}

color_outfit = {
    "yellow": "yellow t-shirt",
    "blue": "blue hoodie",
    "red": "red jacket",
    "green": "green kurta",
    "pink": "pink top",
    "black": "black suit"
}

mood = input("Enter your mood: ").lower()

if mood in mood_color:
    color = mood_color[mood]
    outfit = color_outfit[color]
    print(f"Your mood is '{mood}'. Wear something {color}, like a {outfit}.")
else:
    print("Mood not recognized. Try another mood.")