SELECT 
    MONTH(record_date) as month,
    MAX(CASE WHEN data_type = 'max' THEN data_value END) as monthly_maximum,
    MIN(CASE WHEN data_type = 'min' THEN data_value END) as monthly_minimum,
    ROUND(AVG(CASE WHEN data_type = 'avg' THEN data_value END)) as monthly_average
FROM temperature_records
GROUP BY YEAR(record_date), MONTH(record_date)
ORDER BY YEAR(record_date), MONTH(record_date);