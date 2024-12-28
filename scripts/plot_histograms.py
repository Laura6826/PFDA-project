import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(dfrp, dfs, dfca):
    sns.set_theme(style="darkgrid")
    fig, axs = plt.subplots(4, 3, figsize=(18, 10))

    # Plot histograms for rainfall (mm)
    sns.histplot(data=dfrp, x="rain", kde=True, color="blue", bins=30, ax=axs[0, 0])
    axs[0, 0].set_title('Roches Point')
    axs[0, 0].set_xlabel('Rainfall (mm)')
    axs[0, 0].set_ylabel('Frequency')
    axs[0, 0].set_xlim(0, 50)

    sns.histplot(data=dfs, x="rain", kde=True, color="purple", bins=30, ax=axs[0, 1])
    axs[0, 1].set_title('Sherkin Island')
    axs[0, 1].set_xlabel('Rainfall (mm)')
    axs[0, 1].set_ylabel('Frequency')
    axs[0, 1].set_xlim(0, 50)

    sns.histplot(data=dfca, x="rain", kde=True, color="violet", bins=30, ax=axs[0, 2])
    axs[0, 2].set_title('Cork Airport')
    axs[0, 2].set_xlabel('Rainfall (mm)')
    axs[0, 2].set_ylabel('Frequency')
    axs[0, 2].set_xlim(0, 50)

    # Plot histograms for temperature (0C)
    sns.histplot(data=dfrp, x="temp", kde=True, color="blue", bins=30, ax=axs[1, 0])
    axs[1, 0].set_title('Roches Point')
    axs[1, 0].set_xlabel('Temperature (0C)')
    axs[1, 0].set_ylabel('Frequency')
    axs[1, 0].set_xlim(-10, 40)

    sns.histplot(data=dfs, x="temp", kde=True, color="purple", bins=30, ax=axs[1, 1])
    axs[1, 1].set_title('Sherkin Island')
    axs[1, 1].set_xlabel('Temperature (0C)')
    axs[1, 1].set_ylabel('Frequency')
    axs[1, 1].set_xlim(-10, 40)

    sns.histplot(data=dfca, x="temp", kde=True, color="violet", bins=30, ax=axs[1, 2])
    axs[1, 2].set_title('Cork Airport')
    axs[1, 2].set_xlabel('Temperature (0C)')
    axs[1, 2].set_ylabel('Frequency')
    axs[0, 2].set_xlim(-10, 40)

    # Plot histograms for wind speed (knots)
    sns.histplot(data=dfrp, x="wdsp", kde=True, color="blue", bins=30, ax=axs[2, 0])
    axs[2, 0].set_title('Roches Point')
    axs[2, 0].set_xlabel('Wind Speed (knots)')
    axs[2, 0].set_ylabel('Frequency')
    axs[2, 0].set_xlim(0, 60)

    sns.histplot(data=dfs, x="wdsp", kde=True, color="purple", bins=30, ax=axs[2, 1])
    axs[2, 1].set_title('Sherkin Island')
    axs[2, 1].set_xlabel('Wind Speed (knots)')
    axs[2, 1].set_ylabel('Frequency')
    axs[2, 1].set_xlim(0, 60)

    sns.histplot(data=dfca, x="wdsp", kde=True, color="violet", bins=30, ax=axs[2, 2])
    axs[2, 2].set_title('Cork Airport')
    axs[2, 2].set_xlabel('Wind Speed (knots)')
    axs[2, 2].set_ylabel('Frequency')
    axs[2, 2].set_xlim(0, 60)

    # Plot histograms for wind direction (degrees)
    sns.histplot(data=dfrp, x="wddir", kde=True, color="blue", bins=30, ax=axs[3, 0])
    axs[3, 0].set_title('Roches Point')
    axs[3, 0].set_xlabel('Wind Direction (degrees)')
    axs[3, 0].set_ylabel('Frequency')
    axs[3, 0].set_xlim(0, 360)

    sns.histplot(data=dfs, x="wddir", kde=True, color="purple", bins=30, ax=axs[3, 1])
    axs[3, 1].set_title('Sherkin Island')
    axs[3, 1].set_xlabel('Wind Direction (degrees)')
    axs[3, 1].set_ylabel('Frequency')
    axs[3, 1].set_xlim(0, 360)

    sns.histplot(data=dfca, x="wddir", kde=True, color="violet", bins=30, ax=axs[3, 2])
    axs[3, 2].set_title('Cork Airport')
    axs[3, 2].set_xlabel('Wind Direction (degrees)')
    axs[3, 2].set_ylabel('Frequency')
    axs[3, 2].set_xlim(0, 360)

    # Add an overall title to the figure
    fig.suptitle('Figure 3.1: Histograms with gaussian curves for each variable at the 3 weather stations', fontsize=16, fontweight='bold', color= 'orange')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('Figure3.1.png')
    plt.show()

