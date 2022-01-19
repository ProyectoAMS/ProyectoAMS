insert into `character`(character_name, description) value("osiris", "el destructor");

insert into user(user_name, password) value("paco", "123");

insert into game(FK_USER_ID_USER ,FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) value (1, 10, 1);
insert into game(FK_USER_ID_USER ,FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) value (1, 12, 1);
insert into 
decision(FK_GAME_ID_GAME, FK_GAME_USER_ID_USER, FK_GAME_ADVENTURE_ID_ADVENTURE, FK_GAME_CHARACTER_ID_CHARACTER, FK_OPTION_ID_OPTION)
value (1, 1, 10, 1, 102);

#ID_GAME==1
insert into 
decision(FK_GAME_ID_GAME, FK_GAME_USER_ID_USER, FK_GAME_ADVENTURE_ID_ADVENTURE, FK_GAME_CHARACTER_ID_CHARACTER, FK_OPTION_ID_OPTION)
value (1, 1, 10, 1, 102);
#ID_GAME==2 opc1
insert into 
decision(FK_GAME_ID_GAME, FK_GAME_USER_ID_USER, FK_GAME_ADVENTURE_ID_ADVENTURE, FK_GAME_CHARACTER_ID_CHARACTER, FK_OPTION_ID_OPTION)
value (2, 1, 12, 1, 121);

#ID_GAME==2 opc3
insert into 
decision(FK_GAME_ID_GAME, FK_GAME_USER_ID_USER, FK_GAME_ADVENTURE_ID_ADVENTURE, FK_GAME_CHARACTER_ID_CHARACTER, FK_OPTION_ID_OPTION)
value (2, 1, 12, 1, 124);

/*
select * from game;
select * from adventure;
select * from step;
SELECT * FROM user;
select * from decision;

select step_description from ams.step where ID_STEP=(select FK_STEP_ID_STEP from ams.option where ID_OPTION=(select FK_OPTION_ID_OPTION from ams.decision where FK_GAME_ID_GAME=1))



select a.adventure_name ,id_adventure from adventure a where a.id_adventure=(select g.id_game from game g where a.id_adventure=FK_ADVENTURE_ID_ADVENTURE);
select adventure_name from adventure where id_adventure=(select FK_ADVENTURE_ID_ADVENTURE from game where ID_GAME=2);
select description from adventure where id_adventure=(select FK_ADVENTURE_ID_ADVENTURE from game where ID_GAME=2);
select step_description from step where id_step=(select FK_STEP_ID_STEP from option);







#select step_description from step where id_step=(select FK_STEP_ID_STEP from ams.option where FK_STEP_ID_STEP=101);
SELECT * FROM ams.step;
SELECT * FROM ams.option;
SELECT * FROM ams.game;
SELECT * FROM ams.decision;



select step_description from ams.step 
where ID_STEP=(select FK_STEP_ID_STEP from ams.option 
where ID_OPTION=(select FK_OPTION_ID_OPTION from ams.decision where FK_GAME_ID_GAME=1));
*/