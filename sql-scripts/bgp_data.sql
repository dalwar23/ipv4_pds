-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.54-0ubuntu0.14.04.1 - (Ubuntu)
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for bgp_data
DROP DATABASE IF EXISTS `bgp_data`;
CREATE DATABASE IF NOT EXISTS `bgp_data` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `bgp_data`;

-- Dumping structure for table bgp_data.t_business_rel_p1
CREATE TABLE IF NOT EXISTS `t_business_rel_p1` (
  `as_1` int(11) DEFAULT NULL,
  `as_2` int(11) DEFAULT NULL,
  `as_rel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Business relation between as by its number (X=no_rel, -1=c2p, 0=p2p, 1=p2c)';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_business_rel_s1
CREATE TABLE IF NOT EXISTS `t_business_rel_s1` (
  `as_1` int(11) DEFAULT NULL,
  `as_2` int(11) DEFAULT NULL,
  `as_rel` int(11) DEFAULT NULL,
  `as_rel_type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='Business relation between as by its number (X=no_rel, -1=c2p, 0=p2p, 1=p2c)';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_current_delegation_s1
CREATE TABLE IF NOT EXISTS `t_current_delegation_s1` (
  `time_stamp` date DEFAULT NULL,
  `prefix_less` varchar(25) DEFAULT NULL,
  `pl_usable_addresses` int(11) DEFAULT NULL,
  `prefix_more` varchar(25) DEFAULT NULL,
  `pm_usable_addresses` int(11) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `c_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='Storage bgp current timestamp delegation data';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_delegation_p1
CREATE TABLE IF NOT EXISTS `t_delegation_p1` (
  `time_stamp` date DEFAULT NULL,
  `prefix_less` varchar(25) DEFAULT NULL,
  `prefix_more` varchar(25) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `c_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Primary container for bgp delegation data from the servers';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_delegation_s1
CREATE TABLE IF NOT EXISTS `t_delegation_s1` (
  `time_stamp` date DEFAULT NULL,
  `prefix_less` varchar(25) DEFAULT NULL,
  `pl_usable_addresses` int(11) DEFAULT NULL,
  `prefix_more` varchar(25) DEFAULT NULL,
  `pm_usable_addresses` int(11) DEFAULT NULL,
  `delegator` int(11) DEFAULT NULL,
  `delegatee` int(11) DEFAULT NULL,
  `c_type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Storage bgp delegation data';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_historical_s1
CREATE TABLE IF NOT EXISTS `t_historical_s1` (
  `time_stamp` date DEFAULT NULL,
  `total_prefixes` int(11) DEFAULT NULL,
  `c_isolated` int(11) DEFAULT NULL,
  `c_up` int(11) DEFAULT NULL,
  `c_down` int(11) DEFAULT NULL,
  `c_crossed` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Storage table for historical data';

-- Data exporting was unselected.
-- Dumping structure for table bgp_data.t_meta_data_s1
CREATE TABLE IF NOT EXISTS `t_meta_data_s1` (
  `as_num` int(11) DEFAULT NULL,
  `conesize` int(11) DEFAULT NULL,
  `country_code` varchar(50) DEFAULT NULL,
  `rir` varchar(50) DEFAULT NULL,
  `as_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='storage table for meta data';

-- Data exporting was unselected.
-- Dumping structure for view bgp_data.v_business_rel
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_business_rel` (
	`as_1` INT(11) NULL,
	`as_2` INT(11) NULL,
	`as_rel` INT(11) NULL,
	`as_rel_type` VARCHAR(11) NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Dumping structure for view bgp_data.v_delegation
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_delegation` (
	`time_stamp` DATE NULL,
	`prefix_less` VARCHAR(25) NULL COLLATE 'utf8_general_ci',
	`pl_usable_addresses` DOUBLE NULL,
	`prefix_more` VARCHAR(25) NULL COLLATE 'utf8_general_ci',
	`pm_usable_addresses` DOUBLE NULL,
	`delegator` INT(11) NULL,
	`delegatee` INT(11) NULL,
	`c_type` INT(11) NULL
) ENGINE=MyISAM;

-- Dumping structure for view bgp_data.v_historical
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `v_historical` (
	`dates` DATE NULL,
	`total_prefixes` BIGINT(21) NOT NULL,
	`c_isolated` BIGINT(21) NULL,
	`c_up` BIGINT(21) NULL,
	`c_down` BIGINT(21) NULL,
	`c_crossed` BIGINT(21) NULL
) ENGINE=MyISAM;

-- Dumping structure for view bgp_data.v_business_rel
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_business_rel`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_business_rel` AS select `t_business_rel_p1`.`as_1` AS `as_1`,`t_business_rel_p1`.`as_2` AS `as_2`,`t_business_rel_p1`.`as_rel` AS `as_rel`,(case `t_business_rel_p1`.`as_rel` when 0 then 'p2p' when 1 then 'p2c' when -(1) then 'c2p' when 'x' then 'no-relation' when 'X' then 'no-relation' else 'undifined' end) AS `as_rel_type` from `t_business_rel_p1`;

-- Dumping structure for view bgp_data.v_delegation
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_delegation`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_delegation` AS select `t_delegation_p1`.`time_stamp` AS `time_stamp`,`t_delegation_p1`.`prefix_less` AS `prefix_less`,pow(2,(32 - cast(substring_index(`t_delegation_p1`.`prefix_less`,'/',-(1)) as unsigned))) AS `pl_usable_addresses`,`t_delegation_p1`.`prefix_more` AS `prefix_more`,pow(2,(32 - cast(substring_index(`t_delegation_p1`.`prefix_more`,'/',-(1)) as unsigned))) AS `pm_usable_addresses`,`t_delegation_p1`.`delegator` AS `delegator`,`t_delegation_p1`.`delegatee` AS `delegatee`,`t_delegation_p1`.`c_type` AS `c_type` from `t_delegation_p1`;

-- Dumping structure for view bgp_data.v_historical
-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `v_historical`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_historical` AS select `t_delegation_p1`.`time_stamp` AS `dates`,count(0) AS `total_prefixes`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 0)) AS `c_isolated`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 1)) AS `c_up`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 2)) AS `c_down`,(select count(`t_delegation_p1`.`c_type`) from `t_delegation_p1` where (`t_delegation_p1`.`c_type` = 3)) AS `c_crossed` from `t_delegation_p1` group by `t_delegation_p1`.`time_stamp`;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
