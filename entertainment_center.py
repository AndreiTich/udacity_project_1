import media
import fresh_tomatoes

toy_story = media.Movie("Toy story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
the_matrix = media.Movie("The matrix", "https://www.youtube.com/watch?v=m8e-FF8MsqU")
equilibrium = media.Movie("equilibrium", "https://www.youtube.com/watch?v=raleKODYeg0")
inception  = media.Movie("inception", "https://www.youtube.com/watch?v=66TuSJo4dZM")
interstellar = media.Movie("interstellar", "https://www.youtube.com/watch?v=zSWdZVtXT7E")
pans_labyrinth = media.Movie("pan's labyrinth", "https://www.youtube.com/watch?v=EqYiSlkvRuw")

movies = [toy_story, the_matrix, equilibrium, inception, interstellar, pans_labyrinth]

fresh_tomatoes.open_movies_page(movies)