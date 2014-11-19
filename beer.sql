-- 
-- Table structure for table `Beer`
-- 11/9 added in an image field to hold picture of label
-- 

CREATE TABLE `Beer` (
  `Beer` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `Brewery` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `Style` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL,
  `ABV` varchar(5) COLLATE latin1_german2_ci DEFAULT NULL,
  `Hops` double DEFAULT NULL,
  `SRM` double DEFAULT NULL,
  `Live` double DEFAULT NULL,
  `Img` varchar(255) COLLATE latin1_german2_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_german2_ci;

-- 
-- Dumping data for table `Beer`
-- 

INSERT INTO `Beer` (`Beer`, `Brewery`, `Style`, `ABV`, `Hops`, `SRM`, `Live`) VALUES
('Coronita', 'Corona', 'Mexican Lager', '4.6 %', 1, 5, 100),
('Winter Zest', 'Carling', 'Low Alcohol Lager', '2.8 %', 1, 4, 100),
('Guinness', 'Guinness', 'Stout', '4.1 %', 1, 23, 0),
('Toffee Apple Cider', 'Brothers', 'Cider', '4 %', 0, 3, 0),
('Carlsberg', 'Carlsberg', 'Lager', '5 %', 2, 7, 100),
('Original Apple Cider', 'Brothers', 'Cider', '4.7 %', 1, 3, 0),
('Bittersweet Apple Cider', 'Brothers', 'Cider', '5.5%', 1, 3, 100),
('Tutti Frutti Pear Cider', 'Brothers', 'Cider', '4 %', 1, 99, 0),
('Double Chocolate Stout', 'Young''s', 'Stout', '5.2 %', 0, 30, 100),
('Stella 4', 'Stella Artois', 'Lager', '4 %', 2, 9, 0),
('Stella', 'Stella Artois', 'Lager', '5.2 %', 2, 9, 0),
('Sole Star', 'Adnams', 'Low Alcohol Ale', '2.8%', 3, 12, 100),
('Summer Zest', 'Carling', 'Low Alcohol Lager', '2.8 %', 1, 4, 100),
('Alcohol Free', 'Becks', 'Low Alcohol Lager', '0 %', 2, 6, 100),
('Farm Pressed Medium Cider', 'Perry''s', 'Cider', '5 %', 3, 9, 100),
('2011 Vintage Cider', 'Henry Weston', 'Cider', '8.2 %', 2, 10, 100),
('Crabbies', 'Crabbies', 'Ginger Beer', '4 %', 0, 5, 100),
('Mythos', 'Mythos', 'Lager', '4.7 %', 1, 5, 0),
('Vintage Reserve', 'Bulmers', 'Cider', '5.5 %', 1, 3, 0),
('Mocha Beer', 'Batemans', 'Stout', '6 %', 0, 25, 100),
('Pumpking', 'Wychwood Brewery', 'Seasonal Ale', '4.2 %', 2, 17, 100),
('Rudolph', 'White Horse', 'Seasonal Ale', '4.8 %', 2, 12, 100),
('Black Cherry Cider', 'Bulmers', 'Cider', '4 %', 0, 99, 100),
('Peach & Apricot Cider', 'Rekorderlig', 'Cider', '4 %', 0, 5, 0),
('Ginger Zest', 'Carling', 'Low Alcohol Lager', '2.8 %', 1, 6, 100),
('Jaipur IPA', 'Thornbridge', 'IPA', '5.9 %', 2, 15, 100),
('Brooklyn Lager', 'Brooklyn Brewery', 'Lager', '5.2 %', 1, 20, 100),
('Boston Lager', 'Samuel Adams', 'Lager', '4.8 %', 1, 15, 100),
('Spindrift', 'Adnams', 'Blonde', '5 %', 1, 10, 0),
('Carling Cider', 'Carling', 'Cider', '4.5 %', 1, 5, 0),
('Magners', 'Magners', 'Cider', '4.5 %', 1, 5, 100),
('Fosters', 'Fosters', 'Lager', '4 %', 1, 8, 0),
('Corona', 'Corona', 'Mexican Lager', '4.6 %', 1, 5, 0),
('Strawberry Cider', 'Brothers', 'Cider', '4 %', 0, 98, 0),
('Corona Light', 'Corona', 'Mexican Lager', '3.7 %', 0, 5, 0),
('Strawberry and Lime Cider', 'Kopparberg', 'Cider', '4 %', 0, 98, 0),
('Pear Cider', 'Kopparberg', 'Cider', '4.5 %', 0, 4, 0),
('Naked Apple Cider', 'Kopparberg', 'Cider', '4.5 %', 0, 4, 0),
('Blueberry Cider', 'St. Helier', 'Cider', '5 %', 0, 97, 0);
