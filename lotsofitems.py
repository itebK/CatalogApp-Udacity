from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="khayati", email="khayati.iteb@gmail.com")
session.add(User1)
session.commit()

# Create category of Baseball
category1 = Categories(user_id=1, name="Baseball")
session.add(category1)
session.commit()


# Create category of Basketball
category2 = Categories(user_id=1, name="Basketball")
session.add(category2)
session.commit()

# Create category of Tennis
category3 = Categories(user_id=1, name="Tennis")
session.add(category3)
session.commit()

# Create category of Handball
category4 = Categories(user_id=1, name="Handball")
session.add(category4)
session.commit()

# Create category of Soccer
category5 = Categories(user_id=1, name="Soccer")
session.add(category5)
session.commit()

# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="Two Shin guards",
                             description="A shin guard or \
                             shin pad is a piece \
                             of equipment worn on the front \
                             of a player s shin \
                             to protect them from injury",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Soccer cleats",
                             description="Football shoes have \
                              studs on their soles \
                             Cleats or studs are protrusions \
                             on the sole of a shoe, \
                             or on an external attachment to \
                             a shoe, that provide \
                             additional traction on a soft or \
                             slippery surface",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Ball",
                             description="Ball used in handball \
                              is similar to the \
                              volley ball or the balls that are \
                               used in football, \
                               but nowadays a special type of \
                               ball has been made \
                               which is tailor-made for easy \
                               carrying and passing \
                               from hand to hand.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Rackets",
                             description="The components of a \
                             tennis racket include \
                              a handle, known as the grip, \
                              connected to a neck which \
                              joins a roughly elliptical \
                              frame that holds a matrix \
                              of tightly pulled strings",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Balls",
                             description="Tennis balls were \
                              originally made \
                              of cloth strips stitched together \
                              with thread \
                              and stuffed with feathers",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Shoes",
                             description="One needs specialized shoes when \
               playing basketball. It should be able to give \
               better support to the ankle as compared to running shoes. \
               The basketball shoes should be high-tipped shoes \
               and provide extra comfort during a game. These shoes \
               are specially designed to maintain high traction on \
               the basketball court.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Basketball Shooting Equipment",
                             description="The hoop or basket is a horizontal \
               metallic rim, circular in shape. This rim is \
               attached to a net and helps one score a point. \
               The rim is mounted about 4 feet inside the baseline \
               and 10 feet above the court.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Basketball Court",
                             description="The basketball court is the next \
               important \
               thing for shooting balls in this game. The \
               court is usually \
               made of wooden floorboard. The court size is \
               about 28m x 17m \
               according to the International standards. The \
               National Basketball \
               Association (NBA) regulation states the floor \
               dimension as 29m x 15m. \
               The standard court is rectangular in shape and \
               has baskets placed \
               on opposite ends.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Backboard",
                             description="The backboard is the rectangular \
               board that is placed behind \
               the rim. It helps give better rebound to the \
               ball. The backboard is about \
               1800mm in size horizontally and 1050mm vertically. \
               Many times, backboards \
               are made of acrylic, aluminum, steel or glass.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Bat",
                             description="A rounded, solid wooden or hollow \
               aluminum bat. \
               Wooden bats are traditionally made from ash wood, \
               though maple \
               and bamboo is also sometimes used. Aluminum bats \
               are not permitted \
               in professional leagues, but are frequently used \
               in amateur leagues. \
               Composite bats are also available, essentially \
               wooden bats with a metal \
               rod inside. Bamboo bats are also becoming popular.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Ball",
                             description="A cork sphere, tightly wound with \
               layers of yarn or \
               string and covered with a stitched leather coat.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Base",
                             description="One of four corners \
               of the infield which \
               must be touched \
               by a runner in order to score a run; more specifically, \
               they are canvas \
               bags (at first, second, and third base) and a rubber \
               plate (at home).",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Glove",
                             description="Leather gloves worn by players \
               in the field. \
               Long fingers \
               and a webbed 'KKK' between the thumb and first finger \
               allows the fielder \
               to catch the ball more easily.",
                             categories=category1)
session.add(categoryItem1)
session.commit()


print "added category items!"
