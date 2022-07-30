'''
Carly's Clippers
You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block.
 Your job is to go through the lists of data that have been collected in the past couple of weeks.
You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.

Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list,
 and was purchased 2 times in the last week as shown in the last_week list.
  Each of these elements are in the first index of their respective lists.
'''

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

print('Available cuts in hair salon:', hairstyles)

prices = [30, 25, 40, 20, 20, 35, 50, 35]

print('Origin price of each hairstyle in the hairstyles list. ', prices)

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
print('the number of purchases for each hairstyle type in the last week:', last_week)

total_price = 0

for price in prices:
  total_price += price
print('Total amount of all prices:', total_price)

average_price = total_price / len(prices)
print('Average Haircut Price:', average_price)

'''

That average price is more expensive than Carly thought it would be! 
She wants to cut all prices by 5 dollars.
let's Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
'''
new_prices = [item - 5 for item in prices]
print('New prices:', new_prices)


'''
 We gonna figure out how much revenue was brought in last week.
 we may use 'range()' function to implement this
'''

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print('Total Revenue', total_revenue)


'''
We nee also to find the average daily revenue by dividing total_revenue by 7. 
let's Call this number average_daily_revenue and print it out.
'''
average_daily_revenue = total_revenue / 7
print('avarage_daily_revenue:', average_daily_revenue)

'''
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.
Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.
You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.
'''

cuts_under_30 = [hairstyles[haircut] for haircut in range(len(hairstyles) - 1)  if new_prices[haircut] < 30]

print('Cuts under 30:', cuts_under_30)



