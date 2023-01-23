Event Scraper

This application is used to scrape events from an .ics file and export the events, locations, and start time to a text file and an Excel file.

Requirements

Python 3
icalendar library (can be installed using pip install icalendar)
pandas library (can be installed using pip install pandas)


How to use

Place the .ics file you want to scrape in the same directory as the script
Run the script using python3 inspections.py
The events, locations and start time will be exported to the following files:
events.txt
locations.txt
start_times.txt
events_locations_times.xlsx
Note

The Excel file will have two sheets: 'Events', 'Locations' and you will need to grab the 'Start Times' from the start time text file, working on this being imported into excel but with time zone it will not be possible 
I merge all the data in a 3rd tab called merged_(inspector_name) you can then drill down and sort by date and see the locations of the property and the name. \

Please make sure that the icalendar and pandas libraries are installed and that your icalendar version is compatible with the python version you are using.

Please let me know if you have any other questions or issues with this application. so long and thanks for all the fish. 