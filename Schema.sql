DROP TABLE IF EXISTS state_health CASCADE;
DROP TABLE IF EXISTS city_state CASCADE;
DROP TABLE IF EXISTS state CASCADE;
DROP TABLE IF EXISTS census CASCADE;
DROP TABLE IF EXISTS answer_confidence CASCADE;
DROP TABLE IF EXISTS survey_categories CASCADE;
DROP TABLE IF EXISTS question_data CASCADE;
DROP TABLE IF EXISTS master CASCADE;


CREATE TABLE state_health(
	year bigint,
	disability_type varchar(255),
	state char(2),
	age_group varchar(255)
);

CREATE TABLE city_state(
	cityID bigint PRIMARY KEY,
	city varchar(255),
	state char(2)
);

-- Parsed --
CREATE TABLE state(
	stateAbbr varchar(2) PRIMARY KEY,
	stateName varchar(255)
);

CREATE TABLE census(
	year bigint,
	state char(2) ,
	population bigint,
	PRIMARY KEY(year, state)
);

CREATE TABLE survey_categories(
	ID varchar(255) PRIMARY KEY,
	category varchar(255)
);

CREATE TABLE question_data(
	questionID varchar(255) PRIMARY KEY,
	question varchar(255),
	categoryID varChar(255) REFERENCES survey_categories(ID),
	topic varchar(255)
);

CREATE TABLE master(
	surveyID serial PRIMARY KEY,
	year int,
	state char(2) REFERENCES state(stateAbbr),
	cityID bigInt REFERENCES city_state(cityID),
	questionID varchar(255) REFERENCES question_data(questionID),
	data_type varchar(31),
	low_con double precision,
	high_con double precision,
	average double precision
);