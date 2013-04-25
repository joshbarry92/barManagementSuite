-- 
-- Table structure for table `Beer`
-- 

CREATE TABLE `Beer` (
  `Beer` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `Brewery` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `Style` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `ABV` varchar(5) COLLATE latin1_german2_ci DEFAULT NULL,
  `Hops` double DEFAULT NULL,
  `SRM` double DEFAULT NULL,
  `Live` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_german2_ci;

-- 
-- Dumping data for table `Beer`
-- 

INSERT INTO `Beer` VALUES ('Coronita', 'Corona', 'Lager', '4.6 %', 1, 5, 100);
INSERT INTO `Beer` VALUES ('Winter Zest', 'Carling', 'Low Alcohol', '2.8 %', 1, 4, 100);
INSERT INTO `Beer` VALUES ('Guinness', 'Guinness', 'Stout', '4.1 %', 1, 23, 0);
INSERT INTO `Beer` VALUES ('Toffee Apple Cider', 'Brothers', 'Cider', '4 %', 0, 3, 0);
INSERT INTO `Beer` VALUES ('Carlsberg', 'Carlsberg', 'Lager', '5 %', 2, 7, 0);
INSERT INTO `Beer` VALUES ('Original Apple Cider', 'Brothers', 'Cider', '4.7 %', 1, 3, 0);
INSERT INTO `Beer` VALUES ('Bittersweet Apple Cider', 'Brothers', 'Cider', '5.5%', 1, 3, 100);
INSERT INTO `Beer` VALUES ('Tutti Frutti Pear Cider', 'Brothers', 'Cider', '4 %', 1, 3, 0);
INSERT INTO `Beer` VALUES ('Double Chocolate Stout', 'Young''s', 'Stout', '5.2 %', 0, 30, 100);
INSERT INTO `Beer` VALUES ('Stella 4', 'Stella Artois', 'Lager', '4 %', 2, 9, 0);
INSERT INTO `Beer` VALUES ('Stella', 'Stella Artois', 'Lager', '5.2 %', 2, 9, 0);
INSERT INTO `Beer` VALUES ('Sole Star', 'Adnams', 'Low Alcohol Ale', '2.8%', 3, 12, 100);
INSERT INTO `Beer` VALUES ('Summer Zest', 'Carling', 'Low Alcohol', '2.8 %', 1, 4, 100);
INSERT INTO `Beer` VALUES ('Alcohol Free', 'Becks', 'Low Alcohol Lager', '0 %', 2, 6, 100);
INSERT INTO `Beer` VALUES ('Farm Pressed Medium Cider', 'Perry''s', 'Cider', '5 %', 3, 9, 100);
INSERT INTO `Beer` VALUES ('2011 Vintage Cider', 'Henry Weston', 'Cider', '8.2 %', 2, 10, 100);
INSERT INTO `Beer` VALUES ('Crabbies', 'Crabbies', 'Ginger Beer', '4 %', 0, 5, 100);
INSERT INTO `Beer` VALUES ('Vintage Reserve', 'Bulmers', 'Cider', '5.5 %', 1, 3, 100);
INSERT INTO `Beer` VALUES ('Mocha Beer', 'Batemans', 'Stout', '6 %', 0, 25, 100);
INSERT INTO `Beer` VALUES ('Pumpking', 'Wychwood Brewery', 'Seasonal Ale', '4.2 %', 2, 17, 100);
INSERT INTO `Beer` VALUES ('Rudolph', 'White Horse', 'Seasonal Ale', '4.8 %', 2, 12, 100);
INSERT INTO `Beer` VALUES ('Black Cherry Cider', 'Bulmers', 'Cider', '4 %', 0, 5, 100);
INSERT INTO `Beer` VALUES ('Peach & Apricot Cider', 'Rekorderlig', 'Cider', '4 %', 0, 5, 100);
INSERT INTO `Beer` VALUES ('Ginger Zest', 'Carling', 'Low Alcohol Lager', '2.8 %', 1, 6, 100);
