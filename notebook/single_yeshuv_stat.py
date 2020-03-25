from constants import KNESSETS_LIST

# used mainly for exploration of single yeshuv data.

def stats_population_kneset_df_single_yeshuv(kneset_data, yeshuv_sn : int):
    yeshuv_stats_dict = {}
    for knesset in KNESSETS_LIST:
        yeshuv_per_knesset_dict = {}
        df = kneset_data.get_kneset_data(knesset)
        result_per_yeshuv_df = df.loc[df[
                          'SN'] == yeshuv_sn]

        yeshuv_per_knesset_dict['BZB'] = result_per_yeshuv_df['BZB'].sum()
        yeshuv_per_knesset_dict['Voters']  = result_per_yeshuv_df['Voters'].sum()
        yeshuv_per_knesset_dict['vote_percent'] = yeshuv_per_knesset_dict['Voters'] / yeshuv_per_knesset_dict['BZB']
        yeshuv_per_knesset_dict['Num_Klafi'] = len(result_per_yeshuv_df['SN'])
        yeshuv_per_knesset_dict['Error_Voters'] = len(result_per_yeshuv_df['Error_Voters'])

        yeshuv_stats_dict[knesset] = yeshuv_per_knesset_dict

    # TODO: best worst kalfi with kalfi address
    # best/worst kalfi ?

    # yeshuv_stats_dict["overall"]["Yeshuv_Type"] = result_per_yeshuv_df['Yeshuv_Type']



    # population_stats = calculate_bzb_vote_percent_pearson(
    #     knesset_df['BZB'],
    #     knesset_df[
    #         'vote_percent'])


    #
    # filtered_population_stats = PopulationInfo(num_kalfi_total,
    #                                            num_unique_yeshuvim, total_bzb,
    #                                            total_voters, population_stats)


