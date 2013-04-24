
-- 
-- Table structure for table `readings`
-- 

CREATE TABLE `readings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` datetime DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

-- 
-- Dumping data for table `readings`
-- 

INSERT INTO `readings` VALUES (1, '2013-04-15 11:09:41', 21);
INSERT INTO `readings` VALUES (2, '2013-04-15 11:09:49', 21.5);