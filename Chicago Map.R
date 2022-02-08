
library("tidyverse")
library("ggplot2")

read_csv("Projects/pdLoctations.xlsx")


library(sf)

chi_map <- read_sf("https://raw.githubusercontent.com/thisisdaryn/data/master/geo/chicago/Comm_Areas.geojson")



ggplot() + 
  geom_sf(data = chi_map, , fill = "ivory", colour = "ivory")  +
  geom_point(data = pdLoctations, aes(x= Longitude, y= Latitude, color = Category)) 
+ scale_color_viridis_d()

