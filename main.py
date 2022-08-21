import csv

from go_utils import get_api_data
from go_utils.constants import landcover_protocol, mosquito_protocol
from go_utils.filtering import filter_invalid_coords

out_dir = "GLOBE-Clean-Datasets/General/"

mhm_df = get_api_data(mosquito_protocol)
mhm_df = filter_invalid_coords(mhm_df, "mhm_Latitude", "mhm_Longitude", True)
mhm_df.to_csv(
    f"{out_dir}/Clean_MHM.csv",
    sep=",",
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_ALL,
    quotechar='"',
    escapechar="”",
)

lc_df = get_api_data(landcover_protocol)
lc_df = filter_invalid_coords(lc_df, "lc_Latitude", "lc_Longitude", True)
lc_df.to_csv(
    f"{out_dir}/Clean_LC.csv",
    sep=",",
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_ALL,
    quotechar='"',
    escapechar="”",
)
