# %%
def age_group(age):  
       if age < 18: return "Young"
       elif age >=18 & i age < 35: return "Young Adult"
       elif age >= 35 & age < 60: return "Adult"
       elif age >= 60: return "Old"

plot1 = (
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

# %%
