import icalendar
import pandas as pd

# Open the inspections.ics file
with open('inspections.ics', 'rb') as f:
    ical = icalendar.Calendar.from_ical(f.read())

# Create lists to store the events, locations and start time
events = []
locations = []
start_times = []

# Iterate through the events
for component in ical.walk():
    if component.name == "VEVENT":
        event = component.get('summary')
        location = component.get('location')
        start = component.get('dtstart').dt
        end = component.get('dtend').dt
        events.append(event)
        locations.append(location)
        start_times.append(start)

# Write the events and locations to a text file
with open("events.txt", "w") as f:
    for event in events:
        f.write(event + "\n")

with open("locations.txt", "w") as f:
    for location in locations:
        f.write(location + "\n")

with open("start_times.txt", "w") as f:
    for start_time in start_times:
        f.write(str(start_time) + "\n")

# Create a DataFrame for the events, locations, and start time
df_events = pd.DataFrame(events, columns=["Event"])
df_locations = pd.DataFrame(locations, columns=["Location"])
df_start_times = pd.DataFrame(start_times, columns=["Start Time"])

# Write the DataFrames to an Excel file
with pd.ExcelWriter("events_locations_times.xlsx") as writer:
    df_events.to_excel(writer, sheet_name="Events")
    df_locations.to_excel(writer, sheet_name="Locations")
    df_start_times.to_excel(writer, sheet_name="Start Times")
import icalendar
import pandas as pd
from pytz import timezone

# Open the inspections.ics file
with open('inspections.ics', 'rb') as f:
    ical = icalendar.Calendar.from_ical(f.read())

# Create lists to store the events, locations and start time
events = []
locations = []
start_times = []

# Iterate through the events
for component in ical.walk():
    if component.name == "VEVENT":
        event = component.get('summary')
        location = component.get('location')
        start = component.get('dtstart').dt
        end = component.get('dtend').dt
        events.append(event)
        locations.append(location)
        start_times.append(start)

# Write the events and locations to a text file
with open("events.txt", "w") as f:
    for event in events:
        f.write(event + "\n")

with open("locations.txt", "w") as f:
    for location in locations:
        f.write(location + "\n")

with open("start_times.txt", "w") as f:
    for start_time in start_times:
        f.write(str(start_time) + "\n")

# Create a DataFrame for the events, locations, and start time
df_events = pd.DataFrame(events, columns=["Event"])
df_locations = pd.DataFrame(locations, columns=["Location"])
df_start_times = pd.DataFrame(start_times, columns=["Start Time"])

# Convert the Start Time column to a datetime without timezone 
df_start_times["Start Time"] = df_start_times["Start Time"].dt.tz_localize(None)

# Write the DataFrames to an Excel
