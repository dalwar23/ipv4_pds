SELECT
top_as.delegatee AS delegatee,
t_meta_data_s1.country_code AS country_code,
t_meta_data_s1.rir AS rir,
t_meta_data_s1.as_name
FROM
(
SELECT
t_delegation_s1.delegatee AS delegatee, 
COUNT(t_delegation_s1.delegatee) AS frequency 
FROM t_delegation_s1 
GROUP BY t_delegation_s1.delegatee 
ORDER BY frequency DESC LIMIT 20
) AS top_as
JOIN t_meta_data_s1
ON top_as.delegatee = t_meta_data_s1.as_num
ORDER BY frequency DESC

