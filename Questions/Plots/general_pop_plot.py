import pandas as pd
from matplotlib import pyplot as plt


def graph_avg_bzb_vote_percent(x, avg_bzb_per_kalfi_list, vote_percent_list):
    df = pd.DataFrame({'Kneset': x,
                       'Avg_bzb': avg_bzb_per_kalfi_list,
                       'Vote_percent': vote_percent_list})

    fig, ax1 = plt.subplots()
    fig.suptitle('Average BZB per Kalfi and Vote %', y=1)
    color = 'tab:red'
    ax1.set_xlabel('Kneset')
    ax1.set_ylabel('Avg BZB per Kalfi', color=color, rotation='horizontal',
                   horizontalalignment='left', fontsize='small',
                   position=(0, 0.465))
    ax1.plot(x, avg_bzb_per_kalfi_list, 'r--', label="bzb")
    ax1.tick_params(axis='y', labelcolor=color, labelsize=10)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Vote %', color=color, rotation='horizontal',
                   fontsize='small')
    ax2.plot(x, vote_percent_list, 'c-.')
    ax2.tick_params(axis='y', labelcolor=color, labelsize=10)

    # add grids
    fig.tight_layout()
    plt.grid(True, axis="both", linestyle='--', linewidth=1, which='both')

    font = {'family': 'serif',
            'color': 'royalblue',
            'weight': 'semibold',
            'size': 9
            }
    # add value points for ax2 (vote percent )
    ax2.text("18", vote_percent_list[0] - 0.0025,
             str(round(vote_percent_list[0], 2)) + '%', ha="left",
             fontdict=font)

    ax2.text("19", vote_percent_list[1],
             str(round(vote_percent_list[1], 2)) + '%', ha="right",
             fontdict=font)

    ax2.text("20", vote_percent_list[2],
             str(round(vote_percent_list[2], 2)) + '%', ha="center",
             fontdict=font)

    ax2.text("21", vote_percent_list[3] - 0.0023,
             str(round(vote_percent_list[3], 2)) + '%', ha="center",
             fontdict=font)

    ax2.text("22", vote_percent_list[4] + 0.001,
             str(round(vote_percent_list[4], 2)) + '%', ha="center",
             fontdict=font)
    plt.show()


def graph_general_stat(x, bzb_per_kalfi_list, num_kalfi_list, unique_yeshuv,
                       voters_list):
    fig, axs = plt.subplots(2, 2, gridspec_kw={'hspace': 0.35, 'wspace': 0.4})
    fig.suptitle('General Knesset Elections Info', va='top')

    color = 'tab:red'
    # ax1.set_ylabel('BZB', color=color)
    axs[0, 0].semilogy(x, bzb_per_kalfi_list, 'r--', label="bzb")
    axs[0, 0].set_title('BZB')
    # ax1.tick_params(axis='y', labelcolor=color)

    color = 'tab:blue'
    # ax2.set_ylabel('Voters', color=color)
    axs[0, 1].semilogy(x, voters_list, 'c-.')
    axs[0, 1].set_title('Voters')
    # ax2.tick_params(axis='y', labelcolor=color)

    color = 'tab:pink'
    # ax3.set_ylabel('Kalfi\'s', color=color)
    axs[1, 0].plot(x, num_kalfi_list, 'm-')
    # ax3.tick_params(axis='y', labelcolor=color)
    axs[1, 0].set_title('Kalfi\'s')
    axs[1, 0].set(xlabel='Kneset')
    # axs[1, 0].tick_params(axis='y', labelcolor=color, labelsize=6)
    color = 'tab:green'
    # ax4.set_ylabel('Yeshuvim\'s', color=color)
    axs[1, 1].plot(x, unique_yeshuv, 'g:')
    # ax4.tick_params(axis='y', labelcolor=color)
    # ax4.set_xlabel('Kneset')
    axs[1, 1].set_title('Yeshuvim\'s')
    # fig.tight_layout()
    axs[1, 1].set(xlabel='Kneset')
    # axs[1, 1].tick_params(axis='y', labelcolor=color, labelsize=6)
    plt.show()