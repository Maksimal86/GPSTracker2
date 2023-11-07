import tkinter
import tkintermapview
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from android.permissions import Permission, request_permissions
from plyer import gps


root_tk = tkinter.Tk() # создать окно tkinter.Tk()
root_tk.geometry(f"{800}x{800}")
root_tk.title("example.py")

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=800, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

class GPSApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.text_input = TextInput()
        layout.add_widget(self.text_input)
        # self.mapview = MapView()
        layout.add_widget(self.mapview)
        self.check_android_permission()
        self.start_gps()
        return layout


def check_android_permission(self):
    permissions = [Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION]
    request_permissions(permissions)


def start_gps(self):
    gps.configure(on_location=self.update_gps_coordinates)
    gps.start(minTime=1000, minDistance=0)


def update_gps_coordinates(self, **kwargs):
    latitude = kwargs['lat']
    longitude = kwargs['lon']
    self.text_input.text = f'Latitude: {latitude}, Longitude: {longitude}'


def create_map_widget(latitude_car,longitude_car, text):
    return map_widget.set_marker(latitude_car,longitude_car,text='Home')


def set_position_of_map(latitude_map,longitude_map):
    map_widget.set_position(latitude_map,longitude_map)    # дом
    map_widget.set_zoom(15)


def main():
    gps = GPSApp()
    gps.check_android_permission()
    gps.start_gps()
    create_map_widget(update_gps_coordinates()[0], update_gps_coordinates()[1], text='Home')
    set_position_of_map(update_gps_coordinates()[0], update_gps_coordinates()[1])


GPSApp().run()
root_tk.mainloop()