# Paint Area Calculator

def function(h, w, c):
    num_of_cans = round((h * w) / c)
    print(f"{num_of_cans} cans required")

height = int(input("Enter the height"))
width = int(input("Enter the width"))
coverage = int(input("Enter the total coverage"))
function(h=height, w= width, c = coverage)
