import pandas as pd
import plotly.express as px
import streamlit as st

# Displaying title and text
st.title("Amsterdam AirBnB Listings Data and visualization")
st.markdown("The AirBnB dataset was cleaned and formated into this datarame.")

# Reading the dataframe
dataframe = pd.read_csv(
    "Amsterdam_Airbnb_listings.csv",
    names=[
        "Airbnb Listing ID",
        "Price",
        "Latitude",
        "Longitude",
        "Meters from chosen location",
        "Location",
    ],
)

# Considering a limited budget, I excluded
# listings with a price above 100 pounds per night
dataframe = dataframe[dataframe["Price"] <= 100]

# Displaying as integer
dataframe["Airbnb Listing ID"] = dataframe["Airbnb Listing ID"].astype(int)
# Round of values
dataframe["Price"] = "£ " + dataframe["Price"].round(2).astype(str)
# Rename the number to a string
dataframe["Location"] = dataframe["Location"].replace(
    {1.0: "To visit", 0.0: "Airbnb listing"}
)

# Displaying the dataframe and text
st.dataframe(dataframe)
st.markdown("Below is a map showing all the Airbnb listings with a red dot and the location we've chosen with a blue dot.")

# Creating the plotly express figure
fig = px.scatter_mapbox(
    dataframe,
    lat="Latitude",
    lon="Longitude",
    color="Location",
    color_discrete_sequence=["blue", "red"],
    zoom=11,
    height=500,
    width=800,
    hover_name="Price",
    hover_data=["Meters from chosen location", "Location"],
    labels={"color": "Locations"},
)
fig.update_geos(center=dict(lat=dataframe.iloc[0][2], lon=dataframe.iloc[0][3]))
fig.update_layout(mapbox_style="stamen-terrain")

# Showing the figure
st.plotly_chart(fig, use_container_width=True)
