use birds;
CREATE TABLE bird_appearance(
breed varchar(25) not null,
length decimal(3,2),
colour varchar(10),
primary key(breed),
unique(breed)
);

insert into bird_appearance (breed, length, colour)
values ("Northern Pintail", "0.64", "Brown"),
("Red-backed Shrike", "0.17", "Brown"),
("Azores Gull", "0.58", "Grey"),
("Western Cattle Egret", "0.48", "White"),
("Little Bustard", "0.44", "Brown"),
("Barn Owl", "0.36", "Brown"),
("Siberian Chiffchaff", "0.11", "White");

SELECT bird_details.breed, bird_appearance.breed
FROM bird_details
INNER JOIN bird_appearance
ON bird_details.breed = bird_appearance.breed;

SELECT * FROM bird_details, bird_appearance;

SELECT * FROM bird_details, bird_appearance
WHERE bird_appearance.colour = "White";

SELECT * FROM bird_details, bird_appearance
WHERE bird_appearance.colour="Brown" AND bird_details.wingspan < "1.20";

SELECT * FROM bird_appearance
WHERE length between 0.30 and 0.50;