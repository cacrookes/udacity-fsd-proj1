# Movie Trailers Website Project

This project was for the first project in Udacity's Full Stack Web Developer nanodegree. The app takes a list of movies, grabs the movie details via **The Movie Database** API, and displays info about the movie. Clicking on a movie plays the trailer for the movie.

## How to run


1. Clone this repository to a folder on your computer.
2. Rename `default.config.py` to `config.py`.
3. In `config.py` enter a valid API key for **The Movie Database** API. You can apply for an API key at:
  - [themoviedb.org](https://www.themoviedb.org/documentation/api?language=en)
4. From the command line, at the root folder of the project, run: `python entertainment_center.py`

This will create an html file in the same directory called `fresh_tomatoes.html`.
This html file will automatically open in the default browser.

On the webpage, clicking on a movie poster or description will launch the corresponding trailer for that movie.

The `fresh_tomatoes.html` file is overwritten each time `entertainment_center.py` is run.
