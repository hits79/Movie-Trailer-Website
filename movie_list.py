import fresh_tomatoes
import media

# this file has all the movie list (Name, Summary, Image, & Trailer Links)

the_avengers = media.Movie("The Avengers", 
	"Earth's mightiest heroes must come together and learn to fight as a team  \
	if they are to stop the mischievous Loki and his alien army from \
	enslaving humanity", 
	"http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg", 
	"https://www.youtube.com/watch?v=1hPpG4s3-O4")

avengers = media.Movie("Avengers: Age of Ultron", 
	"When Tony Stark and Bruce Banner try to jump-start a dormant peacekeeping \
	program called Ultron, things go horribly wrong and it's up to Earth's Mightiest \
	Heroes to stop the villainous Ultron from enacting his terrible plans.", 
	"http://ia.media-imdb.com/images/M/MV5BMTU4MDU3NDQ5Ml5BMl5BanBnXkFtZTgwOTU5MDUxNTE@._V1_SY317_CR1,0,214,317_AL_.jpg", 
	"https://www.youtube.com/watch?v=u1OKBqHICMQ")

iron_man = media.Movie("Iron Man", 
	"After being held captive in an Afghan cave, an industrialist creates a unique \
	weaponized suit of armor to fight evil.", 
	"http://ia.media-imdb.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=bK_Y5LjSJ-Y")

iron_man_2 = media.Movie("Iron Man 2", 
	"With the world now aware of his identity as Iron Man, Tony Stark must contend \
	with both his declining health and a vengeful mad man with ties to his father's \
	legacy.", 
	"http://ia.media-imdb.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=FNQowwwwYa0")

iron_man_3 = media.Movie("Iron Man 3", 
	"When Tony Stark's world is torn apart by a formidable terrorist called the \
	Mandarin, he starts an odyssey of rebuilding and retribution.", 
	"http://ia.media-imdb.com/images/M/MV5BMjIzMzAzMjQyM15BMl5BanBnXkFtZTcwNzM2NjcyOQ@@._V1._SY317_.jpg", 
	"https://www.youtube.com/watch?v=aV8H7kszXqo")

the_incredible_hulk = media.Movie("The Incredible Hulk", 
	"Bruce Banner, a scientist on the run from the U.S. Government must find a cure \
	for the monster he emerges whenever he loses his temper. However, Banner then \
	must fight a soldier whom unleashes himself as a threat stronger than he.", 
	"http://ia.media-imdb.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=xbqNb2PFKKA")

sherlock_holmes = media.Movie("Sherlock Holmes", 
	"Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of \
	wits and brawn with a nemesis whose plot is a threat to all of England.", 
	"http://ia.media-imdb.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=J7nJksXDBWc")

sherlock_holmes_games_of_shadows = media.Movie("Sherlock Holmes: A Game of Shadows", 
	"Sherlock Holmes and his sidekick Dr. Watson join forces to outwit and bring down \
	their fiercest adversary, Professor Moriarty.", 
	"http://ia.media-imdb.com/images/M/MV5BMTQwMzQ5Njk1MF5BMl5BanBnXkFtZTcwNjIxNzIxNw@@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=DpxtbtnC1u8")

dawn_of_the_planet_of_the_apes = media.Movie("Dawn of the Planet of the Apes", 
	"A growing nation of genetically evolved apes led by Caesar is threatened by a \
	band of human survivors of the devastating virus unleashed a decade earlier.", 
	"http://ia.media-imdb.com/images/M/MV5BMTgwODk3NDc1N15BMl5BanBnXkFtZTgwNTc1NjQwMjE@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=rf5e7Xc1Hwk")

rise_of_the_planet_of_the_apes = media.Movie("Rise of the Planet of the Apes", 
	"A substance, designed to help the brain repair itself, gives rise to a \
	super-intelligent chimp who leads an ape uprising.", 
	"http://ia.media-imdb.com/images/M/MV5BMTQyMjUxNTc0Ml5BMl5BanBnXkFtZTcwMjg1ODExNg@@._V1_SY317_CR0,0,214,317_AL_.jpg", 
	"https://www.youtube.com/watch?v=X616MkD0k7I")

lucy = media.Movie("Lucy", 
	"A woman, accidentally caught in a dark deal, turns the tables on her captors \
	and transforms into a merciless warrior evolved beyond human logic.", 
	"http://ia.media-imdb.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_SX214_AL_.jpg", 
	"https://www.youtube.com/watch?v=6Vu081NOorA")

# used the backslash to break the lines down a bit
movies = [the_avengers, avengers, iron_man, iron_man_2, iron_man_3, the_incredible_hulk, \
sherlock_holmes, sherlock_holmes_games_of_shadows, dawn_of_the_planet_of_the_apes, \
rise_of_the_planet_of_the_apes, lucy]

fresh_tomatoes.open_movies_page(movies)
