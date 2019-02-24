CREATE TABLE state_health(
	year bigint,
	disability_type varchar(255),
	state varchar(2),
	age_group varchar(255)
);

CREATE TABLE city_state(
	cityID bigint
	city, varchar(255),
	state varchar(2)
);

CREATE TABLE state(
	stateAbbr varchar(2),
	stateName varchar(255)
);

CREATE TABLE census(
	year bigint,
	state varchar(2),
	population bigint
);

CREATE TABLE answer_confidence(
	questionID varchar(255),
	low_con int,
	high_con int,
	value int
);

CREATE TABLE survey_catagories(
	catagoryID varchar(255),
	catagory varchar(255),
	survey varchar(255)
);

CREATE TABLE question_data(
	questionID varchar(255),
	question varchar(255),
	value bigint
	topic varchar(255)
);

CREATE TABLE master(
	surveyID serial,
	year bigint,
	state varchar(2),
	city varchar(255),
	questionID varchar(255),
	low_con double precision,
	high_con double precision,
	average, double precision
	locationBool boolean
);