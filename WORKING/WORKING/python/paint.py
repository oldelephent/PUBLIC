#SOLOLEARN PAIN BOX PROBLEM

#My answer get 
total_box_paint = int(input())
each_paint = int(5.0)
total_paint_price = total_box_paint * each_paint
canvas_brushes = int(40.00)
wihtout_tax_price =  canvas_brushes + total_paint_price
tax_calculation = wihtout_tax_price/100*10
final_price_with_tax = tax_calculation + wihtout_tax_price
print(int(final_price_with_tax))

# ANSWER THAT WORKED
# import math
# supplies = 40.00
# paint = int(input())*5
# tax = (supplies + paint)*0.1
# total = (supplies + paint) + tax
# print(int(math.ceil(total)))

# canvas_brushes = 40.00
# each_paint = 5.0
# store_tax = 10%
# total_colour = 10

# input = 10
# output = 99

# store_tax = 10

# percent = 10*100/100
