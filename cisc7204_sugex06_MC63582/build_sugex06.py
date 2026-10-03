#!/usr/bin/env python3
"""Build CISC7204 Suggested Exercise 06 notebooks, execute them, and package."""

from __future__ import annotations

import base64
import io
import os
import shutil
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook, new_output

ROOT = Path(__file__).resolve().parent
SID = "MC63582"
PKG = ROOT / f"cisc7204_sugex06_{SID}"
DATA = Path("/tmp/dvw-data")

P1 = ["Exercise6.01", "Activity6.01", "Activity6.02"]
P2 = ["Exercise6.02", "Activity6.03", "Activity6.04", "Activity6.05"]
P3 = ["Exercise6.03", "Exercise6.04", "Activity6.06", "Activity6.07"]

PRACTICES = {
    "P1_folder": P1,
    "P2_folder": P2,
    "P3_folder": P3,
}

DATA_BY_NOTEBOOK = {
    "Exercise6.01": [],
    "Activity6.01": [
        "GOOGL_data.csv",
        "FB_data.csv",
        "AAPL_data.csv",
        "AMZN_data.csv",
        "MSFT_data.csv",
    ],
    "Activity6.02": ["movie_scores.csv"],
    "Exercise6.02": ["water_usage.csv"],
    "Activity6.03": ["tips.csv"],
    "Activity6.04": ["smartphone_sales.csv"],
    "Activity6.05": [],
    "Exercise6.03": ["anage_data.csv"],
    "Exercise6.04": [],
    "Activity6.06": ["anage_data.csv"],
    "Activity6.07": ["images"],
}


def md(text: str):
    return new_markdown_cell(textwrap.dedent(text).strip("\n") + "\n")


def code(text: str):
    return new_code_cell(textwrap.dedent(text).strip("\n") + "\n")


def notebook(cells):
    nb = new_notebook(
        cells=cells,
        metadata={
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0",
            },
        },
    )
    return nb


def make_exercise_601():
    return notebook(
        [
            md("## Exercise 6.01: Creating a Simple Visualization"),
            md("In this exercise, we will create our first simple plot using Matplotlib."),
            md("#### Import statements"),
            md("Import the necessary modules and enable plotting within a jupyter notebook."),
            code(
                """
                import numpy as np
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Creating, plotting, and saving a figure"),
            md(
                """
                Explicitly create a figure and set the dpi to 200. Plot the following data pairs (x, y) as circles, which are connected via line segments: (1, 1), (2, 3), (4, 4), (5, 3). Save the plot using plt.savefig(). Finally, visualize the plot.

                Remark: Jupyter Notebooks requires creating, plotting, and saving to be done within one cell, otherwise an empty figure is saved.
                """
            ),
            code(
                """
                plt.figure(dpi=200)
                plt.plot([1, 2, 4, 5], [1, 3, 4, 3], '-o')
                plt.savefig('Exercise6.01.png', dpi=300, bbox_inches='tight')
                plt.show()
                """
            ),
        ]
    )


def make_activity_601():
    return notebook(
        [
            md("## Activity 6.01: Visualizing Stock Trends by Using a Line Plot"),
            md(
                """
                In this activity, we will create a line plot to show stock trends. The aim of this activity is to not just visualize the data but to use labels, a title, and a legend to make the visualization self-explanatory and "complete."

                You downloaded the stock prices for the "big five": Amazon, Google, Apple, Facebook, and Microsoft. Visualize the closing prices in dollars to identify trends.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import matplotlib.pyplot as plt
                import numpy as np
                import pandas as pd
                %matplotlib inline
                """
            ),
            md("#### Loading the datasets"),
            code(
                """
                google = pd.read_csv('GOOGL_data.csv')
                facebook = pd.read_csv('FB_data.csv')
                apple = pd.read_csv('AAPL_data.csv')
                amazon = pd.read_csv('AMZN_data.csv')
                microsoft = pd.read_csv('MSFT_data.csv')
                """
            ),
            md("#### Creating a line chart of closing prices"),
            code(
                """
                plt.figure(figsize=(16, 8), dpi=300)
                plt.plot('date', 'close', data=google, label='Google')
                plt.plot('date', 'close', data=facebook, label='Facebook')
                plt.plot('date', 'close', data=apple, label='Apple')
                plt.plot('date', 'close', data=amazon, label='Amazon')
                plt.plot('date', 'close', data=microsoft, label='Microsoft')
                plt.xticks(np.arange(0, 1260, 40), rotation=70)
                plt.yticks(np.arange(0, 1450, 100))
                plt.title('Stock trend', fontsize=16)
                plt.ylabel('Closing price in $', fontsize=14)
                plt.grid()
                plt.legend()
                plt.show()
                """
            ),
        ]
    )


def make_activity_602():
    return notebook(
        [
            md("## Activity 6.02: Creating a Bar Plot for Movie Comparison"),
            md(
                """
                In this activity, we will create visually appealing bar plots. We will use a bar plot to compare movie scores. You are given five movies with scores from Rotten Tomatoes. The Tomatometer is the percentage of approved Tomatometer critics who have given a positive review for the movie. The Audience Score is the percentage of users who have given a score of 3.5 or higher out of 5. Compare these two scores among the five movies.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import numpy as np
                import pandas as pd
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Loading the dataset"),
            code("movie_scores = pd.read_csv('movie_scores.csv')"),
            md("#### Creating a visually appealing grouped bar plot"),
            code(
                """
                plt.figure(figsize=(10, 5), dpi=300)
                pos = np.arange(len(movie_scores['MovieTitle']))
                width = 0.3
                plt.bar(pos - width / 2, movie_scores['Tomatometer'], width, label='Tomatometer')
                plt.bar(pos + width / 2, movie_scores['AudienceScore'], width, label='Audience Score')
                plt.xticks(pos, rotation=10)
                plt.yticks(np.arange(0, 101, 20))
                ax = plt.gca()
                ax.set_xticklabels(movie_scores['MovieTitle'])
                ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
                ax.set_yticks(np.arange(0, 100, 5), minor=True)
                ax.yaxis.grid(which='major')
                ax.yaxis.grid(which='minor', linestyle='--')
                plt.title('Movie comparison')
                plt.legend()
                plt.show()
                """
            ),
        ]
    )


def make_exercise_602():
    return notebook(
        [
            md("## Exercise 6.02: Creating a Pie Chart for Water Usage"),
            md(
                """
                In this exercise, we will use a pie chart to visualize water usage. There has been a shortage of water in your locality in the past few weeks. To understand the reason behind it, generate a visual representation of water usage using pie charts.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import pandas as pd
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Loading the dataset"),
            code("data = pd.read_csv('water_usage.csv')"),
            md("#### Creating a pie chart"),
            code(
                """
                plt.figure(figsize=(8, 8), dpi=300)
                plt.pie('Percentage', explode=(0, 0, 0.1, 0, 0, 0),
                        labels='Usage', data=data, autopct='%.0f%%')
                plt.title('Water usage')
                plt.show()
                """
            ),
        ]
    )


def make_activity_603():
    return notebook(
        [
            md("## Activity 6.03: Creating a Stacked Bar Plot to Visualize Restaurant Performance"),
            md(
                """
                In this activity, we will use a stacked bar plot to visualize the performance of a restaurant. Due to a new law, you have to introduce a No Smoking Day. To make as few losses as possible, you want to visualize how many sales are made every day, categorized by smokers and non-smokers.

                Use the dataset `tips` from Seaborn, which contains multiple entries of restaurant bills, and create a matrix where the elements contain the sum of the total bills for each day and smokers/non-smokers.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                import seaborn as sns
                %matplotlib inline
                """
            ),
            md(
                """
                #### Loading the dataset

                The tutorial notes load Seaborn's built-in `tips` dataset with `sns.load_dataset('tips')`. We load the same dataset from a local CSV so the notebook is self-contained.
                """
            ),
            code("bills = pd.read_csv('tips.csv')"),
            md("#### Creating a matrix of total bills by day and smoker status"),
            code(
                """
                days = ['Thur', 'Fri', 'Sat', 'Sun']
                days_range = np.arange(len(days))
                smoker = ['Yes', 'No']
                bills_by_days = [bills[bills['day'] == day] for day in days]
                bills_by_days_smoker = [[bills_by_days[day][bills_by_days[day]['smoker'] == s]
                                         for s in smoker] for day in days_range]
                total_by_days_smoker = [[bills_by_days_smoker[day][s]['total_bill'].sum()
                                         for s in range(len(smoker))] for day in days_range]
                totals = np.asarray(total_by_days_smoker)
                totals
                """
            ),
            md("#### Creating a stacked bar plot"),
            code(
                """
                plt.figure(figsize=(10, 5), dpi=300)
                plt.bar(days_range, totals[:, 0], label='Smoker')
                plt.bar(days_range, totals[:, 1], bottom=totals[:, 0], label='Non-smoker')
                plt.legend()
                plt.xticks(days_range)
                ax = plt.gca()
                ax.set_xticklabels(days)
                ax.yaxis.grid()
                plt.ylabel('Daily total sales in $')
                plt.title('Restaurant performance')
                plt.show()
                """
            ),
        ]
    )


def make_activity_604():
    return notebook(
        [
            md("## Activity 6.04: Comparing Smartphone Sales Units Using a Stacked Area Chart"),
            md(
                """
                In this activity, we will compare smartphone sales units using a stacked area chart. You want to invest in one of the five biggest smartphone manufacturers. Looking at the quarterly sales units as part of a whole may be a good indicator of which company to invest in.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Loading the dataset"),
            code("sales = pd.read_csv('smartphone_sales.csv')"),
            md("#### Creating a stacked area chart"),
            code(
                """
                plt.figure(figsize=(10, 6), dpi=300)
                labels = sales.columns[2:]
                plt.stackplot('Quarter', 'Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO',
                              data=sales, labels=labels)
                plt.legend()
                plt.xlabel('Quarters')
                plt.ylabel('Sales units in thousands')
                plt.title('Smartphone sales units')
                plt.show()
                """
            ),
        ]
    )


def make_activity_605():
    return notebook(
        [
            md("## Activity 6.05: Using a Histogram and a Box Plot to Visualize Intelligence Quotient"),
            md(
                """
                In this activity, we will visualize the intelligence quotient (IQ) using histogram and box plots. 100 people have come for an interview in a company. To place an individual applicant in the overall group, a histogram and a box plot shall be used.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import numpy as np
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### IQ samples"),
            code(
                """
                iq_scores = [126, 89, 90, 101, 102, 74, 93, 101, 66, 120, 108, 97, 98,
                             105, 119, 92, 113, 81, 104, 108, 83, 102, 105, 111, 102,
                             107, 103, 89, 89, 110, 71, 110, 120, 85, 111, 83, 122,
                             120, 102, 84, 118, 100, 100, 114, 81, 109, 69, 97, 95,
                             106, 116, 109, 114, 98, 90, 92, 98, 91, 81, 85, 86, 102,
                             93, 112, 76, 89, 110, 75, 100, 90, 96, 94, 107, 108, 95,
                             96, 96, 114, 93, 95, 117, 141, 115, 95, 86, 100, 121, 103,
                             66, 99, 96, 111, 110, 105, 110, 91, 112, 102, 112, 75]
                """
            ),
            md(
                """
                #### Histogram

                Plot a histogram with 10 bins for the given IQ scores. IQ scores are normally distributed with a mean of 100 and a standard deviation of 15. Visualize the mean as a vertical solid red line, and the standard deviation using dashed vertical lines.
                """
            ),
            code(
                """
                plt.figure(figsize=(6, 4), dpi=150)
                plt.hist(iq_scores, bins=10)
                plt.axvline(x=100, color='r')
                plt.axvline(x=115, color='r', linestyle='--')
                plt.axvline(x=85, color='r', linestyle='--')
                plt.xlabel('IQ score')
                plt.ylabel('Frequency')
                plt.title('IQ scores for a test group of a hundred adults')
                plt.show()
                """
            ),
            md("#### Box plot for the same IQ scores"),
            code(
                """
                plt.figure(figsize=(6, 4), dpi=150)
                plt.boxplot(iq_scores)
                ax = plt.gca()
                ax.set_xticklabels(['Test group'])
                plt.ylabel('IQ score')
                plt.title('IQ scores for a test group of a hundred adults')
                plt.show()
                """
            ),
            md("#### IQ scores for different test groups"),
            code(
                """
                group_a = [118, 103, 125, 107, 111, 96, 104, 97, 96, 114, 96, 75, 114,
                           107, 87, 117, 117, 114, 117, 112, 107, 133, 94, 91, 118, 110,
                           117, 86, 143, 83, 106, 86, 98, 126, 109, 91, 112, 120, 108,
                           111, 107, 98, 89, 113, 117, 81, 113, 112, 84, 115, 96, 93,
                           128, 115, 138, 121, 87, 112, 110, 79, 100, 84, 115, 93, 108,
                           130, 107, 106, 106, 101, 117, 93, 94, 103, 112, 98, 103, 70,
                           139, 94, 110, 105, 122, 94, 94, 105, 129, 110, 112, 97, 109,
                           121, 106, 118, 131, 88, 122, 125, 93, 78]
                group_b = [126, 89, 90, 101, 102, 74, 93, 101, 66, 120, 108, 97, 98,
                           105, 119, 92, 113, 81, 104, 108, 83, 102, 105, 111, 102, 107,
                           103, 89, 89, 110, 71, 110, 120, 85, 111, 83, 122, 120, 102,
                           84, 118, 100, 100, 114, 81, 109, 69, 97, 95, 106, 116, 109,
                           114, 98, 90, 92, 98, 91, 81, 85, 86, 102, 93, 112, 76, 89,
                           110, 75, 100, 90, 96, 94, 107, 108, 95, 96, 96, 114, 93, 95,
                           117, 141, 115, 95, 86, 100, 121, 103, 66, 99, 96, 111, 110,
                           105, 110, 91, 112, 102, 112, 75]
                group_c = [108, 89, 114, 116, 126, 104, 113, 96, 69, 121, 109, 102, 107,
                           122, 104, 107, 108, 137, 107, 116, 98, 132, 108, 114, 82, 93,
                           89, 90, 86, 91, 99, 98, 83, 93, 114, 96, 95, 113, 103, 81,
                           107, 85, 116, 85, 107, 125, 126, 123, 122, 124, 115, 114, 93,
                           93, 114, 107, 107, 84, 131, 91, 108, 127, 112, 106, 115, 82,
                           90, 117, 108, 115, 113, 108, 104, 103, 90, 110, 114, 92, 101,
                           72, 109, 94, 122, 90, 102, 86, 119, 103, 110, 96, 90, 110,
                           96, 69, 85, 102, 69, 96, 101, 90]
                group_d = [93, 99, 91, 110, 80, 113, 111, 115, 98, 74, 96, 80, 83, 104,
                           106, 108, 85, 83, 108, 94, 79, 87, 113, 112, 111, 111, 79,
                           116, 104, 84, 116, 111, 103, 103, 112, 68, 54, 80, 86, 119,
                           81, 84, 91, 96, 116, 125, 99, 58, 102, 77, 98, 100, 90, 106,
                           109, 114, 102, 102, 112, 103, 98, 96, 85, 97, 110, 131, 92,
                           79, 115, 122, 95, 105, 74, 85, 85, 95]
                """
            ),
            md("#### Box plot for different test groups"),
            code(
                """
                plt.figure(figsize=(6, 4), dpi=150)
                plt.boxplot([group_a, group_b, group_c, group_d])
                ax = plt.gca()
                ax.set_xticklabels(['Group A', 'Group B', 'Group C', 'Group D'])
                plt.ylabel('IQ score')
                plt.title('IQ scores for different test groups')
                plt.show()
                """
            ),
        ]
    )


def make_exercise_603():
    return notebook(
        [
            md("## Exercise 6.03: Using a Scatter Plot to Visualize Correlation between Various Animals"),
            md(
                """
                In this exercise, we will use a scatter plot to show correlation within a dataset. You are given a dataset containing information about various animals. Visualize the correlation between the various animal attributes.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Loading the dataset"),
            code("data = pd.read_csv('anage_data.csv')"),
            md("#### Preprocessing"),
            code(
                """
                longevity = 'Maximum longevity (yrs)'
                mass = 'Body mass (g)'
                data = data[np.isfinite(data[longevity]) & np.isfinite(data[mass])]
                amphibia = data[data['Class'] == 'Amphibia']
                aves = data[data['Class'] == 'Aves']
                mammalia = data[data['Class'] == 'Mammalia']
                reptilia = data[data['Class'] == 'Reptilia']
                """
            ),
            md("#### Creating a scatter plot with a log scale"),
            code(
                """
                plt.figure(figsize=(10, 6), dpi=300)
                plt.scatter(amphibia[mass], amphibia[longevity], label='Amphibia')
                plt.scatter(aves[mass], aves[longevity], label='Aves')
                plt.scatter(mammalia[mass], mammalia[longevity], label='Mammalia')
                plt.scatter(reptilia[mass], reptilia[longevity], label='Reptilia')
                plt.legend()
                ax = plt.gca()
                ax.set_xscale('log')
                ax.set_yscale('log')
                plt.xlabel('Body mass in grams')
                plt.ylabel('Maximum longevity in years')
                plt.show()
                """
            ),
        ]
    )


def make_exercise_604():
    return notebook(
        [
            md("## Exercise 6.04: Working on Radar Charts"),
            md(
                """
                In this exercise, it is shown step by step how to create a radar chart. As a manager of the team, you have to award a "Star Performer" trophy to an employee for the month of December. Create radar charts to understand the performance of your team and award the trophy.
                """
            ),
            md("#### Import settings"),
            code(
                """
                import numpy as np
                import pandas as pd
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Sample data"),
            md("Attributes: Efficiency, Quality, Commitment, Responsible Conduct, Cooperation"),
            code(
                """
                data = pd.DataFrame({
                    'Employee': ['Alex', 'Alice', 'Chris', 'Jennifer'],
                    'Efficiency': [5, 4, 4, 3],
                    'Quality': [5, 5, 3, 3],
                    'Commitment': [5, 4, 4, 4],
                    'Responsible Conduct': [4, 4, 4, 3],
                    'Cooperation': [4, 3, 4, 5]
                })
                data
                """
            ),
            md("#### Create angle values and close the plot"),
            code(
                """
                attributes = list(data.columns[1:])
                values = list(data.values[:, 1:])
                employees = list(data.values[:, 0])
                angles = [n / float(len(attributes)) * 2 * np.pi for n in range(len(attributes))]
                angles += angles[:1]
                values = np.asarray(values)
                values = np.concatenate([values, values[:, 0:1]], axis=1)
                """
            ),
            md("#### Create subplots with the polar projection"),
            code(
                """
                plt.figure(figsize=(8, 8), dpi=150)
                for i in range(4):
                    ax = plt.subplot(2, 2, i + 1, polar=True)
                    ax.plot(angles, values[i])
                    ax.set_yticks([1, 2, 3, 4, 5])
                    ax.set_xticks(angles[:-1])
                    ax.set_xticklabels(attributes)
                    ax.set_title(employees[i], fontsize=14, color='r')
                plt.tight_layout()
                plt.show()
                """
            ),
        ]
    )


def make_activity_606():
    return notebook(
        [
            md("## Activity 6.06: Creating a Scatter Plot with Marginal Histograms"),
            md(
                """
                In this activity, we will make use of GridSpec to visualize a scatter plot with marginal histograms. You are given a dataset containing information about various animals. Visualize the correlation between the various animal attributes using scatter plots and marginal histograms.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import pandas as pd
                import numpy as np
                import matplotlib.pyplot as plt
                %matplotlib inline
                """
            ),
            md("#### Loading the dataset"),
            code("data = pd.read_csv('anage_data.csv')"),
            md("#### Preprocessing"),
            md(
                """
                Filter the data so that you end up with samples containing a body mass and a maximum longevity. Select all the samples of the Aves class with a body mass smaller than 20,000.
                """
            ),
            code(
                """
                longevity = 'Maximum longevity (yrs)'
                mass = 'Body mass (g)'
                data = data[np.isfinite(data[longevity]) & np.isfinite(data[mass])]
                aves = data[(data['Class'] == 'Aves') & (data[mass] < 20000)]
                """
            ),
            md("#### Scatter plot with marginal histograms using GridSpec"),
            code(
                """
                fig = plt.figure(figsize=(8, 8), dpi=150, constrained_layout=True)
                gs = fig.add_gridspec(4, 4)
                histx_ax = fig.add_subplot(gs[0, :-1])
                histy_ax = fig.add_subplot(gs[1:, -1])
                scatter_ax = fig.add_subplot(gs[1:, :-1])
                scatter_ax.scatter(aves[mass], aves[longevity])
                histx_ax.hist(aves[mass], bins=20, density=True)
                histx_ax.set_xticks([])
                histy_ax.hist(aves[longevity], bins=20, density=True, orientation='horizontal')
                histy_ax.set_yticks([])
                scatter_ax.set_xlabel('Body mass in grams')
                scatter_ax.set_ylabel('Maximum longevity in years')
                fig.suptitle('Scatter plot with marginal histograms')
                plt.show()
                """
            ),
        ]
    )


def make_activity_607():
    return notebook(
        [
            md("## Activity 6.07: Plotting Multiple Images in a Grid"),
            md(
                """
                In this activity, we will plot images in a grid. You are a developer in a social media company. Management has decided to add a feature that helps the customer to upload images in a 2x2 grid format. Develop some standard code to generate grid-formatted images.
                """
            ),
            md("#### Import statements"),
            code(
                """
                import os
                import numpy as np
                import matplotlib.pyplot as plt
                import matplotlib.image as mpimg
                %matplotlib inline
                """
            ),
            md("#### Loading images"),
            code(
                """
                img_filenames = sorted(os.listdir('images'))
                imgs = [mpimg.imread(os.path.join('images', img_filename))
                        for img_filename in img_filenames]
                img_filenames
                """
            ),
            md("#### Visualize the images in a 2x2 grid"),
            code(
                """
                fig, axes = plt.subplots(2, 2)
                fig.set_size_inches(6, 6)
                fig.set_dpi(150)
                axes = axes.ravel()
                labels = ['coast', 'beach', 'building', 'city at night']
                for i in range(len(imgs)):
                    axes[i].imshow(imgs[i])
                    axes[i].set_xticks([])
                    axes[i].set_yticks([])
                    axes[i].set_xlabel(labels[i])
                plt.show()
                """
            ),
        ]
    )


MAKERS = {
    "Exercise6.01": make_exercise_601,
    "Activity6.01": make_activity_601,
    "Activity6.02": make_activity_602,
    "Exercise6.02": make_exercise_602,
    "Activity6.03": make_activity_603,
    "Activity6.04": make_activity_604,
    "Activity6.05": make_activity_605,
    "Exercise6.03": make_exercise_603,
    "Exercise6.04": make_exercise_604,
    "Activity6.06": make_activity_606,
    "Activity6.07": make_activity_607,
}


def copy_data(notebook_key: str, dest: Path):
    for item in DATA_BY_NOTEBOOK[notebook_key]:
        src = DATA / item
        if not src.exists():
            raise FileNotFoundError(f"Missing dataset: {src}")
        target = dest / item
        if src.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(src, target)
        else:
            shutil.copy2(src, target)


def fig_to_png_b64():
    figs = list(map(plt.figure, plt.get_fignums()))
    images = []
    for fig in figs:
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight", dpi=150)
        buf.seek(0)
        images.append(base64.b64encode(buf.read()).decode("ascii"))
    plt.close("all")
    return images


def execute_notebook(nb, workdir: Path):
    ns = {"__name__": "__main__"}
    os.chdir(workdir)
    count = 1
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        source = "".join(cell.source)
        cleaned = "\n".join(
            line for line in source.splitlines() if not line.strip().startswith("%")
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        outputs = []
        try:
            from contextlib import redirect_stderr, redirect_stdout

            with redirect_stdout(stdout), redirect_stderr(stderr):
                result = eval_or_exec(cleaned, ns)
            text = stdout.getvalue()
            if text:
                outputs.append(new_output("stream", name="stdout", text=text))
            err = stderr.getvalue()
            if err:
                outputs.append(new_output("stream", name="stderr", text=err))
            if result is not None:
                outputs.append(
                    new_output(
                        "execute_result",
                        data={"text/plain": repr(result)},
                        metadata={},
                        execution_count=count,
                    )
                )
        except Exception as exc:
            outputs.append(
                new_output(
                    "error",
                    ename=type(exc).__name__,
                    evalue=str(exc),
                    traceback=[str(exc)],
                )
            )
        for png in fig_to_png_b64():
            outputs.append(
                new_output(
                    "display_data",
                    data={"image/png": png, "text/plain": ["<Figure>"]},
                    metadata={},
                )
            )
        cell["outputs"] = outputs
        cell["execution_count"] = count
        count += 1
    return nb


def eval_or_exec(source: str, ns: dict):
    tree = None
    try:
        import ast

        tree = ast.parse(source, mode="exec")
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            *body, last = tree.body
            if body:
                exec(compile(ast.Module(body, type_ignores=[]), "<cell>", "exec"), ns)
            return eval(compile(ast.Expression(last.value), "<cell>", "eval"), ns)
        exec(compile(tree, "<cell>", "exec"), ns)
        return None
    except Exception:
        exec(source, ns)
        return None


def folder_for(practice: str) -> Path:
    return PKG / practice / "Jupyter Notebooks"


def shots_for(practice: str) -> Path:
    return PKG / practice / "Screen Shots"


def extract_plot_screenshots(nb_path: Path, shot_dir: Path, stem: str):
    nb = nbformat.read(nb_path, as_version=4)
    n = 0
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        for out in cell.get("outputs", []):
            png = None
            if out.get("output_type") in {"display_data", "execute_result"}:
                png = out.get("data", {}).get("image/png")
            if png:
                n += 1
                raw = base64.b64decode(png)
                out_path = shot_dir / f"{stem}_step{n:02d}.png"
                out_path.write_bytes(raw)
    return n


def make_folder_screenshot(practice: str, dest: Path):
    from PIL import Image, ImageDraw, ImageFont

    folder = PKG / practice
    lines = [f"CISC7204 Suggested Exercise 06  |  {practice}  |  Student {SID}", ""]
    for root, dirs, files in os.walk(folder):
        dirs.sort()
        files = [f for f in files if not f.startswith(".")]
        files.sort()
        rel = os.path.relpath(root, folder)
        indent = 0 if rel == "." else rel.count(os.sep) + 1
        name = practice if rel == "." else Path(root).name
        lines.append("    " * indent + f"{name}/")
        for f in files:
            size = os.path.getsize(os.path.join(root, f))
            lines.append("    " * (indent + 1) + f"{f}   ({size:,} bytes)")

    width = 1400
    line_h = 28
    height = 80 + line_h * (len(lines) + 2)
    img = Image.new("RGB", (width, height), "#1e1e1e")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18)
        title_font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 20)
    except Exception:
        font = ImageFont.load_default()
        title_font = font
    y = 24
    for i, line in enumerate(lines):
        color = "#dcdcaa" if i == 0 else "#d4d4d4"
        draw.text((28, y), line, fill=color, font=title_font if i == 0 else font)
        y += line_h
    path = dest / f"{SID}_{practice}_folder.png"
    img.save(path)
    return path


def make_notebook_overview(nb_path: Path, dest: Path, stem: str):
    from PIL import Image, ImageDraw, ImageFont

    nb = nbformat.read(nb_path, as_version=4)
    title = ""
    steps = []
    plots = []
    for cell in nb.cells:
        src = "".join(cell.source).strip()
        if cell.cell_type == "markdown" and src.startswith("## "):
            title = src.splitlines()[0][3:]
        if cell.cell_type == "code":
            first = next((ln for ln in src.splitlines() if ln.strip() and not ln.startswith("%")), "")
            if first:
                steps.append(first[:90])
            for out in cell.get("outputs", []):
                png = out.get("data", {}).get("image/png") if out.get("output_type") in {"display_data", "execute_result"} else None
                if png:
                    plots.append(Image.open(io.BytesIO(base64.b64decode(png))).convert("RGB"))

    width = 1600
    header_h = 160 + 22 * min(len(steps), 8)
    plot_w = 720
    row_h = 420
    rows = max(1, (len(plots) + 1) // 2)
    height = header_h + rows * row_h + 40
    img = Image.new("RGB", (width, height), "#ffffff")
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
        big = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
        small = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 15)
    except Exception:
        font = ImageFont.load_default()
        big = font
        small = font
    draw.rectangle((0, 0, width, 64), fill="#0b57d0")
    draw.text((24, 18), f"Jupyter Notebook  |  {SID}_{stem}.ipynb", fill="white", font=big)
    draw.text((24, 80), title, fill="#1a1a1a", font=font)
    draw.text((24, 110), "Completed steps (code cells executed):", fill="#333333", font=font)
    y = 140
    for i, step in enumerate(steps[:8], 1):
        draw.text((36, y), f"In [{i}]: {step}", fill="#333333", font=small)
        y += 22
    y = header_h
    for i, plot in enumerate(plots):
        col = i % 2
        row = i // 2
        x = 30 + col * (plot_w + 40)
        yy = y + row * row_h
        plot.thumbnail((plot_w, row_h - 30))
        img.paste(plot, (x, yy))
    path = dest / f"{SID}_{stem}_notebook.png"
    img.save(path)
    return path


def ensure_seaborn_tips():
    cache = Path.home() / "seaborn-data"
    cache.mkdir(exist_ok=True)
    src = DATA / "tips.csv"
    dst = cache / "tips.csv"
    if src.exists():
        shutil.copy2(src, dst)


def main():
    ensure_seaborn_tips()
    if PKG.exists():
        shutil.rmtree(PKG)
    for practice in PRACTICES:
        folder_for(practice).mkdir(parents=True)
        shots_for(practice).mkdir(parents=True)

    makers = MAKERS
    errors = []
    for practice, keys in PRACTICES.items():
        nb_dir = folder_for(practice)
        shot_dir = shots_for(practice)
        for key in keys:
            print(f"Building {key} ...", flush=True)
            copy_data(key, nb_dir)
            nb = makers[key]()
            fname = f"{SID}_{key}.ipynb"
            path = nb_dir / fname
            executed = execute_notebook(nb, nb_dir)
            # fail if any error outputs
            for cell in executed.cells:
                if cell.cell_type != "code":
                    continue
                for out in cell.get("outputs", []):
                    if out.get("output_type") == "error":
                        errors.append(f"{key}: {out.get('evalue')}")
            nbformat.write(executed, path)
            n = extract_plot_screenshots(path, shot_dir, f"{SID}_{key}")
            make_notebook_overview(path, shot_dir, key)
            print(f"  wrote {path.name} with {n} plot screenshot(s)", flush=True)
        make_folder_screenshot(practice, shot_dir)
        print(f"Finished {practice}", flush=True)

    if errors:
        raise RuntimeError("Notebook errors:\n" + "\n".join(errors))

    zip_base = ROOT / f"cisc7204_sugex06_{SID}"
    shutil.make_archive(str(zip_base), "zip", ROOT, PKG.name)
    print(f"Created {zip_base}.zip")


if __name__ == "__main__":
    main()
