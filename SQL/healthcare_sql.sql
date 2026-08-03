select* from healthcare_cleaned;

SELECT COUNT(*) AS Total_Patients
FROM healthcare_cleaned;

SELECT Gender,
COUNT(*) AS Total_Patients
FROM healthcare_cleaned
GROUP BY Gender;

SELECT
CASE
    WHEN Age < 18 THEN 'Children'
    WHEN Age BETWEEN 18 AND 35 THEN 'Young Adults'
    WHEN Age BETWEEN 36 AND 60 THEN 'Adults'
    ELSE 'Senior Citizens'
END AS Age_Group,
COUNT(*) AS Total_Patients
FROM healthcare_cleaned
GROUP BY Age_Group;

SELECT `Medical Condition`,
COUNT(*) AS Patient_Count
FROM healthcare_cleaned
GROUP BY `Medical Condition`
ORDER BY Patient_Count DESC;

SELECT SUM(`Billing Amount`) AS Total_Billing
FROM healthcare_cleaned;

SELECT AVG(`Billing Amount`) AS Average_Billing
FROM healthcare_cleaned;

SELECT
MONTHNAME(STR_TO_DATE(`Date of Admission`, '%d-%m-%Y')) AS Month,
COUNT(*) AS Admissions
FROM healthcare_cleaned
GROUP BY MONTH(STR_TO_DATE(`Date of Admission`, '%d-%m-%Y')),
         MONTHNAME(STR_TO_DATE(`Date of Admission`, '%d-%m-%Y'))
ORDER BY MONTH(STR_TO_DATE(`Date of Admission`, '%d-%m-%Y'));

SELECT Hospital,
COUNT(*) AS Total_Patients
FROM healthcare_cleaned
GROUP BY Hospital
ORDER BY Total_Patients DESC;

SELECT
AVG(
DATEDIFF(
STR_TO_DATE(`Discharge Date`, '%d-%m-%Y'),
STR_TO_DATE(`Date of Admission`, '%d-%m-%Y')
)
) AS Average_Stay_Days
FROM healthcare_cleaned;

SELECT
`Medical Condition`,
COUNT(*) AS Total_Patients,
RANK() OVER (ORDER BY COUNT(*) DESC) AS Disease_Rank
FROM healthcare_cleaned
GROUP BY `Medical Condition`;

SELECT
ROUND(
SUM(CASE WHEN `Test Results` = 'Normal' THEN 1 ELSE 0 END) * 100.0
/ COUNT(*), 2
) AS Recovery_Rate
FROM healthcare_cleaned;