# bounce.py

starting_height = 100
height_loss_mult = 0.6
bounces_to_show = 10
digits_to_show = 4

height = starting_height

for i in range(1, bounces_to_show + 1):
    height *= height_loss_mult
    print(i, round(height, ndigits=digits_to_show))
