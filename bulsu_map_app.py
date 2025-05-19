import streamlit as st
import folium
from streamlit_folium import st_folium

# Page title
st.set_page_config(page_title="BulSU Malolos Campus Map", layout="wide")
st.title("🗺️ Bulacan State University – Malolos Campus Map")

# Campus center
campus_center = (14.8441, 120.8115)

# Building data
buildings = [
    {"name": "Gate 1", "college": "Entrance", "description": "Main entrance to BulSU.", "coords": (14.8450, 120.8120)},
    {"name": "CICT", "college": "CICT", "description": "College of ICT", "coords": (14.8445, 120.8112)},
    {"name": "COE", "college": "Engineering", "description": "College of Engineering", "coords": (14.8439, 120.8105)},
    {"name": "Library", "college": "Library", "description": "University Library", "coords": (14.8442, 120.8118)},
    {"name": "Gym", "college": "Athletics", "description": "BulSU Gymnasium", "coords": (14.8437, 120.8123)},
]

# Sidebar filter
college_options = ["All"] + sorted(set(b["college"] for b in buildings))
selected_college = st.sidebar.selectbox("Filter by College", college_options)

filtered = buildings if selected_college == "All" else [b for b in buildings if b["college"] == selected_college]

# Create the map
campus_map = folium.Map(location=campus_center, zoom_start=17, tiles="CartoDB positron")

for b in filtered:
    folium.Marker(location=b["coords"], popup=f"<b>{b['name']}</b><br>{b['description']}",
                  icon=folium.Icon(color="blue", icon="info-sign")).add_to(campus_map)

# Display
st_folium(campus_map, width=1200, height=600)
