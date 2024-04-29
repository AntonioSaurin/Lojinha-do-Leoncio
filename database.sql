create database leoncioStore 
default char set utf8mb4 
default collate utf8mb4_general_ci;

use leoncioStore;

create table `itens`(
`id` int auto_increment,
`description` varchar(50),
`value` int,
`role` enum('Bruiser','Mage','Tank','Support','ADCarry','Assassin'),
primary key(id)
);

create table `users`(
`id` int auto_increment,
`username` varchar(20) unique,
`password` varchar(255),
`function` enum('Admin', 'Buyer'),
primary key(id)
);

insert into `users` (`username`, `password`) values ('Leoncio', 'Admin');

select * from itens;