-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema quotes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema quotes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `quotes_api` DEFAULT CHARACTER SET latin1 ;
USE `quotes_api` ;

-- -----------------------------------------------------
-- Table `quotes`.`quotes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quotes_api`.`quotes` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
      `quote` TEXT NULL DEFAULT NULL,
        `author` VARCHAR(255) NULL DEFAULT NULL,
          PRIMARY KEY (`id`))
          ENGINE = InnoDB
          AUTO_INCREMENT = 11
          DEFAULT CHARACTER SET = latin1;


          SET SQL_MODE=@OLD_SQL_MODE;
          SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
          SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (1,'Learn the rules like a pro, so you can break them like an artist.','Pablo Picasso');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (2,'Java is to JavaScript what Car is to Carpet. ','Chris Heilmann');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (3,'If debugging is the process of removing software bugs, then programming must be the process of putting them in.','Edsger Dijkstra');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (4,'Any fool can write code that a computer can understand. Good programmers write code that humans can understand. ','Martin Fowler');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (5,'Computers are good at following instructions, but not at reading your mind.','Donald Knuth');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (6,'Measuring programming progress by lines of code is like measuring aircraft building progress by weight.','Bill Gates');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (7,'There are only two kinds of languages: the ones people complain about and the ones nobody uses','Bjarne Stroustrup');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (8,'It\'s all talk until the code runs.','Ward Cunningham');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (9,'A clever person solves a problem. A wise person avoids it.','Albert Einstein');
          INSERT INTO `quotes` (`id`,`quote`,`author`) VALUES (10,'Being a good software engineer is 3% talent, 97% not being distracted by the internet.','Unknown');

