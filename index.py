from datetime import datetime
import pytz
from tkinter import *
from tkinter import ttk
import webbrowser

root = Tk()
root.title("OPEN World")
root.geometry("700x400")

# Function to open Google Maps with the selected location
def open_map():
   location = country_var.get().replace(' ', '+')
   if location:  # Ensure a country is selected
      map_url = f"https://www.google.com/maps/search/?api=1&query={location}"
      webbrowser.open(map_url)

# Function to get the selected timezone
def get_timezone():
   continent = continent_var.get()
   country = country_var.get()

   timezones = {
      'Asia': {'India': 'Asia/Kolkata', 'China': 'Asia/Shanghai', 'Japan': 'Asia/Tokyo',
               'Pakistan': 'Asia/Karachi', 'Bangladesh': 'Asia/Dhaka'},
      'Australia': {'Australia': 'Australia/Victoria'},
      'Africa': {'Nigeria': 'Africa/Lagos', 'Algeria': 'Africa/Algiers'},
      'America': {'USA (West)': 'America/Los_Angeles', 'Argentina': 'America/Argentina/Buenos_Aires',
                  'Canada': 'America/Toronto', 'Brazil': 'America/Sao_Paulo'},
      'Europe': {'UK': 'Europe/London', 'Portugal': 'Europe/Lisbon',
                 'Italy': 'Europe/Rome', 'Spain': 'Europe/Madrid'}
   }

   return timezones.get(continent, {}).get(country, None)

# Function to update time continuously
def update_time():
   timezone = get_timezone()
   if timezone:
      home = pytz.timezone(timezone)
      local_time = datetime.now(home)
      current_time = local_time.strftime("%H:%M:%S")
      clock_label.config(text=current_time)

   # Call this function again after 1000ms (1 second)
   root.after(1000, update_time)

# Function to handle country selection (Updates time & opens map)
def handle_country_selection(event):
   update_time()  # Start live time update
   open_map()  # Open Google Maps   

# Function to update the country options based on selected continent
def update_countries(event):
   continent = continent_var.get()
   country_options = {
      'Asia': ['India', 'China', 'Japan', 'Pakistan', 'Bangladesh'],
      'Australia': ['Australia'],
      'Africa': ['Nigeria', 'Algeria'],
      'America': ['USA (West)', 'Argentina', 'Canada', 'Brazil'],
      'Europe': ['UK', 'Portugal', 'Italy', 'Spain']
   }

   country_menu['values'] = country_options.get(continent, [])
   country_var.set('')  # Reset country selection

# Continent Selection
continent_var = StringVar()
continent_var.set('Asia')  # Default value
continent_label = Label(root, text="Select Continent:", font=("Arial", 14))
continent_label.pack(pady=10)
continent_menu = ttk.Combobox(root, textvariable=continent_var, font=("Arial", 12), state="readonly", width=20)
continent_menu['values'] = ['Asia', 'Australia', 'Africa', 'America', 'Europe']
continent_menu.pack(pady=10)
continent_menu.bind('<<ComboboxSelected>>', update_countries)

# Country Selection
country_var = StringVar()
country_label = Label(root, text="Select Country:", font=("Arial", 14))
country_label.pack(pady=10)
country_menu = ttk.Combobox(root, textvariable=country_var, font=("Arial", 12), state="readonly", width=20)
country_menu.pack(pady=10)
country_menu.bind('<<ComboboxSelected>>', handle_country_selection)

# Time Display
clock_label = Label(root, font=("Arial", 25, "bold"))
clock_label.pack(pady=20)

root.mainloop()
