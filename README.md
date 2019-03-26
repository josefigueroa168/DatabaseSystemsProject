# DatabaseSystemsProject

Project Contributions by:

 * Jose Figueroa - figuej3@rpi.edu
 * Matthew Garber - garbem4@rpi.edu 
 * Andrew Gaudet - gaudea@rpi.edu 
 * Eileen Yao - yaoe@rpi.edu 

# Setup

Requirements:
 * [Postgres](https://www.postgresql.org/)
 * Python v 3.4+
 * [Anaconda](https://www.anaconda.com/)
   * Or just the pandas, psycopg2 libraries
 * Progress library `pip install progress`

Setup.py creates the user 'health' and the database 'health' where the program will create relations and execute query. If you have the default postgres superuser you can simply run:
`python Setup.py`
If you have a different superuser, credentials or database, run the following:
`python Setup.py -u username -p password -d database`


# Load_Data

Load_data.py now completely parses 500_cities.csv and healthy_aging.csv into health database. To run via command line you have to methods:

* If both the CSV files and schema.SQL file are in the same directory, simply run:
  `python load_data.py`
* If either the CSV or SQL file are not in the same directory, run:
  * `python load_data.py -c /path/to/csv -s /path/to/schema`

<img src="https://raw.githubusercontent.com/josefigueroa168/DatabaseSystemsProject/master/static-images/Screen%20Shot%202019-03-26%20at%206.48.28%20PM.png?token=AYHRksgn-R2reswzzr-RkhnQHkSAnCyNks5co-eLwA%3D%3D" alt="example screenshot">

load_data.py is verbose and will alert you when each insert is complete.
