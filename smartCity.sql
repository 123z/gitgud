-- MySQL dump 10.13  Distrib 5.7.18, for Win64 (x86_64)
--
-- Host: localhost    Database: smartctiy
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `adminID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(80) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`adminID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collegedepartments`
--

DROP TABLE IF EXISTS `collegedepartments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `collegedepartments` (
  `locationDepartmentID` int(11) NOT NULL,
  `department` varchar(45) DEFAULT NULL,
  KEY `locationDepartmentID` (`locationDepartmentID`),
  CONSTRAINT `locationDepartmentID` FOREIGN KEY (`locationDepartmentID`) REFERENCES `location` (`locationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collegedepartments`
--

LOCK TABLES `collegedepartments` WRITE;
/*!40000 ALTER TABLE `collegedepartments` DISABLE KEYS */;
INSERT INTO `collegedepartments` VALUES (3,'Business, Economics & Law'),(3,'Business, Economics & Law'),(3,'Science'),(3,'Humanities & Social Sciences'),(3,'Health & Behavioural Science'),(3,'Information Technology'),(3,'Engineering'),(3,'Agriculture'),(3,'Business'),(1,'Creative Industries'),(1,'Education'),(1,'Health'),(1,'Law'),(1,'Science & Engineering');
/*!40000 ALTER TABLE `collegedepartments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `industrytypes`
--

DROP TABLE IF EXISTS `industrytypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `industrytypes` (
  `locationIndustryID` int(11) NOT NULL,
  `industryType` varchar(45) DEFAULT NULL,
  KEY `locationID_idx` (`locationIndustryID`),
  CONSTRAINT `locationIndustryID` FOREIGN KEY (`locationIndustryID`) REFERENCES `location` (`locationID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `industrytypes`
--

LOCK TABLES `industrytypes` WRITE;
/*!40000 ALTER TABLE `industrytypes` DISABLE KEYS */;
INSERT INTO `industrytypes` VALUES (2,'Finance'),(6,'Health');
/*!40000 ALTER TABLE `industrytypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `locationID` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `address` varchar(80) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `phoneNumber` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(80) DEFAULT NULL,
  `locationType` enum('College','Library','Industry','Hotel','Park','Zoo','Museum','Restaurant','Mall') DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`locationID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Queensland University of Technology','2 George ST','Brisbane','31382000','askqut@qut.edu.au','College','https://www.qut.edu.au/'),(2,'BOQ Private Banking','Level 6, 100 Skyring Ter, NewStead','Brisbane','1300764439',NULL,'Industry','http://www.boq.com.au/personal_privatebank_contact.htm'),(3,'University of Queensland','The University of Queensland St Lucia','Brisbane','3365111','askus@library.uq.edu.au','College','http://www.uq.edu.au/'),(4,'Brisbane Square Library','166 George ST ','Brisbane','34034166',NULL,'Library','https://www.brisbane.qld.gov.au/facilities-recreation/libraries'),(5,'West End Library','178-180 Boundary ST','Brisbane','34038620',NULL,'Library','https://www.brisbane.qld.gov.au/facilities-recreation/libraries'),(6,'QLD Department of Health','33 Charlotte Street','Brisbane','32340111',NULL,'Industry','https://www.health.qld.gov.au/');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `emailAddress` varchar(80) DEFAULT NULL,
  `userType` enum('Businessman','Student','Tourist') DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-09-13 13:14:56
