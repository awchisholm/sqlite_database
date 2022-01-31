BEGIN TRANSACTION;
DROP TABLE IF EXISTS "student";
CREATE TABLE IF NOT EXISTS "student" (
	"StudentID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"FirstName"	TEXT,
	"Surname"	TEXT,
	"TutorID"	INTEGER,
	FOREIGN KEY("TutorID") REFERENCES "tutor"("TutorID")
);
DROP TABLE IF EXISTS "tutor";
CREATE TABLE IF NOT EXISTS "tutor" (
	"TutorID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"FirstName"	TEXT,
	"Surname"	TEXT
);
INSERT INTO "student" ("StudentID","FirstName","Surname","TutorID") VALUES (1,'Crystal','Chan',1),
 (2,'Josh','Tice',1),
 (3,'Tejay','Ford',1),
 (4,'Joe','Harper',3);
INSERT INTO "tutor" ("TutorID","FirstName","Surname") VALUES (1,'Steve','Woods'),
 (2,'Andrew','Chisholm'),
 (3,'Nicolette','Dryden');
COMMIT;
