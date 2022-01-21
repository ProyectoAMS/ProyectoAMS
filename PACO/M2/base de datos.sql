DROP DATABASE IF EXISTS `AMS`;
CREATE SCHEMA IF NOT EXISTS `AMS`;
USE `AMS` ;


CREATE TABLE IF NOT EXISTS `AMS`.`ADVENTURE` (
  `ID_ADVENTURE` INT NOT NULL AUTO_INCREMENT,
  `adventure_name` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(5000) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_ADVENTURE`),
  UNIQUE INDEX `id_adventure_UNIQUE` (`ID_ADVENTURE` ASC) VISIBLE);


CREATE TABLE IF NOT EXISTS `AMS`.`CHARACTER` (
  `ID_CHARACTER` INT NOT NULL AUTO_INCREMENT,
  `character_name` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(5000) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_CHARACTER`),
  UNIQUE INDEX `character_name_UNIQUE` (`character_name` ASC) VISIBLE,
  UNIQUE INDEX `id_character_UNIQUE` (`ID_CHARACTER` ASC) VISIBLE);



CREATE TABLE IF NOT EXISTS `AMS`.`CHARACTER_HAS_ADVENTURE` (
  `FK_CHARACTER_ID_CHARACTER` INT NOT NULL AUTO_INCREMENT,
  `FK_ADVENTURE_ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`FK_CHARACTER_ID_CHARACTER`, `FK_ADVENTURE_ID_ADVENTURE`),
  INDEX `fk_CHARACTER_has_ADVENTURE_ADVENTURE1_idx` (`FK_ADVENTURE_ID_ADVENTURE` ASC) VISIBLE,
  INDEX `fk_CHARACTER_has_ADVENTURE_CHARACTER1_idx` (`FK_CHARACTER_ID_CHARACTER` ASC) VISIBLE,
  CONSTRAINT `FK_CHARACTER_has_ADVENTURE_ADVENTURE1`
    FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`),
  CONSTRAINT `FK_CHARACTER_has_ADVENTURE_CHARACTER1`
    FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`));


CREATE TABLE IF NOT EXISTS `AMS`.`USER` (
  `ID_USER` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_USER`),
  UNIQUE INDEX `user_name_unique` (`user_name` ASC) VISIBLE,
  UNIQUE INDEX `id_user_UNIQUE` (`ID_USER` ASC) VISIBLE);


CREATE TABLE IF NOT EXISTS `AMS`.`GAME` (
  `ID_GAME` INT NOT NULL AUTO_INCREMENT,
  `current_date` DATETIME NULL DEFAULT NULL,
  `FK_USER_ID_USER` INT NOT NULL,
  `FK_ADVENTURE_ID_ADVENTURE` INT NOT NULL,
  `FK_CHARACTER_ID_CHARACTER` INT NOT NULL,
  PRIMARY KEY (`ID_GAME`, `FK_USER_ID_USER`, `FK_ADVENTURE_ID_ADVENTURE`, `FK_CHARACTER_ID_CHARACTER`),
  INDEX `fk_GAME_USER_idx` (`FK_USER_ID_USER` ASC) VISIBLE,
  INDEX `fk_GAME_ADVENTURE_idx` (`FK_ADVENTURE_ID_ADVENTURE` ASC) VISIBLE,
  INDEX `fk_GAME_CHARACTER_idx` (`FK_CHARACTER_ID_CHARACTER` ASC) VISIBLE,
  UNIQUE INDEX `id_game_UNIQUE` (`ID_GAME` ASC) VISIBLE,
  CONSTRAINT `FK_GAME_ADVENTURE`
    FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`),
  CONSTRAINT `FK_GAME_CHARACTER`
    FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`),
  CONSTRAINT `FK_GAME_USER`
    FOREIGN KEY (`FK_USER_ID_USER`)
    REFERENCES `AMS`.`USER` (`ID_USER`));


CREATE TABLE IF NOT EXISTS `AMS`.`STEP` (
  `ID_STEP` INT NOT NULL AUTO_INCREMENT,
  `step_description` VARCHAR(5000) NULL DEFAULT NULL,
  `end` BIT(1) NULL DEFAULT NULL,
  `FK_ADVENTURE_ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`ID_STEP`, `FK_ADVENTURE_ID_ADVENTURE`),
  INDEX `fk_STEP_ADVENTURE_idx` (`FK_ADVENTURE_ID_ADVENTURE` ASC) VISIBLE,
  UNIQUE INDEX `id_step_UNIQUE` (`ID_STEP` ASC) VISIBLE,
  CONSTRAINT `FK_STEP_ADVENTURE`
    FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`));


CREATE TABLE IF NOT EXISTS `AMS`.`OPTION` (
  `ID_OPTION` INT NOT NULL AUTO_INCREMENT,
  `option_description` VARCHAR(5000) NULL DEFAULT NULL,
  `answer` VARCHAR(5000) NULL DEFAULT NULL,
  `go_step` INT NULL DEFAULT NULL,
  `FK_STEP_ID_STEP` INT NOT NULL,
  `FK_STEP_ADVENTURE_ID_ADVENTURE` INT NOT NULL,
  PRIMARY KEY (`ID_OPTION`, `FK_STEP_ID_STEP`, `FK_STEP_ADVENTURE_ID_ADVENTURE`),
  INDEX `fk_option_step1_idx` (`FK_STEP_ID_STEP` ASC, `FK_STEP_ADVENTURE_ID_ADVENTURE` ASC) VISIBLE,
  UNIQUE INDEX `id_option_UNIQUE` (`ID_OPTION` ASC) VISIBLE,
  
  CONSTRAINT `FK_OPTION_STEP`
    FOREIGN KEY (`FK_STEP_ID_STEP` , `FK_STEP_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`STEP` (`ID_STEP` , `FK_ADVENTURE_ID_ADVENTURE`));


CREATE TABLE IF NOT EXISTS `AMS`.`DECISION` (
  `ID_DECEISION` INT NOT NULL AUTO_INCREMENT,
  `FK_GAME_ID_GAME` INT NOT NULL,
  `FK_GAME_USER_ID_USER` INT NOT NULL,
  `FK_GAME_ADVENTURE_ID_ADVENTURE` INT NOT NULL,
  `FK_GAME_CHARACTER_ID_CHARACTER` INT NOT NULL,
  `FK_OPTION_ID_OPTION` INT NOT NULL,
  PRIMARY KEY (`ID_DECEISION`, `FK_GAME_ID_GAME`, `FK_GAME_USER_ID_USER`, `FK_GAME_ADVENTURE_ID_ADVENTURE`, `FK_GAME_CHARACTER_ID_CHARACTER`, `FK_OPTION_ID_OPTION`),
  INDEX `fk_DECISION_GAME1_idx` (`FK_GAME_ID_GAME` ASC, `FK_GAME_USER_ID_USER` ASC, `FK_GAME_ADVENTURE_ID_ADVENTURE` ASC, `FK_GAME_CHARACTER_ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_DECISION_OPTION1_idx` (`FK_OPTION_ID_OPTION` ASC) VISIBLE,
  UNIQUE INDEX `_UNIQUE` (`ID_DECEISION` ASC) VISIBLE,
  CONSTRAINT `FK_DECISION_GAME1`
    FOREIGN KEY (`FK_GAME_ID_GAME` , `FK_GAME_USER_ID_USER` , `FK_GAME_ADVENTURE_ID_ADVENTURE` , `FK_GAME_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`GAME` (`ID_GAME` , `FK_USER_ID_USER` , `FK_ADVENTURE_ID_ADVENTURE` , `FK_CHARACTER_ID_CHARACTER`),
  CONSTRAINT `FK_DECISION_OPTION1`
    FOREIGN KEY (`FK_OPTION_ID_OPTION`)
    REFERENCES `AMS`.`OPTION` (`ID_OPTION`));



CREATE TABLE IF NOT EXISTS `AMS`.`USER_HAS_CHARACTER` (
  `FK_USER_ID_USER` INT NOT NULL AUTO_INCREMENT,
  `FK_CHARACTER_ID_CHARACTER` INT NOT NULL,
  PRIMARY KEY (`FK_USER_ID_USER`, `FK_CHARACTER_ID_CHARACTER`),
  INDEX `fk_USER_has_CHARACTER_CHARACTER1_idx` (`FK_CHARACTER_ID_CHARACTER` ASC) VISIBLE,
  INDEX `fk_USER_has_CHARACTER_USER_idx` (`FK_USER_ID_USER` ASC) VISIBLE,
  CONSTRAINT `fk_USER_has_CHARACTER_CHARACTER1`
    FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`),
  CONSTRAINT `fk_USER_has_CHARACTER_USER`
    FOREIGN KEY (`FK_USER_ID_USER`)
    REFERENCES `AMS`.`USER` (`ID_USER`));
