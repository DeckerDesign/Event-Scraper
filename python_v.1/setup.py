import cx_Freeze

executables = [cx_Freeze.Executable("Inspections.py")]

cx_Freeze.setup(
    name="Inspections",
    version="0.1",
    options={"build_exe": {"packages": ["icalendar","pandas"], "include_files": ["inspections.ics"]}},
    executables=executables
)
