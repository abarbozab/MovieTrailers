# Movie Trailers - Project

In this a simple Movie Trailer Website for Udacity's full-stack [Nanodegree Program]. This static webpage displays a list of favorite movies favorite movies and watch the trailers.

## Description
This is a server-side application written in Python that generates an HTML file containing information of some movies such as name, year, director, a poster and then displays the movie trailer.

## Quick start

### Installation
Requires Python 2.7 or above, which can be download from the [Python website].

### Usage
 To start the application, simply open and run the `entertainment_center.py` module using IDLE. This will generate a `fresh_tomatoes.html` file which will then be displayed on the browser.

 The list of movies can be edited in the `entertainment_center.py` module.

### What's included
```
MovieTrailers.zip/
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── media.py
└── README.md
```

### Movie Properties
Movies have the following properties, which are all strings:
* `title`
* `storyline`
* `running_time`
* `genre`
* `poster_image`
* `trailer_youtube`
* `director`
* `release_date`
* `actors`
#### Example to instantiate a Movie Class
```
apocalyto = media.Movie('Apocalyto'
                        ,"The Mayan kingdom is at the height of its opulence and power but the foundations"
                         " of the empire are beginning to crumble.The leaders believe they must build more"
                         " temples and sacrifice more people or their crops and citizens will die."
                          " Jaguar Paw (Rudy Youngblood), a peaceful hunter in a remote tribe, is captured"
                          " along with his entire village in a raid. He is scheduled for a ritual sacrifice"
                          " until he makes a daring escape and tries to make it back to his pregnant wife"
                          " and son."
                         ,"2h 10m"
                         ,"Thriller/Drama"
                         ,'http://www.gstatic.com/tv/thumb/dvdboxart/161392/p161392_d_v8_aa.jpg'
                         ,'https://www.youtube.com/watch?v=ngWBddVNVZs'
                         ,"Mel Gibson"
                         ,"2016-12-08"
                         ,"Rudy Youngblood, Dalia Hernández, Raoul Trujillo, Jonathan Brewer")
```


[Nanodegree Program]: <https://www.udacity.com/nanodegree>
[Python website]: <https://www.python.org/download/releases/2.7/>
