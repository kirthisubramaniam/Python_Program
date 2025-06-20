#Simple program shows how to use function within a program
def display_message():
    print("Learning about function")

display_message()

#Program shows how to call a function with attribute
def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book('2 states')

#Program shows how to call a function with default attribute
def make_shirt(size='L',text='I Love Python'):
    print(f"The size of the shirt {size}.\nThe message to be print is {text}")

make_shirt()
make_shirt('M')
make_shirt(text='Kind')

def describe_city(city_name,country_name='India'):
    print(f"{city_name} is in {country_name}")

describe_city('chennai')
describe_city(city_name='Banaglore')
describe_city('Birmingham','England')

#using function to add album list to a dictionary
def make_album(artist_name,album_title,number_of_tracks=''):
    if number_of_tracks:
        Album={'Artist_name':artist_name,
               'Album_title':album_title,
               'No_of_tracks':number_of_tracks}
    else:
        Album={'Artist_name':artist_name,
               'Album_title':album_title}
    return Album

Albums=[]
while True:
    Artist_name=input("Enter the artist name or quit to exit\n")
    if Artist_name=='quit':
        break

    Album_title=input("Enter the album name\n")
    No_of_tracks=input("Enter number of tracks")
    if No_of_tracks:
        Album_details=make_album(Artist_name,Album_title,No_of_tracks)
    else:
        Album_details=make_album(Artist_name,Album_title)
    Albums.append(Album_details)

for Album in Albums:
    print(Album)

Album_1=make_album('Rahman','Dil Se')
print(Album_1)
Album_2=make_album('Anirudh','Leo',6)
print(Album_2)
Album_3=make_album('Harris','Minnale')
print(Album_3)


     


