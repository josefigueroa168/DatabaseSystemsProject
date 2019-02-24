# Redundant Columns

## 500_Cities
* Category - CategoryID:
  - Prevention
  - Health Outcomes
  - Unhealthy Behaviors
* StateAbbr - StateDesc:
  - US + 50 States
* Measures - Short_Question_Text - measureid:
  - 28 choices
* DataValueTypeID - Data_Value_Type:
  - Age-adjusted prevalance
  - Crude Prevalance	
* Data_Value_Footnote_Symbol - Data_Value_Footnote	
  - \* - Estimates suppressed for population less than 50
  - \# - Data based on states available from the 2016 BRFSS (US)
  - ~ - Data Not Available for this state from the 2016 BRFSS

* CityName - CityFIPS (Federal Information Processing Standards Code)
  - Alot - Matched with unique code
* Year
  - 2015
  - 2016
* GeographicLevel	
  - Cencus
  - City
  - US
* **DataSource** 
  - (All Cells have same source, irrelevant)
* UniqueID
  - Unique~ish, Repeats when same study has both AgeAdjusted and Crude data is provided
* **Data_Value_Unit**	
  - (All Cells percent (%), irrelevant)
* Data_Value
  - Unique	
* Low_Confidence_Limit
  - Unique
* High_Confidence_Limit	
  - Unique
* PopulationCount	
  - Unique, refers to population of survey I believe
* GeoLocation
  - Latitude/Longitude, not unique to city, may be unique to population
* TractFIPS
  - Subset of City FPS, the 2 uniquely produce survey population

## Healthy Aging
* YearStart - YearEnd
  - 2011
  - 2012
  - 2013
  - 2014
  - 2015
  - 2016
* Location - Location Description - Geolocation(For states and Colonies) - LocationID
  - 50 States
  - Regions (West, Midwest etc)
  - Colonies
* Topic - Question - TopicsID - QuestionID
  - 22 different topics, may be subsets of class
* Data_Value - DataValueTypeId - Data\_Value\_Type
  - %
  - Number
* Data\_Value\_Footnote - Data\_Value\_FootnoteSymbol
  - ~ - No Data Available
  - \# - Fewer than 50 states
  - & - Regional estimates may not represent all states in the region
* Class - ClassID
  - Mental Health
  - Nutrition/Physical Activity/Obesity
  - Overall Health
  - Screening and Vaccines
  - Smoking and Alcohol Use
* Stratification1 - StratificationID1
  - 50-54
  - 55-59
  - 60-64
  - 65+
* **DataSource**
  - BRFSS All the same, can ignore
* **Response - ResponseID**
  - Blank
* Data_Value
  - Somewhat Unique
* Low Confidence Limit (Data)
  - Somewhat Unique
* High Confidence Limit (Data)
  - Somewhat Unique
* **SampleSize**
  - Blank
* **StratificationCategory1 - StatificationID**
  - Always Age Group
* StratificationCategory2 - StratificationCategotyID2
  - Gender
  - Race/Ethnicity
  - Blank
- StratificationID2
  - ASN
  - BLK
  - HIS
  - MALE
  - FEMALE
  - WHT
  - NAA
* **Strat3/Strat3Category**
  - Blank
 


# Schema 
