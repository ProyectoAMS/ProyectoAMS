ALTER TABLE CHARACTER_HAS_ADVENTURE
ADD CONSTRAINT `FK_CHARACTER_has_ADVENTURE_ADVENTURE1`
	FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
	REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`),
ADD CONSTRAINT `FK_CHARACTER_has_ADVENTURE_CHARACTER1`
	FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
	REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`);


ALTER TABLE GAME
ADD CONSTRAINT `FK_GAME_ADVENTURE`
	FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
	REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`),
ADD CONSTRAINT `FK_GAME_CHARACTER`
	FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
	REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`),
ADD CONSTRAINT `FK_GAME_USER`
	FOREIGN KEY (`FK_USER_ID_USER`)
	REFERENCES `AMS`.`USER` (`ID_USER`);


ALTER TABLE STEP
ADD CONSTRAINT `FK_STEP_ADVENTURE`
    FOREIGN KEY (`FK_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`ADVENTURE` (`ID_ADVENTURE`);


ALTER TABLE ams.OPTION
ADD CONSTRAINT `FK_OPTION_STEP`
    FOREIGN KEY (`FK_STEP_ID_STEP` , `FK_STEP_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`STEP` (`ID_STEP` , `FK_ADVENTURE_ID_ADVENTURE`);

ALTER TABLE DECISION
ADD CONSTRAINT `FK_DECISION_GAME1`
    FOREIGN KEY (`FK_GAME_ID_GAME` , `FK_GAME_USER_ID_USER` , `FK_GAME_ADVENTURE_ID_ADVENTURE` , `FK_GAME_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`GAME` (`ID_GAME` , `FK_USER_ID_USER` , `FK_ADVENTURE_ID_ADVENTURE` , `FK_CHARACTER_ID_CHARACTER`),
  ADD CONSTRAINT `FK_DECISION_OPTION1`
    FOREIGN KEY (`FK_OPTION_ID_OPTION` , `FK_STEP_ID_STEP` , `FK_STEP_ADVENTURE_ID_ADVENTURE`)
    REFERENCES `AMS`.`OPTION` (`ID_OPTION` , `FK_STEP_ID_STEP` , `FK_STEP_ADVENTURE_ID_ADVENTURE`);

ALTER TABLE USER_HAS_CHARACTER
ADD CONSTRAINT `fk_USER_has_CHARACTER_CHARACTER1`
    FOREIGN KEY (`FK_CHARACTER_ID_CHARACTER`)
    REFERENCES `AMS`.`CHARACTER` (`ID_CHARACTER`),
  ADD CONSTRAINT `fk_USER_has_CHARACTER_USER`
    FOREIGN KEY (`FK_USER_ID_USER`)
    REFERENCES `AMS`.`USER` (`ID_USER`);