import subprocess
import os
import pandas

def get_cases_data():
    """ Pull new data from John Hopkins GitHub repository """
    # Note: Only relevant directory of timeseries is fetched from repository to not download all large files (according to https://askubuntu.com/questions/460885/how-to-clone-only-some-directories-from-a-git-repository)
    # git clone --depth 1 --filter=blob:none --sparse https://github.com/CSSEGISandData/COVID-19.git
    # cd COVID-19/
    # git sparse-checkout init --cone
    # git sparse-checkout set csse_covid_19_data/csse_covid_19_time_series
    git_pull = subprocess.Popen("git pull",
                            cwd = os.path.dirname('../data/raw/COVID-19/'),
                            shell=True,
                            stdout=subprocess.PIPE,              # get pipeline for standard out
                            stderr=subprocess.PIPE)              # get pipeline for stderr
    (out, error) = git_pull.communicate()

    print("Error: " + str(error))
    print("Out: " + str(out))

def get_vaccination_data():
    """ Pull new data from GitHub Repository of Our World in Data """
    git_pull = subprocess.Popen("git pull",
                            cwd = os.path.dirname('../data/raw/vaccinations/covid-19-data/'),
                            shell=True,
                            stdout=subprocess.PIPE,              # get pipeline for standard out
                            stderr=subprocess.PIPE)              # get pipeline for stderr
    (out, error) = git_pull.communicate()

    print("Error: " + str(error))
    print("Out: " + str(out))