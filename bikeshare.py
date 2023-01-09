import time
import pandas as pd
import numpy as np

# used fils for data ignored in github
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
    CChoice=True #to confirm the user choice for city
    while CChoice:
         city = input('\nWhich city would you like to see data on?\nYour choices are: New York City, Washington, Chicago.\n\nYour Choice: ')
         city = city.casefold()
    
         while city not in CITY_DATA:
                city = input('\nThat is not a valid entry. Please try again.\nYour choices are: New York City, Washington, Chicago.\n\nYour Choice: ')
                city = city.casefold()
         CiChoice=input("\nlooks like you want to hear about "+city.capitalize()+" Enter yes or no.\n")
         CiChoice=CiChoice.casefold()
         CChoice= (CiChoice=="no")
        
         while CiChoice not in ("yes","no"): #handle error for the confirmation message
                CiChoice = input('\nThat is not a valid entry. Please try again.\nYour choices are:Yes or No.\n\nYour Choice: ')
                CiChoice = CiChoice.casefold()
                CChoice= (CiChoice=="no")


    # TO DO: get user input for month (all, january, february, ... , june)
    MChoice=True #to confirm the user choice for month
    while MChoice:
         m_data = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
         month = input('\nWhich month would you like to see data on?\nYour choices are: January, February, March, April, May, June. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
         month = month.casefold()
    
         while month not in m_data:
            month = input('\nThat is not a valid entry. Please try again.\nYour choices are: January, February, March, April, May, June. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
            month = month.casefold()
        
         MoChoice=input("\nlooks like you want to hear about "+month.capitalize()+" Enter yes or no.\n")
         MoChoice=MoChoice.casefold()
         MChoice= (MoChoice=="no")
            
         while MoChoice not in ("yes","no"): #handle error for the confirmation message
                MoChoice = input('\nThat is not a valid entry. Please try again.\nYour choices are:Yes or No.\n\nYour Choice: ')
                MoChoice = MoChoice.casefold()
                MChoice= (MoChoice=="no")
    
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DChoice=True #to confirm the user choice for day
    while DChoice:
         d_data = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
         day = input('\nWhich day would you like to see data on?\nYour choices are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. In case you do not  wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
         day = day.casefold()
    
         while day not in d_data:
            day = input('\nThat is not a valid entry. Please try again.\nYour choices are: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. In case you do not wish to apply a filter, please enter \'All\'.\n\nYour Choice: ')
            day = day.casefold()
        
         DaChoice=input("\nlooks like you want to hear about "+day.capitalize()+" Enter yes or no.\n")
         DaChoice=DaChoice.casefold()
         DChoice= (DaChoice=="no")
            
         while DaChoice not in ("yes","no"): #handle error for the confirmation message
                DaChoice = input('\nThat is not a valid entry. Please try again.\nYour choices are:Yes or No.\n\nYour Choice: ')
                DaChoice = DaChoice.casefold()
                DChoice= (DaChoice=="no")


    print('-'*40)
    return city, month, day


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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    # extract Month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month (from 0 to 11)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[(df['month'].value_counts().idxmax())-1]
    
    print('\nMost Frequent Month:', popular_month)

    # TO DO: display the most common day of week
     # extract day from the Start Time column to create a day column
    df['Day'] = df['Start Time'].dt.weekday_name

    # find the most common day 
    popular_day = df['Day'].value_counts().idxmax()
    
    print('\nMost Frequent Day:', popular_day)

    # TO DO: display the most common start hour
    # extract Hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    
    print('\nMost Frequent hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost Common Start Station: ', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('\nMost Common End Station: ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Combination'] = (df['Start Station'] + ' - ' +df['End Station'])
    popular_st_en_station = df['Start-End Combination'].value_counts().idxmax()
    print('\nMost Common Combination of Start and End Station Trips:\n\n', popular_st_en_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Trip Duration:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nTotal Trip Duration:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)
    print("\n")
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        Gender = df['Gender'].value_counts()

        print(Gender)
        print("\n")
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest year of Birth:', df['Birth Year'].min())
        print('\nMost Recent year of Birth:', df['Birth Year'].max())
        print('\nMost Common year of Birth:', df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    restart=True
    while restart:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        n=0
        Uinput=True #to confirm the user choice for restart raw data
        while Uinput:
            Usinput = input('Would you like to see raw data? (Enter:Yes/No).\n')
            Usinput=Usinput.casefold()
            Uinput= (Usinput=="yes")
            
            while Usinput not in ("yes","no"): #handle error for the confirmation message
                    Usinput = input('\nThat is not a valid entry. Please try again.\nYour choices are:Yes or No.\n\nYour Choice: ')
                    Usinput = Usinput.casefold()
                    Uinput= (Usinput=="yes")
            if Uinput:
                print(df.iloc[n : n + 5])
                n += 5
            
        reestart = input('\nWould you like to restart? Enter yes or no.\n')
        restart=(reestart.casefold() == 'yes')


if __name__ == "__main__":
	main()
