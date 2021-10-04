# %%
import pandas as pd
import numpy as np

# %%
year = 2013
url = "ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/mort2013us.zip"




# %%
raw_file = pd.read_fwf("data/mort2013us.zip", nrows = 1000, compression="zip", header = None, names = format_names, widths = format_widths)
# %%
raw_file = pd.read_fwf("data/mort2013us.zip", nrows = 1000, compression="zip", header = None, names = format_names, widths = format_widths)

# %%
import pandas as pd
import numpy as np
# %%
year = 2013
url =  "ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/mort2013us.zip"

l2 = str(year)[2:]
fnames = ["deaths", "guns", "suicide"]

# leave for later
pd.DataFrame({

})

format_widths = [19,1,40,2,1,1,2,2,1,4,1,2,2,2,2,1,1,1,16,4,1,1,1,1,34,1,1,4,3,1,3,3,2,1,281,1,2,1,1,1,1,33,3,1,1]

format_names = ["drop1", "res_status", "drop2", "education_89", "education_03", "education_flag", "month",  "drop3", "sex", "detail_age", "age_flag", "age_recode", "age_recode2", "age_group", "age_infant", "death_place", "marital", "day_of_week", "drop4", "data_year", "at_work",  "death_manner", "burial", "autopsy", "drop5", "activity", "injury_place", "underlying_cause", "cause_recode358", "drop6", "cause_recode113", "cause_recode130", "cause_recode39", "drop7", "multiple_causes", "drop8", "race", "race_bridged", "race_flag", "race_recode", "race_recode2", "drop9", "hispanic", "drop10", "hispanic_recode"]
# %%
# check to read all lines at the end
# using local file but want to use URL
raw_file = pd.read_fwf("data/mort2013us.zip", nrows = 1000, compression="zip", header=None, names = format_names, widths = format_widths)

# %%
drop_names = raw_file.filter(regex="drop").columns

raw_file = raw_file.drop(drop_names, axis=1)

# %%
# suicide_code <- c(stringr::str_c("X", 60:84), "U03", "Y870")
suicide_code = ["X" + str(i) for i in range(60, 85)] + ["U03", "Y870"]

suicide = raw_file.query('underlying_cause in @suicide_codes').assign(
        gun = lambda x: np.where(x.underlying_cause.isin(["X72", "X73", "X74"]),1,0), year = year)
    gun_codes = ["W32", "W33", "W34", "X72", "X73", "X74", "U014","X93", "X94", "X95", "Y22", "Y23", "Y24", "Y350"]
    intent_conditions = [
        (raw_file.underlying_cause.isin(["W32", "W33", "W34"])),
        (raw_file.underlying_cause.isin(["X72", "X73", "X74"])),
        (raw_file.underlying_cause.isin(["*U01.4", "X93", "X94", "X95","Y350"])),
        (raw_file.underlying_cause.isin(["Y22", "Y23", "Y24"]))
    ]
    intent_names = ["Accidental", "Suicide", "Homicide", "Undetermined"]

    weapon_conditions = [
        (raw_file.underlying_cause.isin(["W32", "X72", "X93", "Y22"])),
        (raw_file.underlying_cause.isin(["W33", "X73", "X94", "Y23"]))
    ]
    weapon_names  = ["Handgun", "Rifle etc"]

# %%
age_conditions = [(round(raw_file.detail_age/1000,1)==1),(round(raw_file.detail_age/1000,1)==2),(raw_file.detail_age==9999)]
age_values = [(raw_file.detail_age-1000),("NA"),("NA_real_")]
guns = raw_file.assign(
    intent = np.select(intent_conditions, intent_names, default = np.nan),
    police = lambda x: np.where(x.underlying_cause=="Y350",1,0),
    weapon = np.select(weapon_conditions, weapon_names, default = "Other/unknown"),
    age = np.select(age_conditions,age_values,default = 0),
    year=year).query('underlying_cause in @gun_codes')

)
# %%
suicide.to_pickle(tnames.query('start_name == "suicide"').file_path_pickle.to_numpy()[0])
guns.to_pickle(tnames.query('start_name == "guns"').file_path_pickle.to_numpy()[0])
raw_file.to_pickle(tnames.query('start_name == "deaths"').file_path_pickle.to_numpy()[0])

#%%
parse_cdc(2013,"ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/mort2013us.zip","death_data")
parse_cdc(2014,"ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/mort2014us.zip","death_data")
parse_cdc(2012,"ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/DVS/mortality/mort2012us.zip","death_data")

#%%
