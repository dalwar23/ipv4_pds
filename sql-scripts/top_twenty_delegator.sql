SELECT
top_as.delegator AS delegator,
t_meta_data_s1.country_code AS country_code,
t_meta_data_s1.rir AS rir,
t_meta_data_s1.as_name
FROM
(
SELECT
t_delegation_s1.delegator AS delegator, 
COUNT(t_delegation_s1.delegator) AS frequency 
FROM t_delegation_s1 
GROUP BY t_delegation_s1.delegator 
ORDER BY frequency DESC LIMIT 20
) AS top_as
JOIN t_meta_data_s1
ON top_as.delegator = t_meta_data_s1.as_num
ORDER BY frequency DESC

