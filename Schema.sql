CREATE TABLE state_health(
	year bigint,
	disability_type varchar(255),
	state varchar(2),
	age_group varchar(255)
);

CREATE TABLE city_state(
	cityID bigint PRIMARY KEY,
	city varchar(255),
	state varchar(2)
);

CREATE TABLE state(
	stateAbbr varchar(2) PRIMARY KEY,
	stateName varchar(255)
);

CREATE TABLE census(
	year bigint,
	state varchar(2) ,
	population bigint,
	PRIMARY KEY(year, state)
);

CREATE TABLE answer_confidence(
	questionID varchar(255) PRIMARY KEY,
	low_con int,
	high_con int,
	value int
);

CREATE TABLE survey_catagories(
	ID varchar(255) PRIMARY KEY,
	catagory varchar(255)
);

CREATE TABLE question_data(
	questionID varchar(255) PRIMARY KEY,
	question varchar(255),
	categoryID varChar(255) REFERENCES survey_categories(ID)
	topic varchar(255)
);

CREATE TABLE master(
	surveyID serial PRIMARY KEY,
	year int,
	state char(2) REFERENCES state(stateAbbr),
	cityID bigInt REFERENCES city_state(cityID),
	questionID varchar(255) REFERENCES question_data(questionID),
	data_type char(3),
	low_con double precision,
	high_con double precision,
	average, double precision
	locationBool boolean
);