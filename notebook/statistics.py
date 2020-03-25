from pandas import Series
from scipy import stats

from notebook.correlation import prepare_new_yeshuv_types_for_scatter_plot


def is_normal_dist(series: Series):
    k2, p = stats.normaltest(series)
    alpha = 1e-3
    print("p = {:g}".format(p))
    print("k2 = {:g}".format(k2))
    p = 3.27207e-11
    if p < alpha:  # null hypothesis: x comes from a normal distribution
        print("The null hypothesis can be rejected")
    else:
        print("The null hypothesis cannot be rejected")



def test_for_normal_dist(series: Series):
    series.plot.hist()
    is_normal_dist(series) #return pvalue -= 0 meanning not from normal dist.

    #another method, qq plot
    import statsmodels.api as sm
    sm.qqplot(series, line='45')
    import pylab
    pylab.show()
    # another method km test
    from scipy.stats import kstest, norm
    ks_statistic, p_value = kstest(series, 'norm')
    print(ks_statistic, p_value)


    small_arab = df[df["Yeshuv_Type"] == "Small Arab Yeshuv"]
    from scipy.stats import anderson
    result = anderson(series)
    print('Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print(
                '%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
        else:
            print(
                '%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))

df= kneset_data.get_kneset_data("22")
# transform yeshuv types to fewer population groups.
prepare_new_yeshuv_types_for_scatter_plot(df)
bzb = df["BZB"]
test_for_normal_dist(bzb)

vote =  df["Vote_Percent"]
test_for_normal_dist(vote)

