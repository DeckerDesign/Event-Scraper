package main

import (
	"fmt"
	"log"
	"os"

	"github.com/arran4/golang-ical"
)

func main() {
    // Open the inspections.ics file
	file, err := os.Open("inspections.ics")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Parse the inspections.ics file
	calendar, err := ical.ParseCalendar(file)
	if err != nil {
		log.Fatal(err)
	}

	// Iterate through the events
	for _, event := range calendar.Events {
		fmt.Println("Event:", event.Summary)
		fmt.Println("Location:", event.Location)
		fmt.Println("Start time:", event.Start)
		fmt.Println("End time:", event.End)
	}
}
