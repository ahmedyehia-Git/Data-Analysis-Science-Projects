import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # use lower to avoid case sensitivity error 
    city = input('Please enter the city name (chicago, new york city, washington): ').lower()
    
    while city not in ['chicago', 'new york city', 'washington']:
        print('Invalid city name!')
        city = input('Please enter valid city name: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
      
    month = input('Please enter the month name (all, january, february, march, april, may, june): ').lower()
    
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('Invalid month name!')
        month = input('Please enter valid month name: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the weekday (all, saturday, sunday, monday, tuesday, wednesday, thursday, friday): ').lower()
    while day not in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        print('Invalid weekday name!')
        day = input('Please enter valid weekday name: ').lower()
        
    print('-'*40)
    return city, month, day

 
# print(get_filters()), (this is used to test the function)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Reading csv file of selected city
    df = pd.read_csv(CITY_DATA[city])
    
    # converting the start time column to date
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and week day name form converted 'Start Time' and create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # apply month filter
    if month != 'all':
        df = df[df['month'] ==  month.title()]

    # apply day of week filter
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # we will display the first mode value not all list if any!
    
    print('The most common month is: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    # Then cadisply most common week day
    
    print(' The most common week day is: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    # Extract hours from 'Start Time' then create nw column for hour first
    # Then cadisply most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: ', df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most common end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    # Create new column that combine the start station and end station
    # Then we can know the most frequent trip using mode()
    df['Trips'] = df['Start Station'] + ' to ' + df['End Station']
    print('The most common trip is: ', df['Trips'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # using sum() to get the total travel suration in seconds
    print('The total travel time is: ', df['Trip Duration'].sum(),' seconds')

    # TO DO: display mean travel time
    # using mean() to get the avarage trip duration in seconds
    print('The avarage trip duration is: ', df['Trip Duration'].mean(),' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user typesc
    # value_counts() return the count of uniq values 
    print('The user type count: \n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # using try/except to check if 'Gender' column is there, if yes it will do counts...
    # if not it will give message and code will not stop
    try:
        print('The gender count: \n', df['Gender'].value_counts())
    except:
        print('There is no gender data!')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The youngest user born in: ', df['Birth Year'].max())
        print('The oldest user born in: ', df['Birth Year'].min())
        print('The most common users birth year is: ', df['Birth Year'].mode()[0])
    except:
        print('There is no birth year data!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(city):
    """Displays sample of raw data."""
    print('\n.Displays sample of raw data..\n')
        
    # Ask user if he need to see sample of raw data
    # if user response 'yes' read the data file of selected city
    # print 5 rows of the raw data
    # ask user if he need more raw data
    # if user response other than 'yes' the function will break
    rdata = input('Do you want to see sample of raw data? ')
    if rdata.lower() == 'yes':
        df=pd.read_csv(CITY_DATA[city])
        print(df.sample(n=5))
        print('-'*40)
        raw_data(city)
    
      
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
