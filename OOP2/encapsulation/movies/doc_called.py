from documentary import Documentary
m = Documentary()
m._add_movie('My Octopus Teacher',2020,'Documentary')
m._add_channel('NetFliex')
m._get_movie()

#acces protected attribute from super class (Movie)
print(f'Title : {m._title}')