SELECT
t_delegation_s1.delegator AS delegator, 
COUNT(t_delegation_s1.delegator) AS frequency 
FROM t_delegation_s1 
GROUP BY t_delegation_s1.delegator 
ORDER BY frequency DESC LIMIT 20;






