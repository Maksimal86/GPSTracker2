from kivy.garden.mapview import  MapMarker, MapView
from kivy.app import App
from plyer import gps
# from android.permissions import Permission, request_permissions

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=12, lat=56.744658, lon=38.861960)
        marker_home = MapMarker(lat=56.744658, lon=38.861960)
        marker_second = MapMarker(lat=self.update_gps_coordinates,
                                  lon=self.update_gps_coordinates)
        mapview.add_marker(marker_home)
        mapview.add_marker(marker_second)
        return mapview

    # def check_android_permission(self):
    #     permissions = [Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION]
    #     request_permissions(permissions)

    def start_gps(self):
        gps.configure(on_location=self.update_gps_coordinates)
        gps.start(minTime=1000, minDistance=1)
# разобаться с получением GPS


    def update_gps_coordinates(self, **kwargs):
        latitude = kwargs['lat']
        longitude = kwargs['lon']
        print('latitude = ', latitude, 'longitude = ', longitude)
        # self.text_input.text = f'Latitude: {latitude}, Longitude: {longitude}'

MapViewApp().run()