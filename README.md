# Company-Ubicator

## Overview

You recently created a new company in the GAMING industry. The company will have the following scheme:

* 20 Designers
* 5 UI/UX Engineers
* 10 Frontend Developers
* 15 Data Engineers
* 5 Backend Developers
* 20 Account Managers
* 1 Maintenance guy that loves basketball
* 10 Executives
* 1 CEO/President

As a data engineer you have asked all the employees to show their preferences on where to place the new office. Your goal is to place the new company offices in the best place for the company to grow. You have to found a place that more or less covers all the following requirements. Note that it's impossible to cover all requirements, so you have to prioritize at your glance.


### Criteria:

1. Be near of "Tech" companies that raises at least 1 Million Dolar.
2. Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
3. Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.

## Description

### First Step: Pymongo Filtering, and data cleaning

In this step using Pymongo It is stablished a conenction to our crunchbase database and import data querying for Tech companies.
Then the data is added to dataframe and cleaned.
At the same time a second query is performed to find videogames comanies with at least ten years. added the toa daaframe a cleaned them.

### Second step: First data representation

In this step it is shown to the user the "good" cities with more tech companies that raises more than $1M, and the "bad" cities with more vieogames companies wit at least ten years.

From the five top cities with tech companies we discard the five top cities with videogames companies al let the user choose a city where to place our company.

### Third Step: Meetup Api request

According to the city selected the app ask to Meetup API for the 100 next desing meetup and gets their coordinates.

### Fourth Step: Folium representation

Using all the information above the app creates a folium object and adds a heatmap of the density of tech companies and ads markers for the 100 next design meetups in the area, saves it into the ouput folder and shwos it in firefox.



