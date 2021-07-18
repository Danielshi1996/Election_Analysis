import datetime as dt
import csv
import os
# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    header = next(file_reader)

    print(header)
    # for row in file_reader:
    #     print(row)


#     reader = csv.reader(election_data)

#     header = next(reader)

#     print(header)

#     candidates = []

#     total = 0

#     for row in reader:

#         total += 1
#         if row[2] not in candidates:

#             candidates.append(row[2])

#     print(candidates)
#     print(total)


# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as outfile:

#     outfile.write("Arapahoe,")
#     outfile.write("Denver,")
#     outfile.write("Jefferson")
