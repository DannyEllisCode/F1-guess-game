import sys
import requests
from bs4 import BeautifulSoup      # library to parse HTML
import pandas as pd                # library for data analysis

pd.set_option('display.max_columns', None)

# What should be used to give clues?
# First Team, Last Team (or current team), Races Driven, Races Won, Total Points scored, Number used when starting
# Nationality

# Get list of F1 drivers in format of HTML from a Wikipedia table
response = requests.get("https://en.wikipedia.org/wiki/List_of_Formula_One_drivers")
table_class = "wikitable sortable jquery-tablesorter"

# Checks data is legal to download and use
if response.status_code != 200:
    sys.exit("Error: Response is not 200.")

# parse data from the html into a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')
f1_driver_table = soup.select("#mw-content-text > div.mw-parser-output > table:nth-child(36)")

# Reads HTML of driver table and returns a list
df = pd.read_html(str(f1_driver_table))

# Converts list to Dataframe
df = pd.DataFrame(df[0])

# Clean up data for use in game format.
# Remove unwanted columns "Race entries"
df = df.drop(["Race entries"], axis=1)

# Remove unwanted last row
df = df[:-1]

# Rename points column
df = df.rename(columns={"Points[a]": "Points"})

# Remove characters on the end of driver's names from Wiki table
df["Driver name"] = df["Driver name"].str.replace(r"[*^~]+$", "", regex=True)

# Removes characters on multiple columns and in order to return only digits
# uses regex to remove anything after " " or "[" or "(" including those specified
columns = ["Race starts", "Pole positions", "Race wins", "Podiums", "Fastest laps", "Points"]
df[columns] = df[columns].replace(r"[ [(].*", "", regex=True)

# Converts the Points column to numeric value, allowing comparison to 0 to drop
# all racers with 0 points and resets row index
df["Points"] = pd.to_numeric(df["Points"])
df = df[df.Points != 0].reset_index(drop=True)

# Rename df
f1_driver_list = df
#print(f1_driver_list[8:9])
#print(f1_driver_list)

# Current driver list       ## CREATE A LIST HERE SO THAT CURRENT DRIVERS DATA CAN BE USED IN EXTRA WAYS

def total_seasons_int(seasons_range):
    # Creates a total years variable to add up seasons raced
    total_years = 0

    # Split string by ", " to create list of years and year ranges
    seasons_list = seasons_range.split(", ")

    # Iterate over seasons_list to add up seasons
    for i in seasons_list:
        # Splits any years with a "–" into new list to be able to subtract years to get total
        year_range = i.split("–")

        # If length of list is 2 then it is a range. Subtracts higher number
        # from lower and adds one to get total years raced in that range. (Could use map function?)
        if len(year_range) == 2:
            i_years = int(year_range[1]) - int(year_range[0]) + 1
            total_years += i_years

        # If the above does not happen then it is just a single year, not a range (i.e. "1998")
        # so just adds 1 to total_years
        else:
            total_years += 1

    return total_years



# Chooses a random driver from the database
# secret_driver = f1_driver_list.sample()
secret_driver = f1_driver_list[9:10]

# Defines characteristics of secret_driver
secret_driver_name = secret_driver.iloc[0, 0]
secret_driver_nationality = secret_driver.iloc[0, 1]
secret_driver_seasons = secret_driver.iloc[0, 2]
secret_driver_wdcs = secret_driver.iloc[0, 3]
secret_driver_starts = secret_driver.iloc[0, 4]
secret_driver_poles = secret_driver.iloc[0, 5]
secret_driver_wins = secret_driver.iloc[0, 6]
secret_driver_podiums = secret_driver.iloc[0, 7]
secret_driver_fast_laps = secret_driver.iloc[0, 8]
secret_driver_points = secret_driver.iloc[0, 9]

# Stores the characteristics in a list for comparison later
secret_driver_characteristics = [
    secret_driver_name,
    secret_driver_nationality,
    secret_driver_seasons,
    secret_driver_wdcs,
    secret_driver_starts,
    secret_driver_poles,
    secret_driver_wins,
    secret_driver_podiums,
    secret_driver_fast_laps,
    secret_driver_points]

#print(secret_driver_name)
#print(secret_driver_nationality)
print(secret_driver_seasons)
#print(secret_driver_wdcs)
#print(secret_driver_starts)
#print(secret_driver_poles)
#print(secret_driver_wins)
#print(secret_driver_podiums)
#print(secret_driver_fast_laps)
#if float(secret_driver_points) == int(secret_driver_points):
    #print(int(secret_driver_points))
#else:
    #print(secret_driver_points)

# Defines the number of guesses the user can take
max_guesses = 8



# Defines a function to check the user's guess against the secret driver variable
def check_guess(guess, secret_driver):

    if guess == secret_driver:
        return True
    else:
        return False

# Defines function to return the game state
def game_state(guesses_list, max_guesses):

    # Displays how many guesses are left and currently guessed drivers
    print("Guesses remaining: " + str(max_guesses - len(guesses_list)))
    print(guesses_list)

# Defines a function to work out and add total seasons to current guess and secret driver

# Defines a function to compare characteristics of current guess and answer
def check_characteristics(secret_driver_list, current_guess_list):

    # Compares Nationality
    if secret_driver_list[1] == current_guess_list[1]:
        print("Same nationality!")
    else:
        print("Wrong nationality!")

    # Compares amount of seasons competed in
    if total_seasons_int(secret_driver_seasons) > total_seasons_int(current_guess_seasons):
        print("More seasons competed in!")
    elif total_seasons_int(secret_driver_seasons) < total_seasons_int(current_guess_seasons):
        print("Less seasons competed in!")
    else:
        print("Same amount of seasons competed in!")

    # Compares championships won
    if int(secret_driver_list[3][0]) > int(current_guess_list[3][0]):
        print("More championships won!")
    elif int(secret_driver_list[3][0]) < int(current_guess_list[3][0]):
        print("Less championships won!")
    else:
        print("Correct amount of championships won!")

    # Compares race starts
    if int(secret_driver_list[4]) > int(current_guess_list[4]):
        print("More starts!")
    elif int(secret_driver_list[4]) < int(current_guess_list[4]):
        print("Less starts!")
    else:
        print("Correct amount of starts!")

    # Compares pole positions
    if int(secret_driver_list[5]) > int(current_guess_list[5]):
        print("More poles!")
    elif int(secret_driver_list[5]) < int(current_guess_list[5]):
        print("Less poles!")
    else:
        print("Correct amount of poles!")

    # Compares wins
    if int(secret_driver_list[6]) > int(current_guess_list[6]):
        print("More wins!")
    elif int(secret_driver_list[6]) < int(current_guess_list[6]):
        print("Less wins!")
    else:
        print("Correct amount of wins!")

    # Compares podiums
    if int(secret_driver_list[7]) > int(current_guess_list[7]):
        print("More podiums!")
    elif int(secret_driver_list[7]) < int(current_guess_list[7]):
        print("Less podiums!")
    else:
        print("Correct amount of podiums!")

    # Compares fastest laps
    if int(secret_driver_list[8]) > int(current_guess_list[8]):
        print("More fastest laps!")
    elif int(secret_driver_list[8]) < int(current_guess_list[8]):
        print("Less fastest laps!")
    else:
        print("Correct amount of fastest laps!")

    # Compares points
    if secret_driver_list[9] > current_guess_list[9]:
        print("More points!")
    elif secret_driver_list[9] < current_guess_list[9]:
        print("Less points!")
    else:
        print("Correct amount of points!")


# List of user guesses
guesses = []

# Starts the game loop
while len(guesses) < max_guesses:
    # Gets user guess
    current_guess = str(input("Please guess a driver: "))

    # Checks if guess is in the "f1_driver_list" DataFrame
    guess_check = (f1_driver_list["Driver name"].eq(current_guess)).any()
    if not guess_check:
        print("Invalid guess!")
        continue

    # Check if guess has already been guessed
    if current_guess in guesses:
        print("You have already guessed this driver!")
        continue

    # Adds the user's guess to the guesses list
    guesses.append(current_guess)

    # Checks if guess is correct
    if current_guess == str(secret_driver_name):
        print("You win! The driver was " + str(secret_driver_name))
        break

    # Gets information of current guess by retrieving info from dataframe
    current_guess_info = (f1_driver_list.loc[f1_driver_list["Driver name"] == current_guess])

    # Defines characteristics of current guess from dataframe to strings
    current_guess_name = current_guess_info.iloc[0, 0]
    current_guess_nationality = current_guess_info.iloc[0, 1]
    current_guess_seasons = current_guess_info.iloc[0, 2]
    current_guess_wdcs = current_guess_info.iloc[0, 3]
    current_guess_starts = current_guess_info.iloc[0, 4]
    current_guess_poles = current_guess_info.iloc[0, 5]
    current_guess_wins = current_guess_info.iloc[0, 6]
    current_guess_podiums = current_guess_info.iloc[0, 7]
    current_guess_fast_laps = current_guess_info.iloc[0, 8]
    current_guess_points = current_guess_info.iloc[0, 9]

    # Stores the characteristics of current guess into a list
    current_guess_characteristics = [
        current_guess_name,
        current_guess_nationality,
        current_guess_seasons,
        current_guess_wdcs,
        current_guess_starts,
        current_guess_poles,
        current_guess_wins,
        current_guess_podiums,
        current_guess_fast_laps,
        current_guess_points]

    # Compares characteristics of current guess to answer using function
    check_characteristics(secret_driver_characteristics, current_guess_characteristics)

    print(current_guess_name)
    print(current_guess_nationality)
    print(current_guess_seasons)
    print(current_guess_wdcs)
    print(current_guess_starts)
    print(current_guess_poles)
    print(current_guess_wins)
    print(current_guess_podiums)
    print(current_guess_fast_laps)
    print(current_guess_points)

    # Shows the current game state
    game_state(guesses, max_guesses)

# Prints end game message when all guesses are used
if len(guesses) == max_guesses:
    print("Sorry, you ran out of guesses. The correct answer was " + secret_driver_name)