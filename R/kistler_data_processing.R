library(tidyverse)
library(dplyr)
library(readr)

raw_data_sens <- read.csv('data/processed_data/Medusa_02/detonation/firing_05/Medusa_02_detonation_05.csv')

processed_data_sens <-  raw_data_sens 

min_value <- min(processed_data_sens$s)
# max_value <- max(processed_data_sens$pC)

processed_data_sens$s <- processed_data_sens$s - min_value

# Find the row with the maximum pC value
# max_row <- processed_data_sens[which.max(processed_data_sens$pC), ]

# Extract the time (s) corresponding to the maximum pC
# time_at_max_pC <- max_row$s

max_t <- 4.75#4.45
min_t <- 3.55

processed_data_sens <- processed_data_sens |>
  filter(s <= max_t ) |>
  filter(s >= min_t)

#min_value <- min(processed_data_sens$s)
#processed_data_sens$s <- processed_data_sens$s - min_value

ggplot(processed_data_sens, aes(x = s, 
                                y = pC))+
  geom_path()+
  theme_minimal()

write_csv(processed_data_sens, "data/processed_data/Medusa_02/detonation/firing_05/Medusa_02_detonation_05_complete.csv")
