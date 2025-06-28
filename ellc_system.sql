-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2025 at 04:09 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ellc_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `journey_tracks`
--

CREATE TABLE `journey_tracks` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `progress` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `expires_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quizzes`
--

CREATE TABLE `quizzes` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `created_at`, `updated_at`) VALUES
(3, 'Tasya', 'capstone123@gmail.com', 'pbkdf2:sha256:600000$r9wld2np5ZJvOmq8$aef5499c65d46239c4a6faf44abfdb6ddc8a40323651dac64fb8b775bd26033f', '2025-05-09 03:27:48', '2025-05-09 03:27:48'),
(4, 'Admin', 'chancaplangg@gmail.com', 'pbkdf2:sha256:600000$7v0MSYSaPQDUYZqC$538e4e81799ddacb969f0d6bc21370598812d8ecf472828691ac04798814131c', '2025-05-13 19:05:18', '2025-05-14 02:59:37');

-- --------------------------------------------------------

--
-- Table structure for table `user_sessions`
--

CREATE TABLE `user_sessions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `session_token` varchar(255) NOT NULL,
  `ip_address` varchar(45) DEFAULT NULL,
  `user_agent` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `expires_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_sessions`
--

INSERT INTO `user_sessions` (`id`, `user_id`, `session_token`, `ip_address`, `user_agent`, `created_at`, `expires_at`) VALUES
(5, 3, 'd470decc-e6d3-4240-81c6-45078e7c87a8', 'gAAAAABoHdjF3LsdVGyCc_oxop544Ehz0nTlwywebLEx-', 'gAAAAABoHdjF5YIweIQuMk1fEhyP6_XHubm9EBvIhnbxW7Kgxq5NsDsOBEGSgVgdNVs5NfANZINRgkPeqrut9rXo0kj6BTFFKvPR6nvYEuONdqVWs9CwJ82jvHjFk-zfL1JET1aqAFI4l_jk5zY9jNsn0Y5SWRbS-F5n2fyCMaa8R8J_LuOXTaCHnxnXaixUjY2kiM8n-WChvZORjVwpTnOeZvSM9cBHoR3GFCWst3YV5PXZSnMyzpk=', '2025-05-09 03:28:21', '2025-05-10 10:28:21'),
(6, 3, '88471d0f-7843-46ac-9f77-6cde74ad8452', 'gAAAAABoIy8ZCGTMKSgBpR-m3omVOGZzQF5Wjm_mQT6Dn', 'gAAAAABoIy8ZBa-G92LriX8OA-7lB9SagyxFqw4zn9rh7u-ABnKOZJz2mhjlejvOrMnB1sSehSrBrQhmkO118hJlImw-AaUheIQZ9f_ZBLmnS8l7r7mtR8APh8jyZ40NRG5dJcmnoYEucb5uH4OTV_l1JdpGMvMckH0fu9gS79xe-MequePHj9ZoEf88MILHfWZA7PXYCYYQBOJDPNEZJbWj0g4orvYUIO0_-GfQtzfH3gOuEBqlEXA=', '2025-05-13 04:38:01', '2025-05-14 11:38:01'),
(7, 4, '4a8e4f40-4fef-450a-953a-49d00fc60aa7', 'gAAAAABoI_p9omQ9CCtdh8spC01y2WvWsd97PzSYIH_A2', 'gAAAAABoI_p9G-GYZWD1_Aaa2ImgH1WJVwmcbcN3uoActZn7VdzE4oshQs30pounICUEr5fIk7dYT0Ihuhz2JFzFiEh64IkysQaRWLyBEUPitLw7_TKQ7C2Qh5LCv7_BSnG9rmKnibRliWZ5KQDig2wv4t5mSo_ABPJx2mMXGgQX8hVE7U5BW6TfGxUOidApJj_7qCBEiRBNAcUrqttY_ajk--6t8gfpkjg0KwLbQxzp_FUf4in0tyc=', '2025-05-13 19:05:49', '2025-05-15 02:05:49'),
(8, 4, '85388c1a-89b3-4e73-8b6b-400f6a5e2cd9', 'gAAAAABoJGmeJQ1RyQZKdSPv8He9yssjR8k3DAp1llK1T', 'gAAAAABoJGmeR8f2CPL9_pDL_HPLVVp0zHVYN9a5M1G0rZhUGwL6HE3AflbXaSaTkPUtoGKYjfRDJRFJv8ebVzomxSE945Mz_p4rZvNmQxN57owxxeVnSDlk_vlAaeb0K6e-aeCA4ShD9EnplbZHddf1xY4YUuYaorx3jKA8c1DUOrK1gcF08lz4dKnlhcS9uzmoW9ZdkkmbdJNWOpASq5IoVEDCOvSoSg==', '2025-05-14 02:59:58', '2025-05-15 09:59:58');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `journey_tracks`
--
ALTER TABLE `journey_tracks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `quizzes`
--
ALTER TABLE `quizzes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_sessions`
--
ALTER TABLE `user_sessions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `session_token` (`session_token`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `journey_tracks`
--
ALTER TABLE `journey_tracks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `quizzes`
--
ALTER TABLE `quizzes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_sessions`
--
ALTER TABLE `user_sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `journey_tracks`
--
ALTER TABLE `journey_tracks`
  ADD CONSTRAINT `journey_tracks_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD CONSTRAINT `password_reset_tokens_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `user_sessions`
--
ALTER TABLE `user_sessions`
  ADD CONSTRAINT `user_sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
