import pandas as pd
from data.info import column_to_name

def get_country_info(df, country: str, columns_needed: list):
    """ Returns information about a country

    Args:
        df (pd.DataFrame: Input dataset
        country (str): Country to find info on
        columns_needed (list): Info on the country to pull

    Returns:
        country_info (dict): Information about the country, key is info category, value is the info
    """

    country_info = {}

    # printing out each column
    for column in columns_needed:
        info_category = column_to_name[column]
        info = df.loc[df["Country"] == country, column].iloc[0]

        # making sure info isn't empty
        if pd.isna(info):
            continue

        # appending the info to the list
        country_info[info_category] = info

    return country_info

def output_country_info(country_info: dict, country: str):
    """ Outputs information on a country

    Args:
        country_info (dict): Information about the country, key is info category, value is the info
        country (str): Name of the country the info is on
    """

    print(f"\nHere is the information on the country {country.title()}!")

    for info_category, info in country_info.items():
        print(f"\n\n{info_category}: {info}")

def get_input(df):
    """ Gets input from the user, specifically their committee, topic, and country, then returns it.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        country (str): user inputted country, validated with dataset
    """

    print("Welcome to the automated country profile generator!\n")

    while True:
        country = input("\nWhat is your country? ").lower();

        # making sure user's country is valid, if it is, return values, else redo process
        if country.lower() in df["Country"].values:
            print(f"\nYour country: {country.title()}")
            input("\nPress enter to continue, or Ctrl + c to cancel: ")

            return country

        else:
            print(f"\n{country} is an invalid country. Please try again.")