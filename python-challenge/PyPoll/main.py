# Creat file paths
import os
# read csv files
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

#lists to store data
total_votes = 0
poll_data = {}
unique_candidates= []
candidate_votes = []
candidate_votes_percentage = []

# open file as csv
with open(csvpath, newline='') as csvfile:
	# reading csv as object
	csvreader = csv.reader(csvfile,delimiter = ',') 
	next(csvreader)
 	
 	# reading csv as lists/rows
	for row in csvreader:

 		# calculate the total number of votes
 		total_votes += 1

 		# create dictionary of candidates and votes
 		if row[2] in poll_data.keys():
 			poll_data[row[2]] += 1
 		else:
 			poll_data[row[2]] = 1

# create lists off of dictionary
for candidate, votes in poll_data.items():
	unique_candidates.append(candidate)
	candidate_votes.append(votes)

# convert votes to percentage
for votes in candidate_votes:
	candidate_votes_percentage.append(round((votes/total_votes)*100,4))

# combine the data into one list 
combined_data = list(zip(unique_candidates,candidate_votes))

# find the winner
winner = combined_data[candidate_votes.index(max(candidate_votes))][0]

# print data
print('Election Results')
print('--------------------------------')
print(f'Total Votes: {total_votes}')
print('--------------------------------')
print(f'{unique_candidates[0]}: {candidate_votes_percentage[0]}% ({candidate_votes[0]})')
print(f'{unique_candidates[1]}: {candidate_votes_percentage[1]}% ({candidate_votes[1]})')
print(f'{unique_candidates[2]}: {candidate_votes_percentage[2]}% ({candidate_votes[2]})')
print(f'{unique_candidates[3]}: {candidate_votes_percentage[3]}% ({candidate_votes[3]})')
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')


final_data_poll = os.path.join('..','PyPoll', 'final_data_poll.txt')

with open(final_data_poll,'w') as textfile:

	textfile.write('Election Results')
	textfile.write('--------------------------------')
	textfile.write(f'Total Votes: {total_votes}')
	textfile.write('--------------------------------')
	textfile.write(f'{unique_candidates[0]}: {candidate_votes_percentage[0]}% ({candidate_votes[0]})')
	textfile.write(f'{unique_candidates[1]}: {candidate_votes_percentage[1]}% ({candidate_votes[1]})')
	textfile.write(f'{unique_candidates[2]}: {candidate_votes_percentage[2]}% ({candidate_votes[2]})')
	textfile.write(f'{unique_candidates[3]}: {candidate_votes_percentage[3]}% ({candidate_votes[3]})')
	textfile.write('--------------------------------')
	textfile.write(f'Winner: {winner}')
	textfile.write('--------------------------------')
