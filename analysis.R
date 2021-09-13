library(tidyverse)

dat <- read_csv("https://github.com/fivethirtyeight/guns-data/raw/master/full_data.csv")

#bar charts and pie charts aggravates info, its just a sum most of the time, it works for companies and sales. 


#' Used this information to build the values.
# https://www.census.gov/quickfacts/fact/table/US/POP010220

dat_pop <- tibble(
    race = c("Asian/Pacific Islander",  
        "Black",  "Hispanic",  
        "Native American/Native Alaskan",  "White"), 
    N =  331449281 *c(.061, .134, .185, .013, .763))


dat %>%
    group_by(race, year) %>%
    summarise(n=n())
    ungroup()

dat %>%
    count(race, year)
