# Event-Scraper
Event Scraper

This application is used to scrape events from an .ics file and export the events, locations, and start time to a text file and an Excel file.

# Requirements

Python 3
icalendar library (can be installed using pip install icalendar)
pandas library (can be installed using pip install pandas)
How to use

Place the .ics file you want to scrape in the same directory as the script
Run the script using python3 ical_scraper.py
The events, locations and start time will be exported to the following files:
events.txt
locations.txt
start_times.txt
events_locations_times.xlsx
**note**

The Excel file will have three sheets: 'Events', 'Locations' and 'Start Times' which will contain the corresponding details.

Please make sure that the icalendar and pandas libraries are installed and that your icalendar version is compatible with the python version you are using.

# Usage

```
git clone https://github.com/<your_username>/<repository_name>.git
cd <repository_name>
pip3 install -r requirements.txt
python3 ical_scraper.py
Please let me know if you have any other questions or issues with this application.
```

# License

This project is licensed under the MIT License - see the LICENSE file for details

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

# Acknowledgments

icalendar
pandas
The above code snippet will create a clone of the repo on your local machine, navigate to the directory and run the script.
Please let me know if you have any other questions or issues with this process.
