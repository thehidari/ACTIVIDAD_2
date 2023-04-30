#Grafica de mapas
import numpy as np
import pandas as pd 
import folium
m = folium.Map(location=[-12.0431800, -77.0282400], zoom_start=12, tiles='Stamen Terrain')
m.show_in_browser()