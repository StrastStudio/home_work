from hitbox import Hitbox

Hitboxes = {}
Hitboxes["HBox1"] = Hitbox(10, 10, 100, 100)
Hitboxes["HBox2"] = Hitbox(90, 30, 100, 100)
Hitboxes["HBox3"] = Hitbox(170, 10, 100, 100)
Hb1WHb2 = Hitboxes["HBox1"].Intersects(Hitboxes["HBox2"])
Hb2WHb3 = Hitboxes["HBox2"].Intersects(Hitboxes["HBox3"])
Hb3WHb2 = Hitboxes["HBox3"].Intersects(Hitboxes["HBox2"])