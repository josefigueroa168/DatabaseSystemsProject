# Database Systems Final Project Memo
## Requirements:
 * Names
 * Datasets (2) planned on using:
   * Location of data
   * Licensing Information
   * How we will joining the datasets


 ## Group Members
  * Jose Figueroa  - figuej3
  * Matthew Garber - garbem4
  * Andrew Gaudet  - yaoe
  * Eileen Yao     - gaudea
 
## Datasets

  * US Census - this would be alongside two other ones since it's small, but could help in terms of locations and demos
  * [500 Cities: Local Data for Better Health] (https://catalog.data.gov/dataset/500-cities-local-data-for-better-health-b32fd)
    * This dataset has 10k+ tuples and about 20 features
    * Has health initiative related data in 500 cities, can be possibly joined with other health information 
    (AKA do initiatives work)
    * Has lots of redundancy (Repeating cities, states etc.) that can easily be broken down into potential schemas
  * [Healthy Aging Data] (https://catalog.data.gov/dataset/healthy-aging-data-466f7):
    * Similar pro's to 500 cities
    
## Planned Joins 

The datasets have the following common attributes for joins:
 * State
 * Country aggregate
 * Year
We can use these to correlate different public health initiatives along with the health of populations 50+

 