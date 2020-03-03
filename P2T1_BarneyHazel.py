#Write a program that ask the user to enter projected total sales then will display the profit that'll be made from that amount.
#February 20th, 2020
#CTI-110 P2T1-Sales Prediction
#Hazel Barney
#Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
