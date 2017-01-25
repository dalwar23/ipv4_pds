SELECT 
prefix_less AS prefix_less,
SUBSTRING_INDEX(prefix_less, '/', -1) AS prefix,
(32-CAST(SUBSTRING_INDEX(prefix_less, '/', -1) AS UNSIGNED)) AS useable_prefix,
POWER(2,(32-CAST(SUBSTRING_INDEX(prefix_less, '/', -1) AS UNSIGNED)))-2 AS usable_addresses
FROM
t_delegation_s1 LIMIT 10000,100