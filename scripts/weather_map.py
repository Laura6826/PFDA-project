# scripts/weather_map.py

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def create_static_weather_map():
    # Create a figure and an axis with a specific projection
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})

    # Add coastlines and borders
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Add markers for the weather stations
    weather_stations = {
        'Roches Point': (51.789, -8.247),
        'Sherkin Island': (51.466, -9.433),
        'Moorepark': (52.160, -8.267)
    }

    for station, (lat, lon) in weather_stations.items():
        ax.plot(lon, lat, marker='o', color='red', markersize=8, transform=ccrs.PlateCarree())
        ax.text(lon + 0.1, lat, station, transform=ccrs.PlateCarree(), fontsize=12, verticalalignment='center')

    # Set the extent of the map
    ax.set_extent([-10.5, -5, 51, 55], crs=ccrs.PlateCarree())

    # Add gridlines
    ax.gridlines(draw_labels=True)

    # Save the map to a file
    plt.savefig('PFDA-project/images/static_weather_stations_map.png')

    # Show the map
    plt.show()


