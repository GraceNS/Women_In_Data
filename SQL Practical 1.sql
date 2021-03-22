create database birds;

use birds;
CREATE TABLE bird_details (
breed varchar (25) not null,
wingspan decimal (3,2) not null,
life_expect int not null,
vore enum ('Herbivore', 'Carnivore', 'Omnivore', 'Insectivore'),
last_spotted date,
primary key (breed)
);

insert into bird_details (breed, wingspan, life_expect, vore, last_spotted)
values ("White-tailed Eagle", "2.12", "21", "Omnivore", "21-01-28"),
("Azores Gull", "0.60", "20", "Omnivore", "20-12-10"),
("Western Cattle Egret", "0.48", "10", "Insectivore", "20-10-30"),
("Red-backed Shrike", "0.26", "4", "Omnivore", "20-09-15"),
("European Honey Buzzard", "1.42", "12", "Insectivore", "20-09-14");

explain bird_details;