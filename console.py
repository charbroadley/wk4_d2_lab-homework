# Use this file to test your repository functions 
import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# artist_1 = Artist("Prince")
# artist_repository.save(artist_1)

# album_1 = Album ("Lovesexy", 1988, artist_1)
# album_repository.save(album_1)

# artist_2 = Artist("McFly")
# artist_repository.save(artist_2)

# album_2 = Album ("Room on the 3rd Floor", 2004, artist_2)
# album_repository.save(album_2)

# artist_3 = Artist("Queen")
# artist_repository.save(artist_3)

# album_3 = Album ("A Night at the Opera", 1975, artist_3)
# album_repository.save(album_3)

# artist_1 = artist_repository.select(3)
# album_4 = Album ("Purple Rain", 1984, artist_1)

# album_repository.save(album_4)

# album_repository.delete_all()
# artist_repository.delete_all()

# artist_1 = artist_repository.select(3)
# print (artist_1.__dict__)

# album_1 = album_repository.select(2)
# print (album_1.__dict__)

# album_list = album_repository.select_all()
# for album in album_list:
#     print(album.__dict__)

# artist_list = artist_repository.select_all()
# for artist in artist_list:
#     print(artist.__dict__)

album_list = album_repository.select_albums_by_artist("Prince")
for album in album_list:
    print(album.__dict__)