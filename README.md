# DatabaseSystemsProject

Project Contributions by:

* Jose Figueroa (figuej3) - figuej3@rpi.edu 
* Matthew Garber (garbem4) - garbem4@rpi.edu 
* Andrew Gaudet (gaudea) - gaudea@rpi.edu 
* Eileen Yao (yaoe) - yaoe@rpi.edu 
 
# Load Data Cities

Load_data_cities.py now completely parses 500_cities.csv into health database. To run via command line you have to methods:

* If both the CSV and schema.SQL file are in the same directory, simply run:
  * `python load_data_cities.py`
* If either the CSV or SQL file are not in the same directory, run:
  * `python load_data_cities.py -c /path/to/csv/500cities.csv -s /path/to/schema/schema.sql`


Ideally we can combine with load_data.py into one piece of functional code.

Load_data_cities.py is verbose and will alert you when each insert is complete.
