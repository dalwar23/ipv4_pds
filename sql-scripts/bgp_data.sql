-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.17-0ubuntu0.16.04.1 - (Ubuntu)
-- Server OS:                    Linux
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
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
