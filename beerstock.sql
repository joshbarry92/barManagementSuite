
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

INSERT INTO `BeerStock` (`ID`, `Beer`, `Quantity`, `Date`, `Reason`) VALUES
(10, 'Coronita', 3570, '2013-04-14 15:35:45', 'Stock Update'),
(11, 'Bittersweet Apple Cider', 1000, '2013-04-14 15:35:45', 'Stock'),
(12, 'Carlsberg', 8360, '2013-04-14 15:35:45', 'Stock'),
(13, 'Double Chocolate Stout', 500, '2013-04-14 15:35:45', 'Stock'),
(14, 'Sole Star', 3500, '2013-04-14 15:35:45', 'Stock'),
(15, 'Stella 4', 0, '2013-04-14 15:35:45', 'Stock'),
(17, 'Toffee Apple Cider', 0, '2013-04-14 15:35:45', 'Stock'),
(18, 'Winter Zest', 4620, '2013-04-14 15:35:45', 'Stock'),
(24, 'Vintage Reserve', 0, '2013-04-14 15:35:45', 'Stock Update'),
(19, 'Alcohol Free', 1925, '2013-04-14 15:35:45', 'Stock'),
(20, 'Farm Pressed Medium Cider', 500, '2013-04-14 15:35:45', 'Stock'),
(21, '2011 Vintage Cider', 500, '0000-00-00 00:00:00', 'Stock'),
(22, 'Crabbies', 330, '2013-04-14 15:35:45', 'Stock'),
(23, 'Mythos', 0, '2013-04-14 15:35:45', 'Stock'),
(25, 'Mocha Beer', 500, '2013-04-14 15:35:45', 'Stock Update'),
(26, 'Pumpking', 500, '2013-04-14 15:35:45', 'Stock Update'),
(27, 'Rudolph', 500, '2013-04-14 15:35:45', 'Stock Update'),
(32, 'Ginger Zest', 2310, '2013-04-14 15:39:52', 'Stock'),
(30, 'Black Cherry Cider', 568, '2013-04-14 15:35:45', 'Stock'),
(31, 'Peach & Apricot Cider', 0, '2013-04-14 15:35:45', 'Stock'),
(33, 'Summer Zest', 1980, '2013-04-16 11:41:42', 'Stock'),
(96, 'Magners', 7040, '2013-05-04 11:06:39', 'Stock'),
(95, 'Carling Cider', 0, '2013-05-04 11:06:06', 'Stock'),
(94, 'Spindrift', 0, '2013-05-04 11:06:06', 'Stock'),
(93, 'Brooklyn Lager', 355, '2013-04-28 10:27:53', 'Stock'),
(92, 'Boston Lager', 660, '2013-04-28 10:27:39', 'Stock'),
(91, 'Jaipur IPA', 500, '2013-04-28 10:27:39', 'Stock');