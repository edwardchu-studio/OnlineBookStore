/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : onlineorder

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 20/06/2019 10:15:11
*/
-- CREATE DATABASE `Test`;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS `BookOnline`;

/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `BookOnline` CHARACTER SET utf8 COLLATE utf8_general_ci;

USE `BookOnline`;

DROP TABLE IF EXISTS `Buyer`;
CREATE TABLE `Buyer`(
    `BuyerID` INT NOT NULL AUTO_INCREMENT,
    `LoginPassword` VARCHAR(120) NOT NULL,
    `UserName` VARCHAR(40) NOT NULL unique,
    `Email` VARCHAR(60) NOT NULL unique,
    CONSTRAINT `PK_Buyer` PRIMARY KEY (`BuyerId`)
);

DROP TABLE IF EXISTS `Book`;
CREATE TABLE `Book` (
  `SellerID` INT NOT NULL ,
  `BookID` int(11) NOT NULL AUTO_INCREMENT,
  `BookName` varchar(255) NOT NULL,
  `ISBN` varchar(255) NOT NULL,
  `Category` varchar(13) NOT NULL,
  `Price` decimal(10,2) NOT NULL,
  `SellPrice` decimal(10,2) NOT NULL,
  `Content`varchar(2500) NOT NULL,
  `Wanted` boolean DEFAULT NULL,
  `ImageURL` varchar(255)DEFAULT NULL,
  CONSTRAINT `Book_ibfk_1` FOREIGN KEY (`SellerID`) REFERENCES `Buyer` (`BuyerID`),
  CONSTRAINT `PK_Book` PRIMARY KEY (`BookID`)
);

DROP TABLE IF EXISTS `Order`;
CREATE TABLE `Order` (
  `OrderID` int(11) NOT NULL AUTO_INCREMENT,
  `BuyerID` int(11) NOT NULL,
  `SellerID` int(11) NOT NULL,
  `BookID` int(11) NOT NULL,
  `OrderTime` timestamp DEFAULT NULL,
  `SellPrice` decimal(25,2) NOT NULL,
  `isSend` boolean NOT NULL,
  `Address`varchar(255) DEFAULT NULL,
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`BuyerID`) REFERENCES `Buyer` (`BuyerID`),
  CONSTRAINT `order_ibfk_2` FOREIGN KEY (`SellerID`) REFERENCES `Buyer` (`BuyerID`),
  CONSTRAINT `order_ibfk_3` FOREIGN KEY (`BookID`) REFERENCES `Book` (`BookID`),
  CONSTRAINT `PK_Order` PRIMARY KEY (`OrderID`)
);
