import sys


# finds the most active cookie for the given date
def most_active_cookie(filename, target_date):
    # open the file
    infile = open(filename, 'r')
    # initializing 2 dictionaries to store and keep track of data
    dates = {}
    track = {}
    # skipping the first line
    infile.readline().strip()
    line1 = infile.readline().strip()
    # reading the file
    while line1 != "":
        # split the line to get the necessary strings
        cookie, timestamp = line1.split(",")
        date, time = timestamp.split("T")
        # keep a frequency count of cookies in each date
        if date in dates:
            if cookie in dates[date]:
                dates[date][cookie] += 1
            else:
                dates[date][cookie] = 1
        else:
            dates[date] = {cookie: 1}

        # keep a track of the maximum frequency of cookies and the cookies itself
        # for each date
        if date in track:
            if dates[date][cookie] > track[date][0]:
                track[date] = [dates[date][cookie], [cookie]]
            elif dates[date][cookie] == track[date][0]:
                track[date][1].append(cookie)
        else:
            track[date] = [1, [cookie]]
        line1 = infile.readline().strip()

    # close the file
    infile.close()
    return track[target_date][1]


final_answer = most_active_cookie(sys.argv[1], sys.argv[3])
# print the answer
for i in final_answer:
    sys.stdout.write(i + "\n")
