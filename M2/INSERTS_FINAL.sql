# ************************************************************************
#-------------------------- INSERTS ADVENTURE ----------------------------
# ************************************************************************

insert ignore into AMS.ADVENTURE(ID_ADVENTURE,adventure_name,description) value(10,'El misteri de la casa encantada','La historia tracta d’un personatge que es fica en una casa abandonada, li han dit que aquesta casa esta encantada, veurem com es resol la aventura');
insert ignore into AMS.ADVENTURE(ID_ADVENTURE, adventure_name,description) value(11, 'Un dia qualsevol','El personatge comença un nou dia de escola y tu escolliràs el seu camí al mateix, anirà o no anirà?');
insert ignore into AMS.ADVENTURE(ID_ADVENTURE, adventure_name,description) value(12, 'Dia perillós','Historia terrorífica que podrà passar el nostre personatge, un assassí escapat y uns pares desapareguts y tu amb el teu germà petit en mitat de no res. Que passarà?');

# ************************************************************************
#-------------------------- INSERTS CHARACTERS ----------------------------
# ************************************************************************

insert ignore into AMS.CHARACTER (character_name, description) values ("Jayce", "Ingenier de Hextech");
insert ignore into AMS.CHARACTER (character_name, description) values ("Gazel", "Famós lladre de guant blanc");
insert ignore into AMS.CHARACTER (character_name, description) values ("Silco", "Ingenier de Hextech");
insert ignore into AMS.CHARACTER (character_name, description) values ("Bäarg", "Mag inepte i lladre de encanteris");


# ************************************************************************
#---------------------- INSERTS CHARACTER_ADVENTURE ----------------------
# ************************************************************************

INSERT ignore INTO AMS.CHARACTER_HAS_ADVENTURE	(FK_CHARACTER_ID_CHARACTER, FK_ADVENTURE_ID_ADVENTURE) values (1,10);
INSERT ignore INTO AMS.CHARACTER_HAS_ADVENTURE	(FK_CHARACTER_ID_CHARACTER, FK_ADVENTURE_ID_ADVENTURE) values (2,10);
INSERT ignore INTO AMS.CHARACTER_HAS_ADVENTURE	(FK_CHARACTER_ID_CHARACTER, FK_ADVENTURE_ID_ADVENTURE) values (3,11);
INSERT ignore INTO AMS.CHARACTER_HAS_ADVENTURE	(FK_CHARACTER_ID_CHARACTER, FK_ADVENTURE_ID_ADVENTURE) values (4,12);



# ************************************************************************
#----------------------------- INSERTS STEP ------------------------------
# ************************************************************************

# Historia 1

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(101,'Torna a ser estiu, temps de vacances. Vas a casa del teu oncle. Et porta a fer un recorregut per la ciutat. Hi ha molts edificis antics, però el més antic de tots es troba al carrer Major. Diu que està embruixat, però no se ho creu',0,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(102,'Comenceu a pujar els graons de pedra de la antiga casa embruixada. Obriu la porta i entres i, de sobte, una fletxa afilada se enfila davant teu!',0,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(103,'Tu et quedes allà. Aleshores decideixes anar a casa, prendre un gelat i anar al llit.',1,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(104,'Puges les escales. Et recolzes a la barana i es trenca. Caus i això és el teu final.',1,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(105,'Passeu per les portes batents. Camines per la habitació',1,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(106,'Vas al armari. Caus per una trampa i et trenques la cama. Les parets són massa llises per pujar. No hi ha una altra manera de pujar.',1,10);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(107,'Entres a un passadís sota la casa. Vas fent camí i et porta a una trampa que et porta de tornada al lloc on vas començar. Trobeu un policia al cim i et diu: "Vas tenir sort de sortir de allà. No hi tornis a entrar mai més!" Vas a casa i prens un gelat.

',1,10);

# Historia 2

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(111,'Finalitza estiu, tornes a l’institut. Aquell mati et despertes  per començar en un nou institut.  Tens por de començar en  un nou institut i t’estàs plantejant si:',0,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(112,'Has decidit agafar la motxilla i marxar cap a l’institut.
De camí a l’institut et trobes amb un accident del qual tu no estàs involucrat, tens l’opció d’ajudar o deixar-ho passar:
',0,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(113,'Decideixes quedar-te en casa, a la tarda els teus pares et foten la bronca i aquí finalitza la teva historia.',1,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(114,'Decideixes ajudar i et demores molta estona en l’accident, quan acabes d’ajudar marxes a l’institut però es massa tard i has perdut tota la presentació i encara que expliques la situació et foten la bronca. Aquí finalitza la teva historia.',1,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(115,'Penses que ja haurà suficient gent per ajudar i marxes a l’institut perquè arribes tard.
Arribes a l’institut, entres, vas a la sala d’actes i et seus sol en una cantonada. 
Un noi s’apropa a tu i es presenta molt educadament, et demana el numero per estar en contacte i tenir un nou possible amic, se’l dones?
',0,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(116,'Li dones el teu telèfon mòbil  i a conseqüència de tenir moltes coses en comú  sereu bons amics durant el curs. Aquí finalitza la teva historia.',1,11);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(117,'No li dones el teu numero de telèfon perquè ets molt desconfiat, aquest noi s’ho pren malament i durant tot el curs no parlareu. Aquí finalitza la teva historia',1,11);

# Historia 3

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(121,'Una família, composta per dos nens del qual tu ets un dels nens i els seus pares, viatjaven per carretera cap a la platja  quan el cotxe es va avariar. Els pares van sortir a buscar ajuda i, perquè els nens no s’avorrissin, els van deixar amb la ràdio encesa. Va caure la nit i els pares seguien sense tornar quan van sentir una inquietant notícia a la ràdio: un assassí molt perillós havia escapat de un centre penitenciari proper a la seva localització i demanaven que extremessin les precaucions. 
Tu ets el major, penses l’opció de anar a buscar els teus pares però després de escoltar la noticia aniràs o no
',0,12);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(122,'Surt del cotxe i li demanes al teu germà que no surti del cotxe que pot ser molt perillós.
Comences a caminar i entres en un bosc, de sobtes escoltes un soroll i et dones la volta, et sorprèn un home. Comences ha córrer per poder amagar-te tens dos opcions:
',0,12);
insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(123,'Decideixes no sortir perquè pot ser perillós al cap d’una estona apareixen els teus pares amb ajuda i aconseguiu marxar a casa. Finalitza la teva historia',1,12);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(124,'Veus una casa abandonada i intentes amagar-te dintre e intentar que l’home no et trobi.
Sembla que l’home no et segueix esperes una estona i surts corrent en direcció al cotxe on es troba el teu germà i en poca estona apareixen els teus pares i marxeu cap a casa. Aquí finalitza la teva historia.
',1,12);

insert ignore into AMS.STEP(ID_STEP,step_description,end,FK_ADVENTURE_ID_ADVENTURE) value(125,'Continues corrent, et trobes amb una benzinera, trobes que hi ha un cadàver a terra del que sembla el noi de la benzinera. De sobte apareix l’assassí. Aqui finalitza la teva historia.',1,12);


# ************************************************************************
#--------------------------- INSERTS OPTION ------------------------------
# ************************************************************************

# HISTORIA 1

insert  ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(101,'Entres dins?',102,102,101,10);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(102,'Et quesdes alla?',103,103,101,10);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(103,'Puges la escala?',104,104,102,10);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(104,'Passes per les portes batents?',105,105,102,10);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(105,'Entres al armari?',106,106,105,10);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(106,'Entres a un passadís sota la casa',107,107,105,10);

# HISTORIA 2

insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(111,'Anar?',112,112,111,11);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(112,'No anar',113,113,111,11);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(113,'Ajudar',114,114,112,11);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(114,'No ajudar',115,115,112,11);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(115,'Donar',116,116,115,11);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(116,'No donar',117,117,115,11);


# HISTORIA 3

insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(121,'Anar',121,122,121,12);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(122,'No anar',123,123,121,12);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(123,'Una casa abandonada',124,124,122,12);
insert ignore into AMS.OPTION(ID_OPTION,option_description,answer,go_step,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) value(124,'Continuar corrent ',125,125,122,12);

# ************************************************************************
#---------------------------- INSERTS GAME -------------------------------
# ************************************************************************

insert ignore into AMS.GAME(FK_USER_ID_USER, FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) VALUES (1, 10,1);
insert ignore into GAME (FK_USER_ID_USER, FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) VALUES (1, 10,2);
insert ignore into GAME (FK_USER_ID_USER, FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) VALUES (2, 11,3);
insert ignore into GAME (FK_USER_ID_USER, FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) VALUES (2, 10,1);
insert ignore into GAME (FK_USER_ID_USER, FK_ADVENTURE_ID_ADVENTURE, FK_CHARACTER_ID_CHARACTER) VALUES (2, 12,4);


# ************************************************************************
#---------------------------- INSERTS USER -------------------------------
# ************************************************************************

insert ignore into USER (user_name,password) VALUES ("Admin", "mypass");
insert ignore into USER (user_name,password) VALUES ("Isma", "mypass123");

