delete from image;
delete from user_known_images;
delete from user_tried_images;

drop Table image;
drop Table user_known_images;
drop Table user_tried_images;

CREATE TABLE IF NOT EXISTS image (
 image text NOT NULL PRIMARY KEY,
 word text NOT NULL,
 num int NOT NULL
);

CREATE TABLE IF NOT EXISTS user_known_images (
 record text NOT NULL,
 username text NOT NULL,
 image text NOT NULL,
 FOREIGN KEY(image) REFERENCES image(image),
 PRIMARY KEY (username, image)
);

CREATE TABLE IF NOT EXISTS user_tried_images (
 username text NOT NULL,
 image text NOT NULL,
 FOREIGN KEY(image) REFERENCES image(image),
 PRIMARY KEY (username, image)
);

/* 1 = easy: 3 to 4 letters, 2 = average: 5 to 6 letters, 3 = hard: more than 6 letters*/

insert into image values ("acorn.png", "acorn", 2);
insert into image values ("ant.png", "ant", 1);
insert into image values ("apple.png", "apple", 2);
insert into image values ("arm.png", "arm", 1);
insert into image values ("backpack.png", "backpack", 3);
insert into image values ("banana.png", "banana", 2);
insert into image values ("basket.png", "basket", 2);
insert into image values ("bathtub.png", "bathtub", 3);
insert into image values ("bed.png", "bed", 1);
insert into image values ("bee.png", "bee", 1);
insert into image values ("bird.png", "bird", 1);
insert into image values ("boat.png", "boat", 1);
insert into image values ("books.png", "books", 2);
insert into image values ("boots.png", "boots", 2);
insert into image values ("brain.png", "brain", 2);
insert into image values ("bread.png", "bread", 2);
insert into image values ("bridge.png", "bridge", 2);
insert into image values ("broom.png", "broom", 2);
insert into image values ("brush.png", "brush", 2);
insert into image values ("bucket.png", "bucket", 2);
insert into image values ("buttons.png", "buttons", 3);
insert into image values ("cake.png", "cake", 1);
insert into image values ("camel.png", "camel", 2);
insert into image values ("camera.png", "camera", 2);
insert into image values ("cardboardbox.png", "cardboardbox", 3);
insert into image values ("carriage.png", "carriage", 3);
insert into image values ("cart.png", "cart", 1);
insert into image values ("cat.png", "cat", 1);
insert into image values ("cheese.png", "cheese", 2);
insert into image values ("chicken.png", "chicken", 3);
insert into image values ("cherries.png", "cherries", 3);
insert into image values ("clock.png", "clock", 2);
insert into image values ("coffee.png", "coffee", 2);
insert into image values ("comb.png", "comb", 1);
insert into image values ("cow.png", "cow", 1);
insert into image values ("crocodile.png", "crocodile", 3);
insert into image values ("desk.png", "desk", 1);
insert into image values ("deer.png", "deer", 1);
insert into image values ("diamond.png", "diamond", 3);
insert into image values ("dog.png", "dog", 1);
insert into image values ("donkey.png", "donkey", 3);
insert into image values ("door.png", "door", 1);
insert into image values ("drawer.png", "drawer", 2);
insert into image values ("dress.png", "dress", 2);
insert into image values ("ear.png", "ear", 1);
insert into image values ("egg.png", "egg", 1);
insert into image values ("eye.png", "eye", 1);
insert into image values ("feather.png", "feather", 3);
insert into image values ("fish.png", "fish", 1);
insert into image values ("flag.png", "flag", 1);
insert into image values ("fly.png", "fly", 1);
insert into image values ("foot.png", "foot", 1);
insert into image values ("fork.png", "fork", 1);
insert into image values ("fruits.png", "fruits", 2);
insert into image values ("geese.png", "geese", 2);
insert into image values ("giraffe.png", "giraffe", 3);
insert into image values ("glove.png", "glove", 2);
insert into image values ("gnome.png", "gnome", 2);
insert into image values ("hammer.png", "hammer", 2);
insert into image values ("hanger.png", "hanger", 2);
insert into image values ("hare.png", "hare", 1);
insert into image values ("hats.png", "hats", 1);
insert into image values ("heart.png", "heart", 2);
insert into image values ("horn.png", "horn", 1);
insert into image values ("house.png", "house", 2);
insert into image values ("horse.png", "horse", 2);
insert into image values ("kettle.png", "kettle", 2);
insert into image values ("key.png", "key", 1);
insert into image values ("leaf.png", "leaf", 1);
insert into image values ("lemon.png", "lemon", 2);
insert into image values ("lightbulb.png", "lightbulb", 3);
insert into image values ("map.png", "map", 1);
insert into image values ("match.png", "match", 2);
insert into image values ("mice.png", "mice", 1);
insert into image values ("microwave.png", "microwave", 3);
insert into image values ("monkey.png", "monkey", 2);
insert into image values ("moon.png", "moon", 1);
insert into image values ("mouse.png", "mouse", 2);
insert into image values ("nail.png", "nail", 1);
insert into image values ("needle.png", "needle", 2);
insert into image values ("onion.png", "onion", 2);
insert into image values ("orange.png", "orange", 3);
insert into image values ("owl.png", "owl", 1);
insert into image values ("pan.png", "pan", 1);
insert into image values ("pants.png", "pants", 2);
insert into image values ("pea.png", "pea", 1);
insert into image values ("peacock.png", "peacock", 3);
insert into image values ("pear.png", "pear", 1);
insert into image values ("pen.png", "pen", 1);
insert into image values ("pencil.png", "pencil", 2);
insert into image values ("pig.png", "pig", 1);
insert into image values ("pin.png", "pin", 1);
insert into image values ("plane.png", "plane", 2);
insert into image values ("potato.png", "potato", 2);
insert into image values ("pots.png", "pots", 1);
insert into image values ("rainboots.png", "rainboots", 3);
insert into image values ("rhino.png", "rhino", 2);
insert into image values ("rocket.png", "rocket", 2);
insert into image values ("rooster.png", "rooster", 3);
insert into image values ("rope.png", "rope", 1);
insert into image values ("scarf.png", "scarf", 2);
insert into image values ("schoolbus.png", "schoolbus", 3);
insert into image values ("scissors.png", "scissors", 3);
insert into image values ("scooter.png", "scooter", 3);
insert into image values ("screw.png", "screw", 2);
insert into image values ("seagull.png", "seagull", 3);
insert into image values ("sheep.png", "sheep", 2);
insert into image values ("ship.png", "ship", 1);
insert into image values ("shirt.png", "shirt", 2);
insert into image values ("sled.png", "sled", 1);
insert into image values ("snail.png", "snail", 2);
insert into image values ("snake.png", "snake", 2);
insert into image values ("sneakers.png", "sneakers", 3);
insert into image values ("sofa.png", "sofa", 1);
insert into image values ("spider.png", "spider", 2);
insert into image values ("sponge.png", "sponge", 2);
insert into image values ("squirrel.png", "squirrel", 3);
insert into image values ("stamp.png", "stamp", 2);
insert into image values ("star.png", "star", 1);
insert into image values ("stoplight.png", "stoplight", 3);
insert into image values ("store.png", "store", 2);
insert into image values ("strawberry.png", "strawberry", 3);
insert into image values ("street.png", "street", 2);
insert into image values ("suitcase.png", "suitcase", 3);
insert into image values ("sun.png", "sun", 1);
insert into image values ("swan.png", "swan", 1);
insert into image values ("swing.png", "swing", 2);
insert into image values ("table.png", "table", 2);
insert into image values ("thumb.png", "thumb", 2);
insert into image values ("ticket.png", "ticket", 3);
insert into image values ("tiger.png", "tiger", 2);
insert into image values ("tomato.png", "tomato", 2);
insert into image values ("tooth.png", "tooth", 2);
insert into image values ("train.png", "train", 2);
insert into image values ("tree.png", "tree", 1);
insert into image values ("trumpet.png", "trumpet", 3);
insert into image values ("ufo.png", "ufo", 1);
insert into image values ("umbrella.png", "umbrella", 3);
insert into image values ("whale.png", "whale", 2);
insert into image values ("wolve.png", "wolve", 2);
insert into image values ("yarn.png", "yarn", 1);
insert into image values ("zebra.png", "zebra", 2);
