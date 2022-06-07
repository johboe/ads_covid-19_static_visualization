import pandas as pd
import plotly.graph_objects as go

from datetime import datetime

def plot_figure(x_in, df_input, title, x_label, y_label, legend, y_scale='linear', slider=False):
    """ Quick plot for creating time-series plots
        
        Parameters:
        ----------
        x_in : array 
            array of date time object, or array of numbers
        df_input : pandas dataframe 
            the plotting matrix where each column is plotted
            the name of the column will be used for the legend
        y_scale: str
            y-axis scale as 'log' or 'linear'
        slider: bool
            True or False for x-axis slider
    
        
        Returns:
        ----------
    """
    fig = go.Figure()

    for each in df_input.columns:
        fig.add_trace(go.Scatter(
                        x=x_in,
                        y=df_input[each],
                        name=legend[each],
                        opacity=0.8)
                    )
    fig.update_layout(autosize=True,
                    width=1024,
                    height=768,
                    title=title,
                    font=dict(
                        family="PT Sans, monospace",
                        size=18,
                        color='#7f7f7f'
                        ),
                    xaxis_title=x_label,
                    yaxis_title=y_label
                    )
    fig.update_yaxes(type=y_scale),
    fig.update_xaxes(tickangle=-45,
                nticks=20,
                tickfont=dict(size=14,color="#7f7f7f")
                )
    if slider==True:
        fig.update_layout(xaxis_rangeslider_visible=True)
    fig.show()


def plot_relative_cases():
    """ Plot the relative cases for the three countries """
    df_cases_countries = pd.read_csv("../data/processed/COVID_cases_three_countries.csv", sep=";")
    title = "Relative Cases"
    legend = {"Germany_relative":"Germany", "France_relative":"France", "Italy_relative":"Italy"}
    plot_figure([datetime.strptime(each, '%m/%d/%y') for each in df_cases_countries["date"]], df_cases_countries.iloc[:,1:], title, "Time", "Relational cases [%]", legend,y_scale="linear", slider=False)
    
def plot_relative_vaccinations():
    """ Plot the vaccination rates for the three countries """
    df_vaccinations_countries = pd.read_csv("../data/processed/COVID_vaccinations_three_countries.csv", sep=";")
    title = "Vaccination Rates"
    legend = {"Germany_relative":"Germany", "France_relative":"France", "Italy_relative":"Italy"}
    plot_figure(df_vaccinations_countries["date"], df_vaccinations_countries.iloc[:,1:], title, "Time", "Vaccination Rate [%]", legend, y_scale="linear", slider=False)

if __name__ == "__main__":
    plot_relative_cases()
    plot_relative_vaccinations()