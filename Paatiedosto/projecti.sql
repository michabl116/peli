create database airportgame1;
use airportgame1;


create table player_information(
ID int not null auto_increment,
first_name varchar(40),
last_name varchar(40),
ident varchar(40),
age int (11),
primary key (ID)
);

create table player_goal(
ID int not null auto_increment,
first_name varchar(40),
player_level varchar (40),
continet varchar (40),
ident varchar (40),
player_points int (50),
player_fuel int ( 11),
primary key (ID)
);

create table gola_reached(
player_information_ID int,
player_goal_ID int,
primary key (player_information_ID,player_goal_ID),
foreign key (player_information_ID) references player_information(ID),
foreign key (player_goal_ID) references player_goal(ID)
 
);

