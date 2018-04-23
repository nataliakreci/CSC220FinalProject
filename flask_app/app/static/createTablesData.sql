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

insert into image values ("acorn.png", "acorn");
insert into image values ("ant.png", "ant");
insert into image values ("apple.png", "apple");
insert into image values ("arm.png", "arm");
insert into image values ("backpack.png", "backpack");
insert into image values ("banana.png", "banana");
insert into image values ("basket.png", "basket");
insert into image values ("bathtub.png", "bathtub");
insert into image values ("bed.png", "bed");
insert into image values ("bee.png", "bee");
insert into image values ("bird.png", "bird");
insert into image values ("acorn.png", "acorn");
insert into image values ("boat.png", "boat");
insert into image values ("books.png", "boots");
insert into image values ("brain.png", "bridge");
insert into image values ("brush.png", "brush");
insert into image values ("bucket.png", "bucket");
insert into image values ("buttons.png", "buttons");
insert into image values ("cake.png", "cake");
insert into image values ("camera.png", "camera");
insert into image values ("cardboardbox.png", "cardboardbox");
insert into image values ("carriage.png", "carriage");
insert into image values ("suitcase.png", "suitcase");
insert into image values ("cart.png", "cart");
insert into image values ("cat.png", "cat");
insert into image values ("cheese.png", "cheese");
insert into image values ("chicken.png", "chicken");
insert into image values ("clock.png", "clock");
insert into image values ("coffee.png", "coffee");
insert into image values ("comb.png", "comb");
insert into image values ("cow.png", "cow");
insert into image values ("desk.png", "desk");
insert into image values ("deer.png", "deer");
insert into image values ("diamond.png", "diamond");
insert into image values ("dog.png", "dog");
insert into image values ("door.png", "door");
insert into image values ("drawer.png", "drawer");
insert into image values ("dress.png", "dress");
insert into image values ("ear.png", "ear");
insert into image values ("egg.png", "egg");
insert into image values ("eye.png", "eye");
insert into image values ("feather.png", "feather");
insert into image values ("fish.png", "fish");
insert into image values ("flag.png", "flag");
insert into image values ("foot.png", "foot");
insert into image values ("fork.png", "fork");
insert into image values ("fruits.png", "fruits");
insert into image values ("geese.png", "geese");
insert into image values ("glove.png", "glove");
insert into image values ("gnome.png", "gnome");
insert into image values ("hammer.png", "hammer");
insert into image values ("hanger.png", "hanger");
insert into image values ("hats.png", "hats");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");
insert into image values ("acorn.png", "acorn");



insert into user values ("Megane", "1234", "mganemichaud@yahoo.fr");

insert into user_known_images values ("00:00:05", "Megane", "apple.img");

insert into user_tried_images values ("Megane", "tree.img");

