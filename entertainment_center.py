import fresh_tomatoes
import media

#Creating instances of a class
titanic = media.Movie("Titanic",
                      "A seventeen-year-old aristocrat falls in love with a kind, but"
                      " poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=kVrqfYjkTdQ",
                      "Leonardo DiCaprio, Kate Winslet")

martian = media.Movie("The Martian",
                      "During a manned mission to Mars, Astronaut Mark Watney"
                      " is presumed dead after a fierce storm and left behind"
                      " by his crew.",
                      "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                      "https://www.youtube.com/watch?v=ej3ioOneTy8",
                      "Matt Damon, Jessica Chastain")
                   
jurassic_world = media.Movie("Jurassic World",
                             "A new theme park is built on the original site"
                             " of Jurassic Park.",
                             "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                             "https://www.youtube.com/watch?v=RFinNxS5KN4",
                             "Chris Pratt, Omar Sy")
spy = media.Movie("Spy",
                  "A desk-bound CIA analyst volunteers to go undercover to"
                  " infiltrate the world of a deadly arms dealer, and prevent"
                  " diabolical global disaster.",
                  "https://upload.wikimedia.org/wikipedia/en/5/5d/Spy2015_TeaserPoster.jpg",
                  "https://www.youtube.com/watch?v=ltijEmlyqlg",
                  "Melissa McCarthy, Jason Statham")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's family, a"
                                " nostalgic screenwriter finds himself mysteriously"
                                " going back to the 1920s every day at midnight.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "Owen Wilson")
hunger_games = media.Movie("Hunger games",
                           "Katniss Everdeen voluntarily takes her younger sister's"
                           " place in the Hunger Games, a televised competition in"
                           " which two teenagers from each of the twelve Districts"
                           " of Panem are chosen at random to fight to the death.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8",
                           "Jennifer Lawrence")

#Defining array with movies 
movies = [titanic, martian, jurassic_world, spy, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

