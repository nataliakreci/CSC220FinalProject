delete from image;
delete from user;
delete from user_known_images;
delete from user_tried_images;

drop Table image;
drop Table user;
drop Table user_known_images;
drop Table user_tried_images;

CREATE TABLE IF NOT EXISTS image (
 image text NOT NULL PRIMARY KEY,
 word text NOT NULL
);
 
CREATE TABLE IF NOT EXISTS user (
 username text NOT NULL PRIMARY KEY,
 password text NOT NULL,
 emailaddress text
);

CREATE TABLE IF NOT EXISTS user_known_images (
 record text NOT NULL,
 username text NOT NULL,
 image text NOT NULL,
 FOREIGN KEY(username) REFERENCES user(username),
 FOREIGN KEY(image) REFERENCES image(image),
 PRIMARY KEY (username, image)
);

CREATE TABLE IF NOT EXISTS user_tried_images (
 username text NOT NULL,
 image text NOT NULL,
 FOREIGN KEY(username) REFERENCES user(username),
 FOREIGN KEY(image) REFERENCES image(image),
 PRIMARY KEY (username, image)
);

insert into image values ("apple.jpg", "apple");
insert into image values ("tree.jpg", "tree");
insert into image values ("sun.jpg", "sun");
insert into image values ("flower.jpg", "flower");

insert into user values ("Megane", "1234", "mganemichaud@yahoo.fr");

