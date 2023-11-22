CREATE DATABASE Grocery;
USE Grocery;

DROP TABLE IF EXISTS `grocery_batch`;

CREATE TABLE `grocery_batch` (
  `G_SKU` varchar(4) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Expiration_Date` date DEFAULT NULL,
  PRIMARY KEY (`G_SKU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `grocery_batch` WRITE;

UNLOCK TABLES;

DROP TABLE IF EXISTS `sample_grocery`;

CREATE TABLE `sample_grocery` (
  `S_SKU` varchar(4) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Descripción` varchar(50) DEFAULT NULL,
  `Price` float DEFAULT NULL,
  `Quantity` int(11) DEFAULT NULL,
  `Expriation_date` date DEFAULT NULL,
  PRIMARY KEY (`S_SKU`),
  CONSTRAINT `sample_grocery_FK` FOREIGN KEY (`S_SKU`) REFERENCES `grocery_batch` (`G_SKU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

LOCK TABLES `sample_grocery` WRITE;

UNLOCK TABLES;