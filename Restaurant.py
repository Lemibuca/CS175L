
# CS 175L 
# LESLIE BUSTAMANTE
# RESTAURANT ASSIGNMENT
vegetarian = input('Is anyone in your party vegetarian? ')
vegan = input('Is anyone in your party vegan? ')
gluten_free = input('Is anyone in your party gluten-free? ')

print("\nHere are your restaurant choices:")

if vegetarian == "no" and vegan == "no" and gluten_free == "no":
    print("\nJoe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "yes" and vegan == "no" and gluten_free == "no":
    print("\nMama's Fine Italian")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "no" and vegan == "no" and gluten_free == "yes":
    print("\nMain Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "yes" and vegan == "no" and gluten_free == "yes":
    print("\nMain Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "no" and vegan == "yes" and gluten_free == "no":
    print("\nCorner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "no" and vegan == "yes" and gluten_free == "yes":
    print("\nCorner Cafe")
    print("The Chef's Kitchen")
elif vegetarian == "yes" and vegan == "yes" and gluten_free == "no":
    print("\nCorner Cafe")
    print("The Chef's Kitchen")
else: 
    print("\nCorner Cafe")
    print("The Chef's Kitchen")

