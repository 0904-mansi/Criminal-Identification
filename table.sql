-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 26, 2022 at 10:04 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `criminaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `criminaldata`
--

CREATE TABLE `criminaldata` (
  `Criminal-ID` int(6) NOT NULL,
  `Address` varchar(40) NOT NULL,
  `Phone` int(12) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father's Name` varchar(30) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB(yyyy-mm-dd)` date NOT NULL,
  `Crimes Done` varchar(40) NOT NULL,
  `Date of Arrest` date NOT NULL,
  `Place of Arrest` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `criminaldata`
--

INSERT INTO `criminaldata` (`Criminal-ID`, `Address`, `Phone`, `Name`, `Father's Name`, `Gender`, `DOB(yyyy-mm-dd)`, `Crimes Done`, `Date of Arrest`, `Place of Arrest`) VALUES
(123456, 'jaipur', 0, 'vivek rati', 'mahesh rathi', 'male', '2000-09-07', 'fraud', '2020-12-09', 'chhattisgarh'),
(234, 'jabalpur', 0, 'jaydeep singh', 'mahendra singh', 'male', '1970-09-08', 'fraud', '2009-08-07', 'jabalpur'),
(567432, 'delhi', 0, 'pranav verma', 'ramesh verma', 'male', '2000-05-04', 'murder', '2000-05-04', 'aagra'),
(876594, 'jharkhand', 0, 'mehul sharma', 'mahesh sharma', 'male', '1999-09-09', 'fraud', '1999-09-09', 'odisha'),
(1234, 'dfg', 0, 'bjk', 'mn', 'm', '1990-09-08', 'b,j', '2000-09-08', 'hv'),
(123456, 'h', 0, 'c', 'c', 'c', '1990-08-09', 'd', '1990-08-09', 'd'),
(89, 'gh', 0, 'nmk', ' h', 'm', '1998-09-08', 'vb', '1998-09-08', 'cgj'),
(409087, 'delhi', 0, 'rajesh yadav', 'brijesh yadav', 'male', '1978-09-08', 'fraud', '2019-08-09', 'mumbai'),
(4, 'g', 0, 'v', 'v', 'v', '2020-09-09', 'm', '2020-09-09', 'g'),
(98, 'v', 0, 'c', 'c', 'c', '2020-09-09', 'f', '2020-09-09', 'f'),
(4, 'g', 47, 'cfc', 'fre', 'm', '2020-09-09', 'm', '2020-09-09', 'v');

-- --------------------------------------------------------

--
-- Table structure for table `missingdata`
--

CREATE TABLE `missingdata` (
  `Report-ID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father's Name` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Phone` int(12) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Identification` varchar(50) NOT NULL,
  `Date of Missing` date NOT NULL,
  `Place of Missing` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `missingdata`
--

INSERT INTO `missingdata` (`Report-ID`, `Name`, `Father's Name`, `Address`, `Phone`, `Gender`, `DOB`, `Identification`, `Date of Missing`, `Place of Missing`) VALUES
(1234, 'a', 'a', 'a', 0, 'a', '2002-09-07', 'a', '2002-08-09', 'a'),
(76, 'n', 'n', 'n', 0, 'm', '1998-09-08', 'm', '1998-09-08', 'm'),
(857, 'b', 'g', 'g', 0, 'm', '2020-09-09', 'g', '2020-09-09', 'g'),
(908078, 'rajesh yadav', 'brijesh yadav', 'mumbai', 0, 'male', '2020-09-09', 'mole on nose', '2020-09-09', 'delhi'),
(8749, 'h', 'h', 'h', 0, 'm', '2020-09-09', 'njk', '2020-09-09', 'fg'),
(987896, 'dd', 'd', 'd', 987987987, 'd', '2020-09-09', 'd', '2020-09-09', 'd');

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`id`, `first_name`, `last_name`, `gender`, `username`, `password`) VALUES
(14, 'Danish', 'Ali', '', 'masterprograming', 'Welcome@12'),
(15, 'Mansi', 'Mishra', '', 'mansi', 'mansi0904'),
(16, 'Margi', 'Mishra', '', 'Margi', 'margi0306'),
(17, 'b', 'v', '', 'op', 'bh'),
(18, 'w', 'f', '', 'b', '1234'),
(19, 'Sakshi', 'Mishra', '', 'Sakshi', 'sakshi1907'),
(20, 'Kunjal', 'Ramteke', '', 'Kunjal', '1234'),
(21, 'Pranjal', 'Hinduja', '', 'pranjal', '1234'),
(22, 'Adiba', 'Noor', '', 'adiba', '1234'),
(23, 'a', 'a', '', 'a', 'a'),
(24, 'munna', 'yadav', '', 'munna', '1234'),
(25, 'Ranu', 'c', '', 'd', 'd'),
(26, 'manu', 'bin', 'Male', 'sa', 'sa'),
(27, 'z', 'z', 'Male', 'z', 'z'),
(28, 'g', 'g', 'Male', 'g', 'g');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_information`
--
ALTER TABLE `user_information`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_information`
--
ALTER TABLE `user_information`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;
