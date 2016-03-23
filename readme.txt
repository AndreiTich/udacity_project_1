
                          Entertainment_center.py

  What is it?
  -----------

  This is the first project of the Udacity Full Stack Developer course.
  It uses python in order to dynamically create a web page with movie
  posters, trailers, and some basic information. I have gone beyond the
  original requirements of the project to add additional information about
  the movies such as release year, and genre (as well as a couple simple 
  animations to bring the page to life). In addition, I have made it a lot 
  easier to generate new movie object by gathering most of the information 
  from an open movie database API (OMDB). Hope that you enjoy it!

  Installation
  ------------

  This project used python 2.7.10 for development. In order to run the
  file properly, please make sure you have at least that version of python
  to properly generate the web page.

  Other than that, the web page requires a modern web browser that supports
  CSS3 animations and youtube videos. 

  Use
  ---

  To generate a movie page, run the entertainment_center.py file with python.
  This will dynamically generate a web page showing the movies which are
  listed in the file.

  If you using a Linux like terminal you can run it by navigating to the
  project folder and running

      python entertainment_center.py

  This should automatically generate the "fresh_tomatoes.html" file and open
  it in your default web browser. For the page to properly display you movies
  an Internet connection is required.

  Adding and removing movies
  __________________________

  You can very easily add your own movies to display. All you need to do is
  make a new movie is create a new movie object in entertainment_center.py
  like so:

      OBJECT_NAME = media.Movie(MOVIE_TITLE(str), YOUTUBE_TRAILER_URL(str))

  Then you add that object to the "movies" array, and as long as that movie
  exists in the OMDB and you spelled the title correctly, it will correctly
  generate the web page with your movie added.

  To remove a move you do not like, just delete the object declaration and
  remove that object from the "movies" array.

  Potential improvements
  ______________________

  A major way I can see to improve this project is to add error checking to 
  the object creation phase. If the movie is not found in the database, it 
  can be ignored and then reported to the user who runs the script.

