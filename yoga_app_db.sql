-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 30, 2026 at 05:53 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `yoga_app_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `activity_log`
--

CREATE TABLE `activity_log` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `activity_date` date DEFAULT NULL,
  `minutes` int(11) DEFAULT 0,
  `status` enum('done','missed') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `daily_plans`
--

CREATE TABLE `daily_plans` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `day_number` int(11) DEFAULT NULL,
  `pose_ids` text DEFAULT NULL,
  `is_completed` tinyint(1) DEFAULT 0,
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `daily_plans`
--

INSERT INTO `daily_plans` (`id`, `user_id`, `day_number`, `pose_ids`, `is_completed`, `timestamp`) VALUES
(1, 1, 1, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(2, 1, 2, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(3, 1, 3, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(4, 1, 4, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(5, 1, 5, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(6, 1, 6, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(7, 1, 7, '18,34,1,32,5', 0, '2026-03-04 10:24:10'),
(8, 5, 1, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(9, 5, 2, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(10, 5, 3, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(11, 5, 4, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(12, 5, 5, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(13, 5, 6, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(14, 5, 7, '7,5,24,19,21', 0, '2026-03-04 12:17:07'),
(15, 10, 1, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(16, 10, 2, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(17, 10, 3, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(18, 10, 4, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(19, 10, 5, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(20, 10, 6, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(21, 10, 7, '9,8,28,29,7', 0, '2026-03-05 13:35:09'),
(22, 11, 1, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(23, 11, 2, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(24, 11, 3, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(25, 11, 4, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(26, 11, 5, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(27, 11, 6, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(28, 11, 7, '26,4,11,18,21', 0, '2026-03-05 13:36:18'),
(29, 12, 1, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(30, 12, 2, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(31, 12, 3, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(32, 12, 4, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(33, 12, 5, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(34, 12, 6, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(35, 12, 7, '8,5,23,1,13', 0, '2026-03-05 14:45:46'),
(36, 12, 1, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(37, 12, 2, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(38, 12, 3, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(39, 12, 4, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(40, 12, 5, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(41, 12, 6, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(42, 12, 7, '21,7,16,11,34', 0, '2026-03-05 14:46:59'),
(43, 13, 1, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(44, 13, 2, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(45, 13, 3, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(46, 13, 4, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(47, 13, 5, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(48, 13, 6, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(49, 13, 7, '15,6,34,30,10', 0, '2026-03-05 15:11:28'),
(50, 14, 1, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(51, 14, 2, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(52, 14, 3, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(53, 14, 4, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(54, 14, 5, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(55, 14, 6, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(56, 14, 7, '10,18,29,13,7', 0, '2026-03-08 13:19:50'),
(57, 14, 1, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(58, 14, 2, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(59, 14, 3, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(60, 14, 4, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(61, 14, 5, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(62, 14, 6, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(63, 14, 7, '4,11,25,30,3', 0, '2026-03-08 13:21:28'),
(71, 17, 1, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(72, 17, 2, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(73, 17, 3, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(74, 17, 4, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(75, 17, 5, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(76, 17, 6, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(77, 17, 7, '12,28,23,3,25', 0, '2026-03-11 14:05:12'),
(78, 18, 1, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(79, 18, 2, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(80, 18, 3, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(81, 18, 4, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(82, 18, 5, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(83, 18, 6, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(84, 18, 7, '33,16,14,24,32', 0, '2026-03-13 00:31:05'),
(92, 30, 1, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(93, 30, 2, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(94, 30, 3, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(95, 30, 4, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(96, 30, 5, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(97, 30, 6, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(98, 30, 7, '10,34,9,20,28', 0, '2026-03-19 11:02:32'),
(99, 16, 1, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(100, 16, 2, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(101, 16, 3, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(102, 16, 4, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(103, 16, 5, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(104, 16, 6, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(105, 16, 7, '32,1,24,15,2', 0, '2026-03-23 14:04:54'),
(106, 16, 1, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(107, 16, 2, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(108, 16, 3, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(109, 16, 4, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(110, 16, 5, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(111, 16, 6, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(112, 16, 7, '31,4,7,32,22', 0, '2026-03-27 14:34:08'),
(113, 16, 1, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(114, 16, 2, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(115, 16, 3, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(116, 16, 4, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(117, 16, 5, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(118, 16, 6, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(119, 16, 7, '22,21,16,10,17', 0, '2026-03-28 12:29:37'),
(120, 41, 1, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(121, 41, 2, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(122, 41, 3, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(123, 41, 4, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(124, 41, 5, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(125, 41, 6, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(126, 41, 7, '21,20,19,6,17', 0, '2026-03-28 12:34:31'),
(127, 42, 1, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(128, 42, 2, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(129, 42, 3, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(130, 42, 4, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(131, 42, 5, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(132, 42, 6, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(133, 42, 7, '24,5,14,34,16', 0, '2026-03-28 13:15:24'),
(134, 42, 1, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(135, 42, 2, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(136, 42, 3, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(137, 42, 4, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(138, 42, 5, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(139, 42, 6, '15,7,14,33,16', 0, '2026-03-29 09:02:18'),
(140, 42, 7, '15,7,14,33,16', 0, '2026-03-29 09:02:18');

-- --------------------------------------------------------

--
-- Table structure for table `favorites`
--

CREATE TABLE `favorites` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `video_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `journey_shots`
--

CREATE TABLE `journey_shots` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `height` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `health_status` varchar(255) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `journey_shots`
--

INSERT INTO `journey_shots` (`id`, `user_id`, `weight`, `height`, `age`, `health_status`, `image_path`, `timestamp`, `created_at`) VALUES
(1, 1, '75', '190', '23', 'Optimal Balance', 'uploads/journey_shots/1772874284_journey.jpg', '2026-03-07 14:34:44', '2026-03-09 10:29:27'),
(2, 16, NULL, NULL, NULL, NULL, NULL, '2026-03-28 12:29:58', '2026-03-28 12:29:58'),
(3, 41, NULL, NULL, NULL, NULL, NULL, '2026-03-28 12:48:57', '2026-03-28 12:48:57'),
(4, 42, NULL, NULL, NULL, NULL, NULL, '2026-03-29 17:20:03', '2026-03-29 17:20:03'),
(5, 42, NULL, NULL, NULL, NULL, NULL, '2026-03-29 17:20:13', '2026-03-29 17:20:13'),
(6, 42, NULL, NULL, NULL, NULL, NULL, '2026-03-29 17:20:18', '2026-03-29 17:20:18');

-- --------------------------------------------------------

--
-- Table structure for table `otp_verifications`
--

CREATE TABLE `otp_verifications` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `otp_code` varchar(6) NOT NULL,
  `expires_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `otp_verifications`
--

INSERT INTO `otp_verifications` (`id`, `email`, `otp_code`, `expires_at`, `created_at`) VALUES
(1, 'Somu@gmail.com', '321717', '2026-03-10 22:49:40', '2026-03-11 03:14:40'),
(6, 'ram@gmail.com', '824388', '2026-03-11 07:15:11', '2026-03-11 04:38:06'),
(26, 'test@example.com', '343422', '2026-03-23 05:14:31', '2026-03-13 07:42:07'),
(28, 'spprushoth45@gmail.com', '424497', '2026-03-13 09:18:26', '2026-03-13 09:13:26'),
(31, 'srihari02045@gmail.com', '200201', '2026-03-16 04:34:52', '2026-03-16 04:29:52'),
(32, 'madhumathi1900@gmail.com', '689000', '2026-03-27 07:25:44', '2026-03-16 04:34:30'),
(34, 'vikramaditya7032@gmail.com', '753037', '2026-03-27 08:52:05', '2026-03-17 03:48:06'),
(35, 'pradeepkumar5031485@gmail.com', '882469', '2026-03-19 05:38:46', '2026-03-19 05:33:46'),
(42, 'jaswanthsarma09@gmail.com', '124099', '2026-03-28 07:15:45', '2026-03-28 07:10:45');

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pose_id` int(11) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `session_summaries`
--

CREATE TABLE `session_summaries` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `style_name` varchar(255) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  `total_duration` int(11) DEFAULT NULL,
  `actual_duration` int(11) DEFAULT NULL,
  `completion_percentage` float DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `calories` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `session_summaries`
--

INSERT INTO `session_summaries` (`id`, `user_id`, `style_name`, `level`, `total_duration`, `actual_duration`, `completion_percentage`, `status`, `calories`, `timestamp`) VALUES
(1, 1, 'Morning Weight Loss', 'Beginner', 600, 30, 5, 'Not Completed', 0, '2026-03-13 12:41:59'),
(2, 1, 'Power Vinyasa Flow', 'Intermediate', 1200, 29, 2.41667, 'Not Completed', 0, '2026-03-16 12:53:52'),
(3, 1, 'Evening Zen', 'Beginner', 600, 40, 6.66667, 'Not Completed', 0, '2026-03-16 12:54:42'),
(4, 1, 'Inner Harmonic Yoga', 'Intermediate', 1200, 52, 4.33333, 'Not Completed', 0, '2026-03-17 09:25:15'),
(5, 1, 'Morning Weight Loss', 'Beginner', 600, 3, 0.5, 'Not Completed', 0, '2026-03-17 12:45:17'),
(6, 1, 'Morning Weight Loss', 'Beginner', 600, 178, 29.6667, 'Not Completed', 8, '2026-03-27 18:43:31'),
(7, 1, 'Morning Weight Loss', 'Beginner', 390, 63, 16.1538, 'Not Completed', 10, '2026-03-28 14:43:24'),
(8, 1, 'Gentle Flexibility', 'Beginner', 390, 130, 33.3333, 'Not Completed', 6, '2026-03-28 23:01:54');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `bio` text DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `is_verified` tinyint(1) DEFAULT 0,
  `created_at` datetime DEFAULT current_timestamp(),
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `height` varchar(50) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `goal` varchar(255) DEFAULT NULL,
  `activityLevel` varchar(255) DEFAULT NULL,
  `experience` varchar(255) DEFAULT NULL,
  `focusArea` varchar(255) DEFAULT NULL,
  `frequency` varchar(255) DEFAULT NULL,
  `dietary_plan` varchar(255) DEFAULT NULL,
  `dietaryPreference` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `phone_number`, `bio`, `password`, `is_verified`, `created_at`, `age`, `gender`, `height`, `weight`, `goal`, `activityLevel`, `experience`, `focusArea`, `frequency`, `dietary_plan`, `dietaryPreference`) VALUES
(1, 'Gh', 'Hk', NULL, NULL, '98', 1, '2026-03-11 09:48:07', '25-34', 'Male', '175', '70', 'Fitness', 'Active', 'Intermediate', 'Core', '3 times a week', NULL, NULL),
(5, 'Test', 'test@test.com', NULL, NULL, 'pass', 1, '2026-03-11 09:48:07', '25-34', 'Male', '175', '70', 'Fitness', 'Active', 'Intermediate', 'Core', '3 times a week', NULL, NULL),
(10, 'High', 'Uuu', NULL, NULL, '8', 1, '2026-03-11 09:48:07', '35-44', 'Female', '324', '434', 'Gain Muscle', 'Lightly Active', 'Intermediate', 'Back Pain', 'Daily', NULL, NULL),
(11, 'd', 'Wd', NULL, NULL, 'Hetdag-0pohgi-puncim', 1, '2026-03-11 09:48:07', '18-24', 'Female', '34', '442', 'Flexibility', 'Very Active', 'Beginner', 'Core Strength', '5-6 days', NULL, NULL),
(12, 'Sxwshny', 'Lkjgfds1234', NULL, NULL, 'dihfIx-jinvu5-xohdiz', 1, '2026-03-11 09:48:07', '18-24', 'Male', '178', '78', 'Gain Muscle', 'Lightly Active', 'Beginner', 'Full Body', '3-4 days', NULL, NULL),
(13, 'Prudhvi reddy', 'Prudhvi@gmail.com', NULL, NULL, 'Prumah@15', 1, '2026-03-11 09:48:07', '18-24', 'Male', '170', '65', 'Gain Muscle', 'Active', 'Beginner', 'Full Body', 'Daily', NULL, NULL),
(14, 'Aditya', 'Jj', NULL, NULL, '00000000', 1, '2026-03-11 09:48:07', '18-24', 'Female', '565', '76', 'Gain Muscle', 'Lightly Active', 'Intermediate', 'Core Strength', '3-4 days', NULL, NULL),
(16, 'Adi', 'vikramaditya7032@gmail.com', '7032710383', 'Zen Enthusiast', 'Aditya@2000', 1, '2026-03-11 13:40:12', '55', '', '170', '67', 'Stress Relief', NULL, 'Advanced', NULL, NULL, NULL, NULL),
(17, 'sharma', 'madhumathi1900@gmail.com', NULL, NULL, 'Madhu@1900', 1, '2026-03-11 14:04:41', '45-54', 'Female', '180', '89', 'Flexibility', 'Very Active', 'All', 'Full Body', '5-6 days', NULL, NULL),
(18, 'jaswanth', 'jaswanthsarmab@gmail.com', '9110533302', NULL, 'Adithya@123', 1, '2026-03-13 00:30:14', '18-24', 'Male', '168', '63', 'Gain Muscle', 'Lightly Active', 'Intermediate', 'Back Pain', '5-6 days', NULL, NULL),
(19, 'sri hari', 'srihari02045@gmail.com', '8122787023', NULL, 'Srihari@2004', 1, '2026-03-16 09:58:39', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(25, 'Adithya Nanda Reddy', 'singamadithya2004@gmail.com', '7032710383', 'Zen Enthusiast', 'An@123456', 1, '2026-03-16 12:51:34', '35-44', 'Male', '172', '90', 'Stress Relief', NULL, 'All', NULL, NULL, NULL, NULL),
(26, 'somuu', 'parlapallisomasekhar@gmail.com', '6304244601', NULL, 'Somu@123', 1, '2026-03-17 09:17:40', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(28, 'Adithya', '20001noway@gmail.com', '7032710383', NULL, 'An@09876', 1, '2026-03-17 09:21:47', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(29, 'dhatchu', 'dhatchu@gmail.com', '9876543210', NULL, 'Dhatchu@123', 1, '2026-03-17 12:39:16', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(30, 'pradeep', 'pradeepkumar5031485@gmail.com', NULL, NULL, 'Pradeep@123', 1, '2026-03-19 11:01:40', '18-24', 'Male', '170', '77', 'Gain Muscle', 'Active', 'Beginner', 'Full Body', '3-4 days', NULL, NULL),
(33, 'Reddy', 'mickeymousey689@gmail.com', '7032710383', NULL, 'Reddy@123', 1, '2026-03-28 11:03:50', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(40, 'New User', 'newuser_test_1774680377@test.com', '9876543210', NULL, 'NewUser@123', 1, '2026-03-28 12:16:17', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(41, 'Mallikarjuna Reddy', 'mallireddy794@gmail.com', NULL, NULL, 'Malli@123', 1, '2026-03-28 12:32:19', '18-24', 'Male', '172', '60', 'Gain Muscle', 'Very Active', 'Beginner', 'Back Pain', 'Daily', NULL, NULL),
(42, 'sateesh ', 'test@gmail.com', NULL, NULL, 'Test@123', 1, '2026-03-28 13:14:20', '67', NULL, '180', '90', 'Stress Relief', NULL, 'Beginner', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_progress`
--

CREATE TABLE `user_progress` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `height` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `health_status` varchar(255) DEFAULT NULL,
  `image_path` varchar(255) DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  `current_level` int(11) DEFAULT 0,
  `streak_days` int(11) DEFAULT 0,
  `total_minutes` int(11) DEFAULT 0,
  `sessions` int(11) DEFAULT 0,
  `bmi` float DEFAULT 0,
  `recovery_rate` int(11) DEFAULT 60
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_progress`
--

INSERT INTO `user_progress` (`id`, `user_id`, `weight`, `height`, `age`, `health_status`, `image_path`, `timestamp`, `current_level`, `streak_days`, `total_minutes`, `sessions`, `bmi`, `recovery_rate`) VALUES
(1, 1, NULL, NULL, NULL, 'Normal', NULL, '2026-03-09 10:31:16', 0, 0, 0, 0, 22, 60);

-- --------------------------------------------------------

--
-- Table structure for table `videos`
--

CREATE TABLE `videos` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `instructor` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `video_url` varchar(255) NOT NULL,
  `thumbnail_url` varchar(255) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  `duration_mins` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `videos`
--

INSERT INTO `videos` (`id`, `title`, `instructor`, `description`, `video_url`, `thumbnail_url`, `category`, `level`, `duration_mins`, `created_at`) VALUES
(1, 'Morning Yoga for Beginners', 'Sarah Zen', 'A gentle morning flow to wake up your body.', 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b', 'Morning Yoga', 'Beginner', 15, '2026-03-12 21:27:22'),
(2, 'Power Vinyasa Flow', 'Mike Strong', 'High intensity yoga for strength and flexibility.', 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4', 'https://images.unsplash.com/photo-1506126613408-eca07ce68773', 'Full Body', 'Intermediate', 30, '2026-03-12 21:27:22'),
(3, 'Stress Relief Relaxation', 'Luna Calm', 'Deep breathing and calming poses for evening.', 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4', 'https://images.unsplash.com/photo-1599447421416-3414502d1820', 'Relaxation', 'Beginner', 20, '2026-03-12 21:27:22'),
(4, 'Advanced Power Flow', 'Master Ryu', 'Intense yoga for pro users.', 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4', 'https://images.unsplash.com/photo-1575052814086-f385e2e2ad1b', 'Full Body', 'Advanced', 45, '2026-03-12 21:38:53'),
(5, 'Deep Tissue Relaxation', 'Emma Soft', 'Targeted relaxation for muscle recovery.', 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4', 'https://images.unsplash.com/photo-1510894347713-fc3ad6cb0d4d', 'Relaxation', 'Intermediate', 25, '2026-03-12 21:38:53');

-- --------------------------------------------------------

--
-- Table structure for table `yoga_poses`
--

CREATE TABLE `yoga_poses` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `difficulty` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `yoga_poses`
--

INSERT INTO `yoga_poses` (`id`, `name`, `description`, `difficulty`) VALUES
(1, 'Supine Twist', 'Yoga posture for supine twist exercise.', 'beginner'),
(2, 'Legs Up Wall', 'Yoga posture for legs up wall exercise.', 'beginner'),
(3, 'Childs Pose', 'Yoga posture for childs pose exercise.', 'beginner'),
(4, 'Happy Baby', 'Yoga posture for happy baby exercise.', 'beginner'),
(5, 'Savasana', 'Yoga posture for savasana exercise.', 'beginner'),
(6, 'Sun Salut', 'Yoga posture for sun salut exercise.', 'beginner'),
(7, 'Warrior 1', 'Yoga posture for warrior 1 exercise.', 'beginner'),
(8, 'High Plank', 'Yoga posture for high plank exercise.', 'beginner'),
(9, 'Downward Dog', 'Yoga posture for downward dog exercise.', 'beginner'),
(10, 'Warrior 2', 'Yoga posture for warrior 2 exercise.', 'beginner'),
(11, 'Boat', 'Yoga posture for boat exercise.', 'beginner'),
(12, 'Bridge', 'Yoga posture for bridge exercise.', 'beginner'),
(13, 'Lotus', 'Yoga posture for lotus exercise.', 'beginner'),
(14, 'Triangle', 'Yoga posture for triangle exercise.', 'beginner'),
(15, 'Tree', 'Yoga posture for tree exercise.', 'beginner'),
(16, 'Crow', 'Yoga posture for crow exercise.', 'beginner'),
(17, 'Seated Twist', 'Yoga posture for seated twist exercise.', 'beginner'),
(18, 'Side Stretch', 'Yoga posture for side stretch exercise.', 'beginner'),
(19, 'Pigeon', 'Yoga posture for pigeon exercise.', 'beginner'),
(20, 'Goddess', 'Yoga posture for goddess exercise.', 'beginner'),
(21, 'Half Moon', 'Yoga posture for half moon exercise.', 'beginner'),
(22, 'Butterfly', 'Yoga posture for butterfly exercise.', 'beginner'),
(23, 'Wall Squat', 'Yoga posture for wall squat exercise.', 'beginner'),
(24, 'Wall Bridge', 'Yoga posture for wall bridge exercise.', 'beginner'),
(25, 'Wall Plank', 'Yoga posture for wall plank exercise.', 'beginner'),
(26, 'Wall Pushup', 'Yoga posture for wall pushup exercise.', 'beginner'),
(27, 'Wall Circles', 'Yoga posture for wall circles exercise.', 'beginner'),
(28, 'Wall Climbers', 'Yoga posture for wall climbers exercise.', 'beginner'),
(29, 'Wall Handstand', 'Yoga posture for wall handstand exercise.', 'beginner'),
(30, 'Warrior 3', 'Yoga posture for warrior 3 exercise.', 'beginner'),
(31, 'Handstand', 'Yoga posture for handstand exercise.', 'beginner'),
(32, 'Forearm Plank', 'Yoga posture for forearm plank exercise.', 'beginner'),
(33, 'Wild Thing', 'Yoga posture for wild thing exercise.', 'beginner'),
(34, 'Scorpion', 'Yoga posture for scorpion exercise.', 'beginner');

-- --------------------------------------------------------

--
-- Table structure for table `yoga_progress`
--

CREATE TABLE `yoga_progress` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `video_id` int(11) DEFAULT NULL,
  `time_watched` int(11) DEFAULT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  `date_completed` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `activity_log`
--
ALTER TABLE `activity_log`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_user_date` (`user_id`,`activity_date`);

--
-- Indexes for table `daily_plans`
--
ALTER TABLE `daily_plans`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `favorites`
--
ALTER TABLE `favorites`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_favorite` (`user_id`,`video_id`),
  ADD KEY `video_id` (`video_id`);

--
-- Indexes for table `journey_shots`
--
ALTER TABLE `journey_shots`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `otp_verifications`
--
ALTER TABLE `otp_verifications`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `email_2` (`email`),
  ADD UNIQUE KEY `email_3` (`email`),
  ADD UNIQUE KEY `email_4` (`email`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `pose_id` (`pose_id`);

--
-- Indexes for table `session_summaries`
--
ALTER TABLE `session_summaries`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_progress`
--
ALTER TABLE `user_progress`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `videos`
--
ALTER TABLE `videos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yoga_poses`
--
ALTER TABLE `yoga_poses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yoga_progress`
--
ALTER TABLE `yoga_progress`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `video_id` (`video_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `activity_log`
--
ALTER TABLE `activity_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `daily_plans`
--
ALTER TABLE `daily_plans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;

--
-- AUTO_INCREMENT for table `favorites`
--
ALTER TABLE `favorites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `journey_shots`
--
ALTER TABLE `journey_shots`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `otp_verifications`
--
ALTER TABLE `otp_verifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `session_summaries`
--
ALTER TABLE `session_summaries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `user_progress`
--
ALTER TABLE `user_progress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `videos`
--
ALTER TABLE `videos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `yoga_poses`
--
ALTER TABLE `yoga_poses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `yoga_progress`
--
ALTER TABLE `yoga_progress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `daily_plans`
--
ALTER TABLE `daily_plans`
  ADD CONSTRAINT `daily_plans_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `favorites`
--
ALTER TABLE `favorites`
  ADD CONSTRAINT `favorites_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `favorites_ibfk_2` FOREIGN KEY (`video_id`) REFERENCES `videos` (`id`);

--
-- Constraints for table `journey_shots`
--
ALTER TABLE `journey_shots`
  ADD CONSTRAINT `journey_shots_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `sessions`
--
ALTER TABLE `sessions`
  ADD CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `sessions_ibfk_2` FOREIGN KEY (`pose_id`) REFERENCES `yoga_poses` (`id`);

--
-- Constraints for table `session_summaries`
--
ALTER TABLE `session_summaries`
  ADD CONSTRAINT `session_summaries_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `user_progress`
--
ALTER TABLE `user_progress`
  ADD CONSTRAINT `user_progress_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `yoga_progress`
--
ALTER TABLE `yoga_progress`
  ADD CONSTRAINT `yoga_progress_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `yoga_progress_ibfk_2` FOREIGN KEY (`video_id`) REFERENCES `videos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
