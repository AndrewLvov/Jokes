-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Хост: 127.0.0.1
-- Время создания: Янв 09 2014 г., 01:36
-- Версия сервера: 5.5.27
-- Версия PHP: 5.4.7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `fun`
--

-- --------------------------------------------------------

--
-- Структура таблицы `jokes`
--

CREATE TABLE IF NOT EXISTS `jokes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(1024) NOT NULL,
  `text` varchar(8196) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `jokes`
--

INSERT INTO `jokes` (`id`, `url`, `text`, `rating`) VALUES
(1, 'http://google.com', 'гугл - это вам не шутки!', 3),
(2, 'http://bash.im/quote/426216', 'xxx: Мой сын - официант. Насчёт стакана воды перед смертью я могу быть спокоен.\nxxx: Главное - чаевые под рукой держать.', 3269),
(3, 'http://bash.im/quote/426212', 'Zibx:\nкупил себе вчера телевизор. брался как здоровый монитор, даже антенну втыкать не буду. так эта зараза тянет рекламу по вайфаю, и показывает её мне в меню.', 1370);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
