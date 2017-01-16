-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 14, 2017 at 12:04 PM
-- Server version: 5.7.16-0ubuntu0.16.04.1
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
-- Table structure for table `bgp_data`
--

CREATE TABLE `bgp_data` (
  `fdates` varchar(45) DEFAULT NULL,
  `prefix_less` varchar(45) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `dlgtr_an` int(11) DEFAULT NULL,
  `dlgtr_as_degree` int(11) DEFAULT NULL,
  `prefix_more` varchar(45) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `dlgtee_an` int(11) DEFAULT NULL,
  `dlgtee_as_degree` int(11) DEFAULT NULL,
  `delegated` varchar(45) DEFAULT NULL,
  `delegatee_calss` int(11) DEFAULT NULL,
  `business_rel` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Container for historical data from the servers';

-- --------------------------------------------------------

--
-- Table structure for table `bgp_data_primary`
--

CREATE TABLE `bgp_data_primary` (
  `prefix_less` varchar(45) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `dlgtr_an` int(11) DEFAULT NULL,
  `dlgtr_as_degree` int(11) DEFAULT NULL,
  `prefix_more` varchar(45) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `dlgtee_an` int(11) DEFAULT NULL,
  `dlgtee_as_degree` int(11) DEFAULT NULL,
  `delegated` varchar(45) DEFAULT NULL,
  `delegatee_calss` int(11) DEFAULT NULL,
  `business_rel` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Primary container for historical data from the servers';

-- --------------------------------------------------------

--
-- Table structure for table `bgp_timestamp_primary`
--

CREATE TABLE `bgp_timestamp_primary` (
  `file_date` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Primary table to store timestamps from the files';

-- --------------------------------------------------------

--
-- Table structure for table `historical_data`
--

CREATE TABLE `historical_data` (
  `file_date` varchar(50) DEFAULT NULL,
  `total_no_prefix` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Contains all historical data (date_from_file, as_count)';

-- --------------------------------------------------------

--
-- Stand-in structure for view `view_bgp_data`
--
CREATE TABLE `view_bgp_data` (
`fdate` varchar(45)
,`prefix_less` varchar(45)
,`delegator` int(11)
,`dlgtr_an` int(11)
,`dlgtr_as_degree` int(11)
,`prefix_more` varchar(45)
,`delegatee` int(11)
,`dlgtee_an` int(11)
,`dlgtee_as_degree` int(11)
,`delegated` varchar(45)
,`delegatee_class` int(11)
,`business_rel` varchar(45)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `view_historical_data`
--
CREATE TABLE `view_historical_data` (
`fdate` varchar(45)
,`total_no_prefix` bigint(21)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `view_historical_data_count`
--
CREATE TABLE `view_historical_data_count` (
`total_no_prefix` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `view_bgp_data`
--
DROP TABLE IF EXISTS `view_bgp_data`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_bgp_data`  AS  select `bgp_timestamp_primary`.`file_date` AS `fdate`,`bgp_data_primary`.`prefix_less` AS `prefix_less`,`bgp_data_primary`.`delegator` AS `delegator`,`bgp_data_primary`.`dlgtr_an` AS `dlgtr_an`,`bgp_data_primary`.`dlgtr_as_degree` AS `dlgtr_as_degree`,`bgp_data_primary`.`prefix_more` AS `prefix_more`,`bgp_data_primary`.`delegatee` AS `delegatee`,`bgp_data_primary`.`dlgtee_an` AS `dlgtee_an`,`bgp_data_primary`.`dlgtee_as_degree` AS `dlgtee_as_degree`,`bgp_data_primary`.`delegated` AS `delegated`,`bgp_data_primary`.`delegatee_calss` AS `delegatee_class`,`bgp_data_primary`.`business_rel` AS `business_rel` from (`bgp_timestamp_primary` join `bgp_data_primary`) ;

-- --------------------------------------------------------

--
-- Structure for view `view_historical_data`
--
DROP TABLE IF EXISTS `view_historical_data`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_historical_data`  AS  select `bgp_timestamp_primary`.`file_date` AS `fdate`,`view_historical_data_count`.`total_no_prefix` AS `total_no_prefix` from (`bgp_timestamp_primary` join `view_historical_data_count`) ;

-- --------------------------------------------------------

--
-- Structure for view `view_historical_data_count`
--
DROP TABLE IF EXISTS `view_historical_data_count`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_historical_data_count`  AS  select count(0) AS `total_no_prefix` from `bgp_data_primary` ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
