-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: localhost    Database: django_model_test
-- ------------------------------------------------------
-- Server version	5.7.9-log

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
-- Table structure for table `money`
--

DROP TABLE IF EXISTS `money`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `money` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `player_id` int(11) NOT NULL,
  `currency_id` varchar(20) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player_id_idx` (`player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `money`
--

LOCK TABLES `money` WRITE;
/*!40000 ALTER TABLE `money` DISABLE KEYS */;
INSERT INTO `money` VALUES (1,1,'BYN',100,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (2,2,'BYN',200,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (3,3,'BYN',300,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (4,4,'BYN',400,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (5,5,'BYN',500,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (10,5,'dead_crystals',1000,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (11,4,'dead_crystals',100,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (12,3,'dead_crystals',2000,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (13,2,'dead_crystals',200,'2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `money` VALUES (14,1,'dead_crystals',1000,'2016-01-08 00:00:00','2016-01-08 00:00:00');
/*!40000 ALTER TABLE `money` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (1,'Vasya','vasya@tut.by','1','2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `player` VALUES (2,'Petya','petya@tut.by','2','2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `player` VALUES (3,'Lesha','lesha@tut.by','3','2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `player` VALUES (4,'Monster','monster@gmail.com','4','2016-01-08 00:00:00','2016-01-08 00:00:00');
INSERT INTO `player` VALUES (5,'test','test@mail.ru','test','2016-01-08 00:00:00','2016-01-08 00:00:00');
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-08 18:03:54
