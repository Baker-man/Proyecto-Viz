#función para generar mapa base centrado sobre mi zona de estudio
def generateBaseMap(default_location=[40.416729, -3.703339], default_zoom_start=11):
    
    base_map = folium.Map(location=default_location, 
                          control_scale=True, 
                          zoom_start=default_zoom_start)
    
    return base_map