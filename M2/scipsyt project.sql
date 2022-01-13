create database if not exists AMS;
use AMS;

CREATE TABLE IF NOT EXISTS `AMS`.`USER` (
  `id_user` INT NOT NULL auto_increment,
  `user_name` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `user_name_unique` (`user_name` ASC) VISIBLE);
  
  CREATE TABLE IF NOT EXISTS `AMS`.`CHARACTER` (
  `id_character` INT NOT NULL,
  `character_name` VARCHAR(45) NULL,
  `description` VARCHAR(100) NULL,
  PRIMARY KEY (`id_character`),
  UNIQUE INDEX `character_name_UNIQUE` (`character_name` ASC) VISIBLE);
  
  CREATE TABLE IF NOT EXISTS `AMS`.`ADVENTURE` (
  `id_adventure` INT NOT NULL auto_increment,
  `adventure_name` VARCHAR(45) NULL,
  `description` VARCHAR(1000) NULL,
  PRIMARY KEY (`id_adventure`));
  
  CREATE TABLE IF NOT EXISTS `AMS`.`STEP` (
  `id_step` INT NOT NULL,
  `step_description` VARCHAR(45) NULL,
  `end` bit NULL,
  `adventure_id_adventure` INT NOT NULL,
  PRIMARY KEY (`id_step`, `adventure_id_adventure`),
  INDEX `fk_STEP_ADVENTURE_idx` (`adventure_id_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_STEP_ADVENTURE`
    FOREIGN KEY (`adventure_id_adventure`)
    REFERENCES `AMS`.`ADVENTURE` (`id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`OPTION` (
  `id_option` INT NOT NULL,
  `option_description` VARCHAR(500) NULL,
  `answer` VARCHAR(45) NULL,
  `go` VARCHAR(45) NULL,
  `comes` VARCHAR(45) NULL,
  `step_id_step` INT NOT NULL,
  PRIMARY KEY (`id_option`),
  INDEX `fk_OPTION_STEP_idx` (`step_id_step` ASC) VISIBLE,
  CONSTRAINT `fk_OPTION_STEP`
    FOREIGN KEY (`step_id_step`)
    REFERENCES `AMS`.`STEP` (`id_step`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`GAME` (
  `id_game` INT NOT NULL,
  `current_date` datetime NULL,
  `user_id_user` INT NOT NULL,
  `adventure_id_adventure` INT NOT NULL,
  `character_id_character` INT NOT NULL,
  PRIMARY KEY (`id_game`, `user_id_user`, `adventure_id_adventure`, `character_id_character`),
  INDEX `fk_GAME_USER_idx` (`user_id_user` ASC) VISIBLE,
  INDEX `fk_GAME_ADVENTURE_idx` (`adventure_id_adventure` ASC) VISIBLE,
  INDEX `fk_GAME_CHARACTER_idx` (`character_id_character` ASC) VISIBLE,
  CONSTRAINT `fk_GAME_USER`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `AMS`.`USER` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_GAME_ADVENTURE`
    FOREIGN KEY (`adventure_id_adventure`)
    REFERENCES `AMS`.`ADVENTURE` (`id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_GAME_CHARACTER`
    FOREIGN KEY (`character_id_character`)
    REFERENCES `AMS`.`CHARACTER` (`id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`USER_has_CHARACTER` (
  `user_id_user` INT NOT NULL,
  `character_id_character` INT NOT NULL,
  PRIMARY KEY (`user_id_user`, `character_id_character`),
  INDEX `fk_USER_has_CHARACTER_CHARACTER1_idx` (`character_id_character` ASC) VISIBLE,
  INDEX `fk_USER_has_CHARACTER_USER_idx` (`user_id_user` ASC) VISIBLE,
  CONSTRAINT `fk_USER_has_CHARACTER_USER`
    FOREIGN KEY (`user_id_user`)
    REFERENCES `AMS`.`USER` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_USER_has_CHARACTER_CHARACTER1`
    FOREIGN KEY (`character_id_character`)
    REFERENCES `AMS`.`CHARACTER` (`id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`CHARACTER_has_ADVENTURE` (
  `character_id_character` INT NOT NULL,
  `adventure_id_adventure` INT NOT NULL,
  PRIMARY KEY (`character_id_character`, `adventure_id_adventure`),
  INDEX `fk_CHARACTER_has_ADVENTURE_ADVENTURE1_idx` (`adventure_id_adventure` ASC) VISIBLE,
  INDEX `fk_CHARACTER_has_ADVENTURE_CHARACTER1_idx` (`character_id_character` ASC) VISIBLE,
  CONSTRAINT `fk_CHARACTER_has_ADVENTURE_CHARACTER1`
    FOREIGN KEY (`character_id_character`)
    REFERENCES `AMS`.`CHARACTER` (`id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CHARACTER_has_ADVENTURE_ADVENTURE1`
    FOREIGN KEY (`adventure_id_adventure`)
    REFERENCES `AMS`.`ADVENTURE` (`id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`DECISION` (
  `id_decision` INT NOT NULL,
  `game_id_game` INT NOT NULL,
  `game_user_id_user` INT NOT NULL,
  `game_adventure_id_adventure` INT NOT NULL,
  `game_character_id_character` INT NOT NULL,
  `option_id_option` INT NOT NULL,
  PRIMARY KEY (`id_decision`, `game_id_game`, `game_user_id_user`, `game_adventure_id_adventure`, `game_character_id_character`, `option_id_option`),
  INDEX `fk_DECISION_GAME1_idx` (`game_id_game` ASC, `game_user_id_user` ASC, `game_adventure_id_adventure` ASC, `game_character_id_character` ASC) VISIBLE,
  INDEX `fk_DECISION_OPTION1_idx` (`option_id_option` ASC) VISIBLE,
  CONSTRAINT `fk_DECISION_GAME1`
    FOREIGN KEY (`game_id_game` , `game_user_id_user` , `game_adventure_id_adventure` , `game_character_id_character`)
    REFERENCES `AMS`.`GAME` (`id_game` , `user_id_user` , `adventure_id_adventure` , `character_id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DECISION_OPTION1`
    FOREIGN KEY (`option_id_option`)
    REFERENCES `AMS`.`OPTION` (`id_option`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `AMS`.`ANSWER` (
  `id_answer` INT NOT NULL,
  `step_id_step` INT NOT NULL,
  `step_adventure_id_adventure` INT NOT NULL,
  PRIMARY KEY (`id_answer`, `step_id_step`, `step_adventure_id_adventure`),
  INDEX `fk_ANSWER_STEP1_idx` (`step_id_step` ASC, `step_adventure_id_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_ANSWER_STEP1`
    FOREIGN KEY (`step_id_step` , `step_adventure_id_adventure`)
    REFERENCES `AMS`.`STEP` (`id_step` , `adventure_id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
  
  