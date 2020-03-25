import plot_helper
from plot_helper import PlotType


def __add_labels(ax, boxplot):

    # Grab the relevant Line2D instances from the boxplot dictionary
    iqr = boxplot['boxes'][0]
    caps = boxplot['caps']
    med = boxplot['medians'][0]
    fly = boxplot['fliers'][0]

    # The x position of the median line
    xpos = med.get_xdata()

    # Lets make the text have a horizontal offset which is some
    # fraction of the width of the box
    xoff = 0.10 * (xpos[1] - xpos[0])

    # The x position of the labels
    xlabel = xpos[1] + xoff

    # The median is the y-position of the median line
    median = med.get_ydata()[1]

    # The 25th and 75th percentiles are found from the
    # top and bottom (max and min) of the box
    pc25 = iqr.get_ydata().min()
    pc75 = iqr.get_ydata().max()

    # The caps give the vertical position of the ends of the whiskers
    capbottom = caps[0].get_ydata()[0]
    captop = caps[1].get_ydata()[0]

    # Make some labels on the figure using the values derived above
    ax.text(xlabel, median,
            'Median = {:6.3g}%'.format(median), va='center')
    ax.text(xlabel, pc25,
            '25th percentile = {:6.3g}%'.format(pc25), va='center')
    ax.text(xlabel, pc75,
            '75th percentile = {:6.3g}%'.format(pc75), va='center')
    ax.text(xlabel, capbottom,
            'Bottom cap = {:6.3g}%'.format(capbottom), va='center')
    ax.text(xlabel, captop,
            'Top cap = {:6.3g}%'.format(captop), va='center')


def __set_axes_design_by_pt(ax, pt: PlotType):
    if pt == PlotType.Error:
        ax.set_title('Klafis Error Votes Percent BoxPlot')
        ax.set_ylim((-1, 6))



def __get_filter_df_outliers(df,outlier_threshold, pt: PlotType):
    error_outliers_df = df[df[pt.value] > outlier_threshold]
    return error_outliers_df


def __get_cap_threshold(boxplot):
    caps = boxplot['caps']
    cap_threshold = caps[1].get_ydata()[0]
    return cap_threshold

def __explore_outliers(df, boxplot, pt: PlotType):
    #outliers
    outliers_df = __get_filter_df_outliers(df, __get_cap_threshold(boxplot))
    #Number of outliers:
    len(outliers_df)
    outliers_df.sort_values(by=[pt.value], ascending=False, inplace = True)
    #number sunique yeshuvs:
    len(outliers_df["SN"].unique())
    utliers_df_value_count = outliers_df["Yeshuv"].value_counts()
    print(utliers_df_value_count.head(50))
    # non jew part
    otulier_non_jew = outliers_df[outliers_df.apply(
        lambda x: x['Yeshuv_Type'] in plot_helper.NON_JEW_YESHUVS, axis=1)]
    len(otulier_non_jew)
    value_count_small_non_jew = otulier_non_jew["Yeshuv"].value_counts()
    len(otulier_non_jew["Yeshuv"].unique())
    print(value_count_small_non_jew.head(25))


def create_boxplot(df, pt: PlotType):
    #boxplot
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    __set_axes_design_by_pt(ax, pt)
    boxplot = ax.boxplot(df.Error_Percent)
    __add_labels(ax, boxplot)
    __explore_outliers()

