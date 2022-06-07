import pandas as pd
import numpy as np

def store_processed_cases():
    """ Transform data from John Hopkins into a data set allowing to plot the cases in a simple way """
    data_path = "../data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    pd_raw = pd.read_csv(data_path)
        
    pd_data_base=pd_raw.rename(columns={'Country/Region':'country',
                        'Province/State':'state'})

    countries = pd_data_base['country']
    df_cases_countries = pd.DataFrame({'date':pd_raw.columns[4:]})
    for country in countries:
    # add for each country a new column in df_cases_countries by summing up values of each Province/State with corresponding country
        df_cases_countries[country] = np.array(pd_raw[pd_raw['Country/Region']==country].iloc[:,4::].sum(axis=0))

    df_cases_countries.to_csv("../data/processed/COVID_cases_countries.csv", sep=";", index=False)

def store_processed_vaccinations():
    """ Transform vaccination data from 'Our World in Data' """
    data_path = "../data/raw/vaccinations/covid-19-data/public/data/vaccinations/vaccinations.csv"
    pd_raw = pd.read_csv(data_path)
    countries = pd_raw['location'].drop_duplicates()

    df_vacc_countries = pd.DataFrame({'date':pd_raw['date'].drop_duplicates()})
    df_vacc_countries.set_index('date', inplace=True)

    for country in countries:
        df_country = pd.DataFrame({'date': pd_raw.loc[pd_raw['location']==country]['date'], country: pd_raw.loc[pd_raw['location']==country]['people_fully_vaccinated']})
        df_country.set_index('date', inplace=True)
        df_vacc_countries = df_vacc_countries.join(df_country, how='outer')
    
    df_vacc_countries.to_csv("../data/processed/COVID_vaccinations_countries.csv", sep=";", index=True)

def store_cases_three_countries(countries: dict):
    """ Store relational cases (absolute cases divided by population size) for three countries in extra file """
    df_cases_countries = pd.read_csv("../data/processed/COVID_cases_countries.csv", sep=";")
    df_cases_three_countries = pd.DataFrame({"date":df_cases_countries["date"]})

    for country in countries.keys():
        df_cases_three_countries[country + "_relative"] = df_cases_countries[country].divide(countries[country])
    
    df_cases_three_countries.to_csv("../data/processed/COVID_cases_three_countries.csv", sep=";", index=False)


def store_vaccinations_three_countries(countries: dict):
    """ Store relational vaccinations (absolute vaccinations divided by population size) for three countries in extra file """
    df_vacc_countries = pd.read_csv("../data/processed/COVID_vaccinations_countries.csv", sep=";")
    df_vacc_three_countries = pd.DataFrame({"date": df_vacc_countries["date"]})

    for country in countries.keys():
        df_vacc_three_countries[country + "_relative"] = df_vacc_countries[country].divide(countries[country])   
    
    df_vacc_three_countries.to_csv("../data/processed/COVID_vaccinations_three_countries.csv", sep=";", index=False)

if __name__ == '__main__':
    # define three countries to select (attention: not all countries have the same name in both DataFrames of cases and vaccinations)
    # source of population data: datatopics.worldbank.org
    countries = {"Germany":83240000, "Italy":59550000, "France":67390000}
    store_processed_cases()
    store_processed_vaccinations()
    store_cases_three_countries(countries)
    store_vaccinations_three_countries(countries)