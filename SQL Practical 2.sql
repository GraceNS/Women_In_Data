use birds;

insert into bird_details (breed, wingspan, life_expect, vore, last_spotted)
values ("Swallow-tailed Kite", "1.24", "6", "Carnivore", "21-03-25"),
("Little Bustard", "0.98", "10", "Omnivore", "21-03-23"),
("Common Crane", "2.24", "13", "Insectivore", "21-03-09"),
("Rough-legged Buzzard", "1.35", "18", "Carnivore", "21-03-02"),
("Siberian Chiffchaff", "0.18", "5", "Insectivore", "21-01-01");

explain bird_details;
select * from bird_details;

UPDATE bird_details
SET last_spotted = "21-01-15"
WHERE breed = "Red-backed Shrike";

DELETE FROM bird_details
WHERE breed = "Rough-legged Buzzard";

SELECT wingspan from bird_details;

SELECT wingspan, vore, life_expect FROM bird_details;

SELECT * FROM bird_details ORDER BY last_spotted;