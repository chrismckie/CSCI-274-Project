import python.data_processing as process
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter, MultipleLocator
from datetime import date

def create_gantt_chart(df, start_min_col, end_min_col, width_col, interval_col, title, x_label, y_label):
    
    # Define figure and axis
    fig, ax = plt.subplots(figsize=(12,8))

    # Set labels
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Set y values on graph 
    y_pos = np.arange(len(df))
    ax.barh(
        y=y_pos, 
        left=df[start_min_col], 
        width=df[width_col]
    )
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df[interval_col])

    # Set x values on graph
    xmin = df[start_min_col].min()
    xmax = df[end_min_col].max()
    ax.set_xlim(xmin, xmax)

    # Set ticks every hour
    ax.xaxis.set_major_locator(MultipleLocator(60))
    ax.xaxis.set_major_formatter(FuncFormatter(process.min_to_hhmm))

    # Adjust layout
    plt.tight_layout()

    return fig

def create_bar_chart(df, selected_df, title, x_label_1, x_label_2, y_label):
    # Create bar chart: Jobs selected vs jobs available
    total_jobs = len(df)
    selected_jobs = len(selected_df)
    x_labels = [x_label_1, x_label_2]
    values = [total_jobs, selected_jobs]

    fig, ax = plt.subplots(figsize=(5,4))

    # Chart lables
    ax.set_title(title)
    ax.bar(x_labels,values)
    ax.set_ylabel(y_label)
    
    for i, v in enumerate(values):
        ax.text(i, v + 0.5, str(v), ha="center", fontsize=10)

    # Adjust layout
    plt.tight_layout()

    return fig