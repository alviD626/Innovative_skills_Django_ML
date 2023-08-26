#list of cakes
c1 = 'Black Forest'
c2 = 'Vanilla cake'
c3 = 'Red Velvet'
c4 = 'Lemon Sponge'
c5 = 'Chocolate Cake'

print('Solve of question no.1\n')
print(f'List to cake flavor:\n1: {c1}\n2: {c2}\n3: {c3}\n4: {c4}\n5: {c5}\n\n')


#list of raw material cost
#raw = raw material
c1_raw = 180
c2_raw = 150
c3_raw = 220
c4_raw = 165
c5_raw = 170

#amount of transport cost
#tp_cost = transport cost
tp_cost = 150

#utility cost is 3% on material and transportation cost
#list utility cost of cakes
percentage = 3/100

#utility = utility cost
c1_utility = (c1_raw + tp_cost) * percentage
c2_utility = (c2_raw + tp_cost) * percentage
c3_utility = (c3_raw + tp_cost) * percentage
c4_utility = (c4_raw + tp_cost) * percentage
c5_utility = (c5_raw + tp_cost) * percentage

#space cost for each pound is 50
space_cost = 50

#staff cost for each pound is 60
staff_cost = 60

#list of inventory cost
#invencost = inventory cost
c1_invencost = c1_raw + c1_utility + tp_cost + space_cost + staff_cost
c2_invencost = c2_raw + c2_utility + tp_cost + space_cost + staff_cost
c3_invencost = c3_raw + c3_utility + tp_cost + space_cost + staff_cost
c4_invencost = c4_raw + c4_utility + tp_cost + space_cost + staff_cost
c5_invencost = c5_raw + c5_utility + tp_cost + space_cost + staff_cost

print('Solve of question no.2\n')
print(f'Inventory cost of cakes:\n1: {c1_invencost}\n2: {c2_invencost}\n3: {c3_invencost}\n4: {c4_invencost}\n5: {c5_invencost}\n\n')


#selling price before discount
#bdis = before discount
c1_bdis = 780
c2_bdis = 600
c3_bdis = 800
c4_bdis = 650
c5_bdis = 660

print('Solve of question no.3\n')
print(f'Selling price before discount:\n1: {c1_bdis}\n2: {c2_bdis}\n3: {c3_bdis}\n4: {c4_bdis}\n5: {c5_bdis}\n\n')

#discount for 1st 3cakes is 5% and 7% for rest of the cakes
# dis = discount
dis1 = 5/100
dis2 = 7/100

#amount of discount
# disamount = discount amount
c1_disamount = 780 * dis1
c2_disamount = 600 * dis1
c3_disamount = 800 * dis1
c4_disamount = 650 * dis2
c5_disamount = 660 * dis2

#amount after getting discount
#famount = final amount
c1_famount = c1_bdis - c1_disamount
c2_famount = c2_bdis - c2_disamount
c3_famount = c3_bdis - c3_disamount
c4_famount = c4_bdis - c4_disamount
c5_famount = c5_bdis - c5_disamount

print('Solve of question no.4\n')
print(f'Selling price after discount:\n1: {c1_famount}\n2: {c2_famount}\n3: {c3_famount}\n4: {c4_famount}\n5: {c5_famount}\n\n')



#total profit = unit price × quantity - unit cost × quantity
#quantities of each cakes
#quant = quantity
c1_quant = 5
c2_quant = 7
c3_quant = 10
c4_quant = 5
c5_quant = 9

#sp = selling price
c1_sp = c1_famount * c1_quant
c2_sp = c2_famount * c2_quant
c3_sp = c3_famount * c3_quant
c4_sp = c4_famount * c4_quant
c5_sp = c5_famount * c5_quant

#cp = cost price
c1_cp = c1_invencost * c1_quant
c2_cp = c2_invencost * c2_quant
c3_cp = c3_invencost * c3_quant
c4_cp = c4_invencost * c4_quant
c5_cp = c5_invencost * c5_quant

# tp = total profit
c1_tp = c1_sp - c1_cp
c2_tp = c2_sp - c2_cp
c3_tp = c3_sp - c3_cp
c4_tp = c4_sp - c4_cp
c5_tp = c5_sp - c5_cp

print('Solve of question no.5\n')
print(f'Total amount of profit for each cake:\n1: {c1_tp}\n2: {c2_tp}\n3: {c3_tp}\n4: {c4_tp}\n5: {c5_tp}\n\n')

#Profit % = (SP-CP) / CP * 100
# difference between sp and cp
c1_diff = c1_sp - c1_cp
c2_diff = c2_sp - c2_cp
c3_diff = c3_sp - c3_cp
c4_diff = c4_sp - c4_cp
c5_diff = c5_sp - c5_cp

# division between difference and cp
c1_div = c1_diff /c1_cp
c2_div = c2_diff /c2_cp
c3_div = c3_diff /c3_cp
c4_div = c4_diff /c4_cp
c5_div = c5_diff /c5_cp

#percentage of profit
c1_profit = c1_div * 100
c2_profit = c2_div * 100
c3_profit = c3_div * 100
c4_profit = c4_div * 100
c5_profit = c5_div * 100

print('Solve of question no.6\n')
print(f'Percentage of profit for each cake:\n1: {c1_profit}\n2: {c2_profit}\n3: {c3_profit}\n4: {c4_profit}\n5: {c5_profit}\n\n')