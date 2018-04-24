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
insert into image values ("boat.png", "boat");
insert into image values ("books.png", "books");
insert into image values ("boots.png", "boots");
insert into image values ("brain.png", "bridge");
insert into image values ("bread.png", "bread");
insert into image values ("bridge.png", "bridge");
insert into image values ("broom.png", "broom");
insert into image values ("brush.png", "brush");
insert into image values ("bucket.png", "bucket");
insert into image values ("buttons.png", "buttons");
insert into image values ("cake.png", "cake");
insert into image values ("camel.png", "camel");
insert into image values ("camera.png", "camera");
insert into image values ("cardboardbox.png", "cardboardbox");
insert into image values ("carriage.png", "carriage");
insert into image values ("cart.png", "cart");
insert into image values ("cat.png", "cat");
insert into image values ("cheese.png", "cheese");
insert into image values ("chicken.png", "chicken");
insert into image values ("cherries.png", "cherries");
insert into image values ("clock.png", "clock");
insert into image values ("coffee.png", "coffee");
insert into image values ("comb.png", "comb");
insert into image values ("cow.png", "cow");
insert into image values ("crocodile.png", "crocodile");
insert into image values ("desk.png", "desk");
insert into image values ("deer.png", "deer");
insert into image values ("diamond.png", "diamond");
insert into image values ("dog.png", "dog");
insert into image values ("donkey.png", "donkey");
insert into image values ("door.png", "door");
insert into image values ("drawer.png", "drawer");
insert into image values ("dress.png", "dress");
insert into image values ("ear.png", "ear");
insert into image values ("egg.png", "egg");
insert into image values ("eye.png", "eye");
insert into image values ("feather.png", "feather");
insert into image values ("fish.png", "fish");
insert into image values ("flag.png", "flag");
insert into image values ("fly.png", "fly");
insert into image values ("foot.png", "foot");
insert into image values ("fork.png", "fork");
insert into image values ("fruits.png", "fruits");
insert into image values ("geese.png", "geese");
insert into image values ("giraffe.png", "giraffe");
insert into image values ("glove.png", "glove");
insert into image values ("gnome.png", "gnome");
insert into image values ("hammer.png", "hammer");
insert into image values ("hanger.png", "hanger");
insert into image values ("hare.png", "hare");
insert into image values ("hats.png", "hats");
insert into image values ("heart.png", "heart");
insert into image values ("horn.png", "horn");
insert into image values ("house.png", "house");
insert into image values ("horse.png", "horse");
insert into image values ("kettle.png", "kettle");
insert into image values ("key.png", "key");
insert into image values ("leaf.png", "leaf");
insert into image values ("lemon.png", "lemon");
insert into image values ("lightbulb.png", "lightbulb");
insert into image values ("map.png", "map");
insert into image values ("match.png", "match");
insert into image values ("mice.png", "mice");
insert into image values ("microwave.png", "microwave");
insert into image values ("monkey.png", "monkey");
insert into image values ("moon.png", "moon");
insert into image values ("mouse.png", "mouse");
insert into image values ("nail.png", "nail");
insert into image values ("needle.png", "needle");
insert into image values ("onion.png", "onion");
insert into image values ("orange.png", "orange");
insert into image values ("owl.png", "owl");
insert into image values ("pan.png", "pan");
insert into image values ("pants.png", "pants");
insert into image values ("pea.png", "pea");
insert into image values ("peacock.png", "peacock");
insert into image values ("pear.png", "pear");
insert into image values ("pen.png", "pen");
insert into image values ("pencil.png", "pencil");
insert into image values ("pig.png", "pig");
insert into image values ("pin.png", "pin");
insert into image values ("plane.png", "plane");
insert into image values ("potato.png", "potato");
insert into image values ("pots.png", "pots");
insert into image values ("rainboots.png", "rainboots");
insert into image values ("rhino.png", "rhino");
insert into image values ("rocket.png", "rocket");
insert into image values ("rooster.png", "rooster");
insert into image values ("rope.png", "rope");
insert into image values ("scarf.png", "scarf");
insert into image values ("schoolbus.png", "schoolbus");
insert into image values ("scissors.png", "scissors");
insert into image values ("scooter.png", "scooter");
insert into image values ("screw.png", "screw");
insert into image values ("seagull.png", "seagull");
insert into image values ("sheep.png", "sheep");
insert into image values ("ship.png", "ship");
insert into image values ("shirt.png", "shirt");
insert into image values ("sled.png", "sled");
insert into image values ("snail.png", "snail");
insert into image values ("snake.png", "snake");
insert into image values ("sneakers.png", "sneakers");
insert into image values ("sofa.png", "sofa");
insert into image values ("spider.png", "spider");
insert into image values ("sponge.png", "sponge");
insert into image values ("squirrel.png", "squirrel");
insert into image values ("stamp.png", "stamp");
insert into image values ("star.png", "star");
insert into image values ("stoplight.png", "stoplight");
insert into image values ("store.png", "store");
insert into image values ("strawberry.png", "strawberry");
insert into image values ("street.png", "street");
insert into image values ("suitcase.png", "suitcase");
insert into image values ("sun.png", "sun");
insert into image values ("swan.png", "swan");
insert into image values ("swing.png", "swing");
insert into image values ("table.png", "table");
insert into image values ("thumb.png", "thumb");
insert into image values ("ticket.png", "ticket");
insert into image values ("tiger.png", "tiger");
insert into image values ("tomato.png", "tomato");
insert into image values ("tooth.png", "tooth");
insert into image values ("train.png", "train");
insert into image values ("tree.png", "tree");
insert into image values ("trumpet.png", "trumpet");
insert into image values ("ufo.png", "ufo");
insert into image values ("umbrella.png", "umbrella");
insert into image values ("whale.png", "whale");
insert into image values ("wolve.png", "wolve");
insert into image values ("yarn.png", "yarn");
insert into image values ("zebra.png", "zebra");

insert into user values ("Megane", "1234", "mganemichaud@yahoo.fr");

