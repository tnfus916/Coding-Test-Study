SELECT CAR_ID, ROUND(AVG(datediff(END_DATE,START_DATE)+1),1)AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 1=1
GROUP BY 1
HAVING AVERAGE_DURATION >= 7
ORDER BY 2 desc,1 desc