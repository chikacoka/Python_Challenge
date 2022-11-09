# This will allow us to create file paths across operating systems
import os
import csv

# Module for reading CSV files
#import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
# csvpath = '/Users/markamanfu/coding-boot-camp/DataViz-Lesson-Plans/01-Lesson-Plans/03-Python/2/Activities/08-Ins_ReadCSV/Resources/contacts.csv'

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

# Method 2: Improved Reading using CSV module

month_count=0
profit_loss = 0
net_total_amount_of_profit = 0
total_profit_loss_change = 0
greatest_increase_in_profit = 0





with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        month_count+=1
        profit_loss= int(row[1])
        net_total_amount_of_profit = net_total_amount_of_profit + profit_loss
        previous_profit_loss =int(row[1])
        total_profit_loss_change = int(row[1]) -previous_profit_loss
        
        if total_profit_loss_change > greatest_increase_in_profit

        
        #if profit_loss_change - profit_loss == 0:
        #else: profit_loss_change = profit_loss_change + profit_loss
    


    print(month_count)
    print(net_total_amount_of_profit)
    print(total_profit_loss_change)

# Total Number of Months


    
#print(months)
    # for month in months:
    # months += month 



# #total_no_of_months = len(months)


# #def total_no_of_months(months):
#     month = str([0])
#     total_no_of_months=0
#     for month in months:
#         total_no_of_months += month
#     return total_no_of_months






# def net_total_amount_of_profit(profit_data):
#     profit_loss = int(profit_data[1])
#     net_total_amount_of_profit = 0
#     net_total_amount_of_profit +=profit_loss


# # Changes in Profit

# profit_loss = int(profit_data[1])



