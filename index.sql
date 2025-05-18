USE ProgramingHero;

CREATE TABLE Student(
	Roll CHAR(4) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(60) UNIQUE,
    Address VARCHAR(250),
    Age INT CHECK(Age>10)
);

INSERT INTO Student(Roll,Name,Email,Address,Age) VALUES('0003','Shovon','shovon@gmail.com','Badda',1);

CREATE TABLE Student(
	Roll CHAR(4),
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(60),
    Address VARCHAR(250),
    Age INT,
    PRIMARY KEY(Roll),
    UNIQUE(Email),
    CHECK(Age>10)
);

CREATE TABLE Student(
	Roll CHAR(4),
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(60),
    Address VARCHAR(250),
    Age INT,
    Constraint pk_rlule PRIMARY KEY(Roll),
    Constraint unique_rule UNIQUE(Email),
    Constraint checking_rule CHECK(Age>10)
);

CREATE TABLE Library(
	BookName VARCHAR(50) PRIMARY KEY,
    WhoHired_Roll CHAR(4),
    FOREIGN KEY(WhoHired_Roll) REFERENCES Student(Roll),
);

CREATE TABLE Course(
    CourseName VARCHAR(10),
    University VARCHAR(10),
    Credit INT,

    PRIMARY KEY(CourseName,University);
);