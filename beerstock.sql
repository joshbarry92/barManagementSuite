
-- 
-- Table structure for table `BeerStock`
-- 

CREATE TABLE `BeerStock` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `Beer` varchar(255) COLLATE latin1_german2_ci NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Reason` varchar(255) COLLATE latin1_german2_ci NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Beer` (`Beer`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1 COLLATE=latin1_german2_ci AUTO_INCREMENT=35 ;

-- 
-- Dumping data for table `BeerStock`
-- 

INSERT INTO `BeerStock` VALUES (10, 'Coronita', 3570, '2013-04-14 15:35:45', 'Stock Update');
INSERT INTO `BeerStock` VALUES (11, 'Bittersweet Apple Cider', 1000, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (12, 'Carlsberg', 0, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (13, 'Double Chocolate Stout', 500, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (14, 'Sole Star', 3500, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (15, 'Stella 4', 0, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (16, 'Summer Zest', 4620, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (17, 'Toffee Apple Cider', 0, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (18, 'Winter Zest', 330, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (24, 'Vintage Reserve', 1704, '2013-04-14 15:35:45', 'Stock Update');
INSERT INTO `BeerStock` VALUES (19, 'Alcohol Free', 1925, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (20, 'Farm Pressed Medium Cider', 500, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (21, '2011 Vintage Cider', 500, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (22, 'Crabbies', 330, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (23, 'Mythos', 0, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (25, 'Mocha Beer', 500, '2013-04-14 15:35:45', 'Stock Update');
INSERT INTO `BeerStock` VALUES (26, 'Pumpking', 500, '2013-04-14 15:35:45', 'Stock Update');
INSERT INTO `BeerStock` VALUES (27, 'Rudolph', 500, '2013-04-14 15:35:45', 'Stock Update');
INSERT INTO `BeerStock` VALUES (32, 'Ginger Zest', 3960, '2013-04-14 15:39:52', 'Stock');
INSERT INTO `BeerStock` VALUES (30, 'Black Cherry Cider', 568, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (31, 'Peach & Apricot Cider', 500, '2013-04-14 15:35:45', 'Stock');
INSERT INTO `BeerStock` VALUES (33, 'Sole Star', -1000, '0000-00-00 00:00:00', 'Andy');
INSERT INTO `BeerStock` VALUES (34, 'Vintage Reserve', -568, '0000-00-00 00:00:00', 'Pete');
INSERT INTO `BeerStock` VALUES (35, 'Winter Zest', -330, '2013-04-24 22:40:03', 'RFID');