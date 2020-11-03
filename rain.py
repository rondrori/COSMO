import folium

# Create a Map instance
m = folium.Map(location=[32, 35], tiles='Stamen Toner',
                   zoom_start=10, control_scale=True)
outfp = "/home/geo/base_map.html"  
# Let's change the basemap style to 'Stamen Toner'
m = folium.Map(location=[32, 35], tiles='Stamen Toner',
                zoom_start=12, control_scale=True, prefer_canvas=True)

# Filepath to the output
outfp = "/home/geo/base_map2.html"

# Save the map
m.save(outfp)
