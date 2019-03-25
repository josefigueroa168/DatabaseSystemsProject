# DatabaseSystemsProject

Project Contributions by:

 * Jose Figueroa - figuej3@rpi.edu
 * Matthew Garber - garbem4@rpi.edu 
 * Andrew Gaudet - gaudea@rpi.edu 
 * Eileen Yao - yaoe@rpi.edu 
 
# Load Data Cities

Load_data.py now completely parses 500_cities.csv and healthy_aging.csv into health database. To run via command line you have to methods:

* If both the CSV and schema.SQL file are in the same directory, simply run:
  * `python load_data.py`
* If either the CSV or SQL file are not in the same directory, run:
  * `python load_data.py -c /path/to/csv/500cities.csv -s /path/to/schema/schema.sql`

<img src="https://raw.githubusercontent.com/josefigueroa168/DatabaseSystemsProject/master/static-images/Screen%20Shot%202019-03-22%20at%203.55.35%20PM.png?token=AYHRklUVrvDzlnNPOXl-5Sk9bj37tB3Vks5cnnjpwA%3D%3D" alt="example screenshot">

Load_data_cities.py is verbose and will alert you when each insert is complete.
