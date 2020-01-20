from matplotlib import pyplot as plt


def get_plot_idx_by_threshold(threshold):
    plot_title = "{}+ BZB".format(threshold)
    if threshold == 150:
        return 0, 0, plot_title
    elif threshold == 200:
        return 0, 1, plot_title
    elif threshold == 250:
        return 0, 2, plot_title
    elif threshold == 300:
        return 1, 0, plot_title
    elif threshold == 350:
        return 1, 1, plot_title
    elif threshold == 400:
        return 1, 2, plot_title
    elif threshold == 450:
        return 2, 0, plot_title
    elif threshold == 500:
        return 2, 1, plot_title
    elif threshold == 550:
        return 2, 2, plot_title


def add_to_plot(threshold, bzb, vote_percent, axs):
    i, j, plot_title = get_plot_idx_by_threshold(threshold)
    axs[i, j].scatter(bzb, vote_percent, alpha=0.5)
    axs[i, j].set_title(plot_title, fontsize=10)


def plot_all_scatter(threshold_kneset_dict_rang):
    kneset_num = "18"
    # fig, (ax150, ax200, ax250, ax300, ax350, ax400, ax450, ax500,
    #       ax550) = plt.subplots(9, sharex=True)
    fig, axs = plt.subplots(3, 3, sharex='col', sharey='row',
                            gridspec_kw={'hspace': 0.15, 'wspace': 0.15})
    fig.suptitle('Voting % By Kalfi BZB ')
    for threshold, v in threshold_kneset_dict_rang.items():
        bzb_per_kalfi_result = threshold_kneset_dict_rang[threshold]
        single_kneset_dict = bzb_per_kalfi_result.get_single_kneset_dict(
            kneset_num)
        bzb = single_kneset_dict["data"]["BZB"]
        vote_percent = single_kneset_dict["data"]["vote_percent"]
        add_to_plot(threshold, bzb, vote_percent, axs)

        # for ax in axs.flat:
        #     ax.label_outer()

    plt.show()


def scatter_plot_population(kneset_df: pd.DataFrame) -> None:
    x = kneset_df['BZB']
    y = kneset_df['vote_percent']
    plt.scatter(x, y, alpha=0.5)
    plt.title('vote percent by BZB')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
