from hitbox import Hitbox

Hitboxes = {}
Hitboxes["HBox1"] = Hitbox(10, 10, 100, 100)
Hitboxes["HBox2"] = Hitbox(130, 10, 100, 100)
Hitboxes["HBox3"] = Hitbox(250, 10, 100, 100)
Hb1WHb2 = Hitboxes["HBox1"].Intersects(Hitboxes["HBox2"])
Hb2WHb3 = Hitboxes["HBox2"].Intersects(Hitboxes["HBox3"])