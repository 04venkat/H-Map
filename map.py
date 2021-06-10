import folium
from folium.map import Icon
import pandas

df = pandas.read_excel("Hospital.xlsx")
map = folium.Map(location = [13, 80])

fgm = folium.FeatureGroup(name = "Marker")

nam = list(df["Name"])
lat = list(df["Lat"])
lon = list(df["Long"])
add = list(df["Address"])
hospt = list(df["Hospital Type"])
ph = list(df["Phone Number"])

def priv_or_gov(ho):
    if ho == "Private":
        return "green"
    else:
        return "red"

for la, lo, ad, ho, ph, na in zip(lat, lon, add, hospt, ph, nam):
    fgm.add_child(folium.CircleMarker(location = [la, lo], fill_color = priv_or_gov(ho), color = "grey",  fill_opacity = 0.9, radius = 10, popup = folium.Popup(f"Name: {na}\t\n\n||\tAddress: {ad}\t||\tPhone Number: +044-{ph}||\tHospital Type: {ho}", max_width = len(f"Address: {ad}")*20)))

map.add_child(fgm)
map.add_child(folium.LayerControl())
map.save("Map.html")