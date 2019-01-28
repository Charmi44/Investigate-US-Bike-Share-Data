import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_city():

    cities = ['chicago', 'new york city','washington']

    print('Hello! Let\'s explore some US bikeshare data!')


    while True:
        try:
            city_choice = str(input('\nSo, what city would you like to explore?! Chicago, New York City, or Washington:\n'))
        # To handle value error
        except ValueError:
            print("{} wis not valid".format(city_choice))
            continue
        # If entered city is not in the given list
        if city_choice.lower() not in cities:
            print("{}, is not available".format(city_choice))
            continue
        else:
#           if the input is accepted it will assign he input to 'city'
            city = city_choice.lower()
            break
    return city

def get_filters():
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    filters = ['month', 'day', 'both','none']

    print("\nHow would you like to filter this data?")
    while True:
        try:
            filter_choice = str(input('\nYou can filter by month, day , both or not at all. If you want to filter by both type "both", If you want no filter, type "none":\n'))
	# to handle value error
        except ValueError:
            print("{} is not valid input".format(filter_choice))
            continue
        # If entered filter is not in the given list
        if filter_choice.lower() not in filters:
            print("{}, is not valid".format(filter_choice))
            continue
        else:
            break
    # if user select to filter by month, below code will ask which month you look for
    if filter_choice.lower() == 'month':

        while True:
            try:
	        # To handle value error
                month_choice = str(input('\nWhich month you want, between January to June! Enter full name e.g.June:\n'))
            except ValueError:
                print("Enter a full month name please.")
                continue
        # If entered month is not in the given list
            if month_choice.lower() not in months:
                print("{}, is not valid".format(month_choice))
                continue
            # If the input is valid, assign value to month and assign all to day
            else:
                month = month_choice.lower()
                day = 'all'
                break

        print("\nData will be filtered on month of {}\n".format(month.title()))
    # if user wants to filter with day
    elif filter_choice.lower() == 'day':

        while True:
            try:
                day_choice = str(input('\nPlease enter the day. e.g.Sunday:\n'))
	        # To handle value error
            except ValueError:
                print("Enter the full day name please.")
                continue
       	 # If entered day is not in the given list
            if day_choice.lower() not in days:
                print("{}, is not valid".format(day_choice))
                continue
            # If the input is valid, assign value to day and assign all to month
            else:
                day = day_choice.lower()
                month = 'all'
                break

        print("\nData will be filtered on {}\n".format(day.title()))
    elif filter_choice.lower() == 'both':
                month = str(input('\nWhich month you want, between January to June! Enter full name e.g.June:\n')).lower()
                day = str(input('\nPlease enter the day. e.g.Sunday:\n')).lower()

                if month in months and day in days:
                    print("*" * 40)


    # if user choose not to apply any filter
    else:
        print('\nNo filters will be applied to your data')
        # if no filters it will show all days and months
        day = 'all'
        month = 'all'


    return  filter_choice, month, day

def load_data(city, filter_choice, month, day):

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # this will turn the trip duration (currently in seconds) into minutes
    df['Trip_Dur_Mins'] = df['Trip Duration'] / 60

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month :',df['month'].mode().loc[0])

    # TO DO: display the most common day of week
    print('most common day :',df['day_of_week'].mode().loc[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('most common start hour :',df['hour'].mode().loc[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most common start station :',df['Start Station'].mode().loc[0])

    # TO DO: display most commonly used end station
    print('most common end station :',df['End Station'].mode().loc[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df['Start Station']+' To '+df['End Station']

    print('most_frequent_trip :',most_frequent_trip.mode().loc[0])

 	
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time in minutes :',df['Trip Duration'].sum())
 
    # TO DO: display mean travel time
    print('Mean travel time in minutes :',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
  if city =='washington':
         print('\nCalculating User Stats...\n')
         print('User data not available')
      
  else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        print('Counts of user Types :\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
        print('Counts of Gender :\n',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest Birth Year :',df['Birth Year'].min())
        print('Most Recent Birth Year :',df['Birth Year'].max())
        print('Most Common Birth Year :',df['Birth Year'].mode().loc[0])
        #print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    raw_data_options = ['yes','no']


    while True:
        try:
            raw_data_input = str(input('\nWould you like to see some raw data without any filters applied? (yes/no) \n'))

        except ValueError:
            print("{} is not a valid selection".format(raw_data_input))
        # if user selection is not proper
        if raw_data_input.lower() not in raw_data_options:
            print("{}, is not valid selection".format(raw_data_input))
            continue

        # this will loop until 'no' is entered
        elif raw_data_input.lower() == 'yes':
        # To select random line of data
            df_1 = df.sample(n=5)
            print(df_1)
            continue
        # if 'no' is chosen the script will stop
        else:
            print("We will exit now.Thank you.")
            break        
def main():
    while True:
        city = get_city()
        filter_choice, month, day = get_filters()
        df = load_data(city, filter_choice, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

