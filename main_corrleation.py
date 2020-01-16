import pandas as pd

from Parse.edit_yeshuvim_data import add_yeshuv_type
from Questions.corrleation import calculate_corrleation


def clean_missing_data(yeshuvim):
    yeshuvim.dropna(inplace=True)





yeshuvim = pd.read_csv("Data/yeshovim.csv")
clean_missing_data(yeshuvim)
add_yeshuv_type(yeshuvim)
calculate_corrleation(yeshuvim)
