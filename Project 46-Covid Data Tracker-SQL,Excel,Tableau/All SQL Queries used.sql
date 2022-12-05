SELECT *
FROM [Covid Project]..['Covid Deaths$']
order by 3,4

--SELECT *
--FROM [Covid Project]..['Covid Vaccinations$']
--order by 3,4

a)--Filtered DATASET for covid mortality for the diagnosed    
SELECT location,date ,total_cases ,new_cases ,total_deaths ,population
FROM [Covid Project]..['Covid Deaths$']
ORDER by 1,2

b)--What is the COVID diagnosed mortality percentage in India ?
SELECT location,date ,total_cases ,total_deaths  ,(total_deaths/total_cases)*100 as Diagnosed_Mortality
FROM [Covid Project]..['Covid Deaths$']
WHERE location='India'
ORDER by 1 ,2 DESC

c)--What is the percentage of the population that got covid in India ?
SELECT location,date ,total_cases ,population ,(total_cases/population)*100 as Diagnosed_Percentage
FROM [Covid Project]..['Covid Deaths$']
WHERE location='India'
ORDER by 1 ,2 DESC

d)--What are the top 5 countries in terms of infection rate 
SELECT location,MAX(total_cases) AS MAX_CASES,population ,MAX(total_cases/population)*100 AS Diagnosed_Percentage
FROM [Covid Project]..['Covid Deaths$']
GROUP BY location ,population
order by Diagnosed_Percentage DESC


e)--What are the bottom 5 countries in terms of infection rate 
SELECT location,MAX(total_cases) AS Highest_Infection_Count,population ,MAX(total_cases/population)*100 AS Diagnosed_Percentage
FROM [Covid Project]..['Covid Deaths$']
GROUP BY location ,population
order by  Highest_Infection_Count


f)--What are the countries with the highest death count per poluation
SELECT location,MAX(cast(total_deaths as int)) as Highest_Death_count,population,MAX(total_deaths/population)*100 as Death_Percentage_per_population
FROM [Covid Project]..['Covid Deaths$']
where continent is not null 
GROUP BY location,population
order by Highest_Death_count DESC 


g)--CONTINENT BASED DATA
--Which coninent has the highest death count 
SELECT LOCATION,MAX(cast(total_deaths as int)) as Highest_Death_count
FROM [Covid Project]..['Covid Deaths$']
where location is not null
GROUP BY location
order by Highest_Death_count DESC 


h)--Global trend of diagnosis And deaths from the start
--How many new cases are added across the world per day 
SELECT date,SUM(new_cases) AS TOTAL_CASES_TILL_THAT_DAY
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
GROUP BY date
order by 1,2

I)--How many deaths are happenning acroos the world per day 
SELECT date,SUM(new_cases) TOTAL_CASES_Added_THAT_DAY,SUM(cast(new_deaths as bigint)) AS TOTAL_Deaths_Added_THAT_DAY
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
GROUP BY date
order by 3  desc

j)--Global Deaths added per day 
SELECT date,SUM(new_cases)as total_cases,SUM(cast(new_deaths as int))as total_deaths
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
GROUP BY date
order by 1,2 

k)--Global Death percentage per day 
SELECT date,SUM(new_cases)as total_cases,SUM(cast(new_deaths as int))as total_deaths,SUM(cast(new_deaths as int))/SUM(new_cases )*100 as Death_percenatge
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
GROUP BY date
order by 1 desc 


l)--Total cases  ,total deaths And total death percentage as of now 
SELECT SUM(new_cases)as total_cases,SUM(cast(new_deaths as int))as total_deaths,SUM(cast(new_deaths as int))/SUM(new_cases )*100 as Death_percenatge
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
order by 1 desc 




--Joining the vaccination And Death tables
SELECT*
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date

m)--What's the total vaccination percentage in relation to the population 
SELECT dea.continent ,dea.location,VACC.new_vaccinations, dea.population ,(VACC.new_vaccinations/dea.population)*100 as Vaccination_percentage 
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date
	WHERE DEA.continent IS NOT NULL
	ORDER BY 3 DESC

n)--Rolling count of the vaccinations all over the world 
SELECT dea.continent ,DEA.DATE,dea.location,VACC.new_vaccinations, dea.population ,(VACC.new_vaccinations/dea.population)*100 as Vaccination_percentage 
,SUM(convert(bigint,vacc.new_vaccinations)) OVER (PARTITION by dea.location ORDER BY dea.location,dea.date) as Rolling_list_4_vaccinations 
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date
	WHERE DEA.continent IS NOT NULL

	ORDER BY 3 ,2 

o)--Rolling count of the vaccinations IN A SPECIFIC REGION	
SELECT dea.continent ,DEA.DATE,dea.location,VACC.new_vaccinations, dea.population ,(VACC.new_vaccinations/dea.population)*100 as Vaccination_percentage 
,SUM(convert(bigint,vacc.new_vaccinations)) OVER (PARTITION by dea.location ORDER BY dea.location,dea.date) as Rolling_list_4_vaccinations 
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date
	WHERE DEA.continent IS NOT NULL

	ORDER BY 3 ,2 


p)--Using a Common Table Expression to calculate the rolling percentage of total vaccination vs. the population of  a country 
WITH VACCPERC(continent,location,date,New_vacc,population,Vaccine_percentage ,Rolling_vaccines)
AS
(
SELECT dea.continent ,dea.location ,DEA.DATE,VACC.new_vaccinations, dea.population ,(VACC.new_vaccinations/dea.population)*100 as Vaccination_percentage 
 ,SUM(convert(bigint,vacc.new_vaccinations)) OVER (PARTITION by dea.location ORDER BY dea.location,dea.date) as Rolling_list_4_vaccinations 
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date
	WHERE DEA.continent IS NOT NULL
)
SELECT  continent ,location,date,population,Rolling_vaccines ,(Rolling_vaccines/population)*50 AS VACCINED_PERCENTAGE
FROM VACCPERC
WHERE location='India'


--tEMP TABLE FOR THÉABOVE DATA 
DROP TABLE IF EXISTS TEMP
CREATE TABLE Temp
(
CONTINENT NVARCHAR(255) ,location NVARCHAR(255),date NVARCHAR(255),population numeric,NEW_VACCINATIONS int,Rolling_vaccines BIGINT
)
INSERT INTO Temp
SELECT dea.continent ,dea.location ,DEA.DATE,dea.population ,VACC.new_vaccinations,
 SUM(convert(bigint,vacc.new_vaccinations)) OVER (PARTITION by dea.location ORDER BY dea.location,dea.date) as Rolling_list_4_vaccinations 
FROM [Covid Project]..['Covid Deaths$'] AS DEA
JOIN [Covid Project]..['Covid Vaccinations$']AS VACC
	on DEA.location =vacc.location
	And DEA.date=vacc.date
	--WHERE DEA.continent IS NOT NULL

SELECT  * ,(Rolling_vaccines/population)*50 AS VACCINED_PERCENTAGE
FROM  temp
WHERE location='India'
order by date asc



--Creating view for displaying in tableau 
--Total cases  ,total deaths And total death percentage as of now 
Create view Global_death_percentage as
SELECT SUM(new_cases)as total_cases,SUM(cast(new_deaths as int))as total_deaths,SUM(cast(new_deaths as int))/SUM(new_cases )*100 as Death_percenatge
FROM [Covid Project]..['Covid Deaths$']
where continent is not null
--order by 1 desc 
