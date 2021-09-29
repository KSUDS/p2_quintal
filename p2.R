
library(tidyverse)
library(ggplot2)
library(ggthemes)
install.packages(viridis)  
library(viridis)

httpgd::hgd()
httpgd::hgd_browse()



dat <- read_csv("https://github.com/fivethirtyeight/guns-data/raw/master/full_data.csv") %>%
    select(-...1)

#mutate age groups
dat <- dat %>%
    mutate(age_group = case_when(
        age < 18 ~ "Young",
        age >= 18 & age < 35 ~ "Young Adult",
        age >= 35 & age < 60 ~ "Adult",
        age >= 60 ~ "Old",
        TRUE ~ "NA"
    ))

#tibble from class
dat_pop <- tibble(
    race = c("Asian/Pacific Islander",  
        "Black",  "Hispanic",  
        "Native American/Native Alaskan",  "White"), 
    N =  331449281 *c(.061, .134, .185, .013, .763))

dat_counts <- dat %>%
    count(race, year, age_group, month, intent)

dat_counts_2 <- dat_counts %>%
    left_join(dat_pop, by="race")

plot1 <- dat_counts_2 %>%
    filter(intent != "NA")

plot1 %>%
    mutate(age_group = fct_relevel(age_group, #looked at cohen code on how to reorder the categories (Young, Young Adult, Old, NA), https://forcats.tidyverse.org/reference/fct_relevel.html
        "Young", "Young Adult","Adult","Old")) %>%
    ggplot(aes(y= n ,x = month, color = race)) +
    geom_point(size = 1) +
    facet_grid(age_group ~ intent)  +
    labs(
    title = "Gun Death Rates by Month",
    caption = "Multiple Cause of Death datafile for FiveThirtyEight's",
    tag = "Figure 1",
    x = "Month",
    y = "Number",
    color = "Race") +
    theme_bw() +
    scale_color_brewer(palette = "Accent") #https://www.datanovia.com/en/blog/top-r-color-palettes-to-know-for-great-data-visualization/

ggsave(file = "GunDeathRate1_Quintal_R.png", width = 15, height = 6)

# Comparing the Gun Death Rates by Month we can see how there is a high number of homicides in black young adults, The highest number of suicides are found in Adults and Old people.

#Since adults has the highest numbers of death we are going to compare it by race, gender, intent, and month

dat %>% # Adult deaths by race
    filter(age_group == "Adult") %>% 
        ggplot(aes(x=intent, fill=race)) + 
        geom_bar() + 
        labs(
        title = "Adult Deaths by Race",
        tag = "Figure 2",
        x = "Intent",
        y = "Number of Deaths",
        legend = "Race",
        color = "Race"
        ) +
        scale_fill_manual("legend", values = c("Asian/Pacific Islander" = "black", "Black" = "orange", "Hispanic" = "blue", "Native American/Native Alaskan" = "green", "White" = "red"))

ggsave(file = "GunDeathRate2_Quintal_R.png", width = 15, height = 6)

# Adult deaths are predominant in white people but this is obvious since it is has the highest population


dat %>% # White Adult Deaths by Sex
    filter(age_group == "Adult", race=="White") %>% 
        ggplot(aes(x=intent, fill=sex)) + 
        geom_bar() +
        labs(
        title = "White Adult Deaths by Sex",
        tag = "Figure 3",
        x = "Intent",
        y = "Number of Deaths",
        legend = "Sex"
        ) +
        scale_fill_manual("legend", values = c("F" = "#911e31", "M" = "#035e039d" ))

ggsave(file = "GunDeathRate3_Quintal_R.png", width = 15, height = 6)

# White Adult male have more deaths than White Adult female

dat %>% # Suicide Rate by Race and Month
    filter(intent == "Suicide") %>% 
        ggplot(aes(x=month, fill=race)) + 
        geom_bar() +
        labs(
        title = "Suicide Rate by Race and Month",
        tag = "Figure 4",
        x = "Month",
        y = "Number of Suicides",
        legend = "Race"   
        ) +
        scale_fill_manual("legend", values = c("Asian/Pacific Islander" = "black", "Black" = "orange", "Hispanic" = "blue", "Native American/Native Alaskan" = "green", "White" = "red"))

ggsave(file = "GunDeathRate4_Quintal_R.png", width = 15, height = 6)

# Suicides rates are evenly distributed among the months with May and July having the highest suicide rate and February having the lowest suicide rate