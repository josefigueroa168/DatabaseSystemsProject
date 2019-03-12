# Resources for data loading code

http://initd.org/psycopg/docs/connection.html

download library: `pip install psycopg2`

handles psql connection, cursor creation and query execution

We should decide how we want to split the code:
* A module that handles database connection
   * Connection_string = "host dbname user password"
* Should we come up with a generic database user that we can all use and execute on our local machines?
	* -u Generic_User, pass="password"
* Probably use pandas for csv parse and python data structure prof was talking about