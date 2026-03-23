import sys
import pandas as pd

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)

    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    
    rock_cases = []
    burg_cases = []

    # Make new lists only including dates and the cumulative amount of cases
    for date,county, state, fips, cases, deaths in data:
        if county == 'Rockingham' and state == 'Virginia' and cases > 0:
            rock_cases.append(date)
        if county == 'Harrisonburg city' and state == 'Virginia' and cases > 0:
            burg_cases.append(date)
    
    #Print the earliest/lowest dates in the list of dates.
    print(f'The first positive COVID case in Rockingham County was on {min(rock_cases)}.')
    print(f'The first positive COVID case in Harrisonburg City was on {min(burg_cases)}.')
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    rock_cases = []
    burg_cases = []

    # Make new lists only including dates and the cumulative amount of cases
    for date,county, state, fips, cases, deaths in data:
        if county == 'Rockingham' and state == 'Virginia':
            rock_cases.append([date, cases])
        if county == 'Harrisonburg city' and state == 'Virginia':
            burg_cases.append([date, cases])
    
    # Store the actual amounts of cases found on individual day
    daily_rock = []
    for i in range(1, len(rock_cases)):
        new_cases = rock_cases[i][1] - rock_cases[i-1][1]
        daily_rock.append([rock_cases[i][0], new_cases])

    # Find and print the date for the largest of cases recorded in a single day
    rock_max = max(case[1] for case in daily_rock)
    for case in daily_rock:
        if case[1] == rock_max:
            print(f'The day with the greatest number of new daily cases recorded in Rockingham County was on {case[0]}.')

    # Store the actual amounts of cases found on individual day
    daily_burg = []
    for i in range(1, len(burg_cases)):
        new_cases = burg_cases[i][1] - burg_cases[i-1][1]
        daily_burg.append([burg_cases[i][0], new_cases])

    # Find and print the date for the largest of cases recorded in a single day
    burg_max = max(case[1] for case in daily_burg)
    for case in daily_burg:
        if case[1] == burg_max:
            print(f'The day with the greatest number of new daily cases recorded in Harrisonburg was on {case[0]}.')
        
    return

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in both the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    
    rock_cases = []
    burg_cases = []

    # Make new lists only including dates and the cumulative amount of cases
    for date,county, state, fips, cases, deaths in data:
        if county == 'Rockingham' and state == 'Virginia':
            rock_cases.append([date, cases])
        if county == 'Harrisonburg city' and state == 'Virginia':
            burg_cases.append([date, cases])

    # Store the actual amounts of cases found on individual day
    daily_rock = []
    for i in range(1, len(rock_cases)):
        new_cases = rock_cases[i][1] - rock_cases[i-1][1]
        daily_rock.append([rock_cases[i][0], new_cases])

    # 
    rock_seven = 0
    rock_seven_index = 0
    for i, pair in enumerate(daily_rock):
        # Don't let the index go out of the list
        if pair == daily_rock[len(daily_rock) - 7]:
                break
        total = 0
        # Find total for 7 day ranges and compare them to the previously highest
        for num in range(7): 
            total += daily_rock[i + num][1]
        if total > rock_seven:
            rock_seven = total
            rock_seven_index = i

    # Print the saved index date to the date 6 days after
    print(f"The largest amount of cases were from {daily_rock[rock_seven_index][0]} to {daily_rock[rock_seven_index + 6][0]}.")

    # Store the actual amounts of cases found on individual day
    daily_burg = []
    for i in range(1, len(burg_cases)):
        new_cases = burg_cases[i][1] - burg_cases[i-1][1]
        daily_burg.append([burg_cases[i][0], new_cases])

    burg_seven = 0
    burg_seven_index = 0
    for i, pair in enumerate(daily_burg):
        # Don't let the index go out of the list
        if pair == daily_burg[len(daily_burg) - 7]:
            break
        total = 0
        # Find total for 7 day ranges and compare them to the previously highest
        for num in range(7):
            total += daily_burg[i + num][1]
        if total > burg_seven:
            burg_seven = total
            burg_seven_index = i
    
    # Print the saved index date to the date 6 days after
    print(f"The largest amount of cases were from {daily_burg[burg_seven_index][0]} to {daily_burg[burg_seven_index + 6][0]}.")
    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    #for (date,county, state, fips, cases, deaths) in data:
        #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data)


