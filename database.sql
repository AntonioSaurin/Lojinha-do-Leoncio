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

insert into `itens` (`description`, `value`, `role`) values('Eclipse','2800','Assassin');
insert into `itens` (`description`, `value`, `role`) values('Armadura de Warmog','3100','Tank');
insert into `itens` (`description`, `value`, `role`) values('Cutelo Negro','3000','Bruiser');
insert into `itens` (`description`, `value`, `role`) values('Força Do Vendaval','3400','ADCarry');
insert into `itens` (`description`, `value`, `role`) values('Companheiro de Luden','2900','Mage');
insert into `itens` (`description`, `value`, `role`) values('Cajado Aquafluxo','2300','Support');
