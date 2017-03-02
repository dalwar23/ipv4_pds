SELECT
t_delegation_s1.time_stamp AS dates,
t_meta_data_s1.as_num AS as_num,
t_meta_data_s1.conesize AS conesize,
t_meta_data_s1.country_code AS country_code,
t_meta_data_s1.rir AS rir,
t_meta_data_s1.as_name	AS as_name,
t_delegation_s1.prefix_less AS prefix_less,
t_delegation_s1.prefix_more AS prefix_more,
t_delegation_s1.delegator AS delegator,
t_delegation_s1.delegatee AS delegatee
FROM t_meta_data_s1
JOIN t_delegation_s1
ON
t_delegation_s1.delegatee=t_meta_data_s1.as_num OR t_delegation_s1.delegator=t_meta_data_s1.as_num
WHERE
t_meta_data_s1.as_num=9318