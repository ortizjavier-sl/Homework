# Creat file paths
import os
# read csv files
import csv
# csv file path
csvpath = os.path.join('..','PyBank','budget_data.csv')

#lists to store data
total_months = 0
profit_total = 0
prior_profit = 0
total_monthly_change = []
biggest_loss = 0
biggest_loss_month = 0
biggest_gain = 0
biggest_gain_month = 0


# open file as csv
with open(csvpath, newline = '') as csvfile:

	# reading csv as object
	csvreader = csv.reader(csvfile,delimiter = ',')
	next(csvreader)
	skip_row = next(csvreader)
	total_months += 1
	profit_total += int(skip_row[1])
	prior_profit = int(skip_row[1])
	# reading csv as lists/rows
	for row in csvreader:
		# calculate the total number of months
		total_months += 1

		# calculate total profit/losses
		profit_total += int(row[1])



		# calculating month to month profit/loss in 3 steps
		# 1) calculate profit difference between prior index and next index
		monthly_changes = int(row[1]) - prior_profit

		#3) save all monthly changes to a list
		total_monthly_change.append(monthly_changes)

		# 2) set variable to the last index/profit
		prior_profit = int(row[1])

		average_change = (sum(total_monthly_change)/len(total_monthly_change))

	# find the month associated to the highest and lowest profit
		if int(row[1]) < biggest_loss:
			biggest_loss = int(row[1])
			biggest_loss_month = row[0]

		if int(row[1]) > biggest_gain:
			biggest_gain = int(row[1])
			biggest_gain_month = row[0]
		#mean = round(int(row[1])/ int(len(total_months)),2)

	# find the highest and lowest profit by searching the proper list
	highest_profit = max(total_monthly_change)
	lowest_profit = min(total_monthly_change)


final_total = print(f'Total Months: {total_months}')
print(f'Total: ${profit_total}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {biggest_gain_month} (${highest_profit})')
print(f'Greatest Decrease in Profits: {biggest_loss_month} (${lowest_profit})')


final_data = os.path.join('..','PyBank', 'final_data.txt')

with open(final_data,'w') as textfile:

	textfile.write(f'Total Months: {total_months}')
	textfile.write(f'Total: ${profit_total}')
	textfile.write(f'Average Change: ${round(average_change,2)}')
	textfile.write(f'Greatest Increase in Profits: {biggest_gain_month} (${highest_profit})')
	textfile.write(f'Greatest Decrease in Profits: {biggest_loss_month} (${lowest_profit})')

		#if total < total + int(row[1])
		#print(f'Total Months :{len(list(csvreader))}')
		#print(months_count)
	#if int(list(row[1])) > 0:
			#total = total + int(row[1])
			#print(total)