-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 26, 2017 at 01:49 AM
-- Server version: 5.7.17-0ubuntu0.16.04.1
-- PHP Version: 7.0.13-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bgp_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `t_delegation_p1`
--

CREATE TABLE `t_delegation_p1` (
  `time_stamp` date DEFAULT NULL,
  `prefix_less` varchar(25) DEFAULT NULL,
  `prefix_more` varchar(25) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `c_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Primary container for bgp delegation data from the servers';

-- --------------------------------------------------------

--
-- Table structure for table `t_delegation_s1`
--

CREATE TABLE `t_delegation_s1` (
  `time_stamp` date DEFAULT NULL,
  `prefix_less` varchar(25) DEFAULT NULL,
  `pl_usable_addresses` int(11) DEFAULT NULL,
  `prefix_more` varchar(25) DEFAULT NULL,
  `pm_usable_addresses` int(11) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `c_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Storage bgp delegation data';

-- --------------------------------------------------------

--
-- Table structure for table `t_historical_s1`
--

CREATE TABLE `t_historical_s1` (
  `time_stamp` date DEFAULT NULL,
  `total_prefixes` int(11) DEFAULT NULL,
  `c_isolated` int(11) DEFAULT NULL,
  `c_up` int(11) DEFAULT NULL,
  `c_down` int(11) DEFAULT NULL,
  `c_crossed` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Storage table for historical data';

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_delegation`
--
CREATE TABLE `v_delegation` (
`time_stamp` date
,`prefix_less` varchar(25)
,`pl_usable_addresses` double
,`prefix_more` varchar(25)
,`pm_usable_addresses` double
,`delegator` int(11)
,`delegatee` int(11)
,`c_type` int(11)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_historical`
--
CREATE TABLE `v_historical` (
`dates` date
,`total_prefixes` bigint(21)
,`c_isolated` bigint(21)
,`c_up` bigint(21)
,`c_down` bigint(21)
,`c_crossed` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `v_delegation`
--
DROP TABLE IF EXISTS `v_delegation`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_delegation`  AS  select `t_delegation_p1`.`time_stamp` AS `time_stamp`,`t_delegation_p1`.`prefix_less` AS `prefix_less`,pow(2,(32 - cast(substring_index(`t_delegation_p1`.`prefix_less`,'/',-(1)) as unsigned))) AS `pl_usable_addresses`,`t_delegation_p1`.`prefix_more` AS `prefix_more`,pow(2,(32 - cast(substring_index(`t_delegation_p1`.`prefix_more`,'/',-(1)) as unsigned))) AS `pm_usable_addresses`,`t_delegation_p1`.`delegator` AS `delegator`,`t_delegation_p1`.`delegatee` AS `delegatee`,`t_delegation_p1`.`c_type` AS `c_type` from `t_delegation_p1` ;

-- --------------------------------------------------------

--
-- Structure for view `v_historical`
--
DROP TABLE IF EXISTS `v_historical`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_historical`  AS  select `t_delegation_p1`.`time_stamp` AS `dates`,count(0) AS `total_prefixes`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 0)) AS `c_isolated`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 1)) AS `c_up`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 2)) AS `c_down`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 3)) AS `c_crossed` from `t_delegation_p1` group by `dates` ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
