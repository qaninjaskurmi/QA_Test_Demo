-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Oct 04, 2020 at 07:24 PM
-- Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `app`
--

-- --------------------------------------------------------

--
-- Table structure for table `statement`
--

CREATE TABLE `statement` (
  `id` int(11) NOT NULL,
  `account_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` datetime NOT NULL,
  `amount` decimal(16,6) NOT NULL,
  `currency` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `to_date_turnover_amount` decimal(16,6) DEFAULT NULL,
  `to_date_turnover_currency` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `statement`
--

INSERT INTO `statement` (`id`, `account_id`, `date`, `amount`, `currency`, `to_date_turnover_amount`, `to_date_turnover_currency`) VALUES
(343, '1', '2020-09-24 20:35:20', '1999000900.000001', 'EUR', '9995018962.000001', 'EUR'),
(342, '1', '2020-09-24 20:35:20', '1999000900.000001', 'EUR', '7996018062.000000', 'EUR'),
(341, '1', '2020-09-24 20:35:20', '1999000900.000000', 'EUR', '5997017162.000000', 'EUR'),
(340, '1', '2020-09-24 20:35:20', '1999000900.000000', 'EUR', '3998016262.000000', 'EUR'),
(339, '1', '2020-09-24 20:35:20', '1999000000.000000', 'EUR', '1999016262.000000', 'EUR'),
(338, '1', '2020-09-24 20:35:20', '1999000000.000000', 'EUR', '16262.000000', 'EUR');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `statement`
--
ALTER TABLE `statement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_C0DB51769B6B5FBAAA9E377A` (`account_id`,`date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `statement`
--
ALTER TABLE `statement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=344;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
