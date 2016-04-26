import media
import fresh_tomatoes
# Defining Movies
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
egypt = media.Movie('Gods of Egypt'
                     ,"The survival of mankind hangs in the balance when Set (Gerard Butler), the"
                      " merciless god of darkness, usurps Egypt's throne and plunges the prosperous"
                      " empire into chaos and conflict. Hoping to save the world and rescue his true"
                      " love, a defiant mortal named Bek (Brenton Thwaites) forms an unlikely"
                      " alliance with the powerful god Horus (Nikolaj Coster-Waldau). Their battle"
                      " against Set and his henchmen takes them into the afterlife and across the"
                      " heavens for an epic confrontation."
                     ,"2h 8m"
                     ,"Fantasy/Action"
                     ,'http://t2.gstatic.com/images?q=tbn:ANd9GcRtOqwgh3331PNXsqGLMi215fVKC0j0Oto2viXi7d1_obsI45Kd'
                     ,'https://www.youtube.com/watch?v=IJBnK2wNQSo'
                     ,"Alex Proyas"
                     ,"2016-02-24"
                     ,"Gerard Butler, Nikolaj Coster-Waldau, Courtney Eaton, Brenton Thwaites, Elodie Yung")

punisher = media.Movie('The Punisher'
                       ,"This dark action film, based on the comic book series, follows FBI agent Frank"
                        " Castle (Thomas Jane) as he transforms into the vengeful Punisher after criminals"
                        " murder his family, including his wife and son. Castle is gravely injured in the"
                        " attack and believed to be dead by Howard Saint (John Travolta), the crime lord"
                        " who ordered the hit. Following his recovery, Castle becomes a heavily armed"
                        " vigilante who will stop at nothing to exact revenge on Saint and dismantle his"
                        " underworld empire."
                       ,"2h 20m"
                       ,"Thiller/Drama"
                       ,'http://www.gstatic.com/tv/thumb/movieposters/34317/p34317_p_v8_aa.jpg'
                       ,'https://www.youtube.com/watch?v=G59cD1NSbS8'
                       ,"Jonathan Hensleigh"
                       ,"2004-04-16"
                       ,"Thomas Jane, John Travolta, Laura Harring, Rebecca Romijn, Samantha Mathis")

pulp = media.Movie('Pulp Finction'
                   ,"Vincent Vega (John Travolta) and Jules Winnfield (Samuel L. Jackson) are hitmen with"
                    " a penchant for philosophical discussions. In this ultra-hip, multi-strand crime movie,"
                    " their storyline is interwoven with those of their boss, gangster Marsellus Wallace"
                    " (Ving Rhames) ; his actress wife, Mia (Uma Thurman) ; struggling boxer Butch Coolidge"
                    " (Bruce Willis) ; master fixer Winston Wolfe (Harvey Keitel) and a nervous pair of"
                    " armed robbers, 'Pumpkin' (Tim Roth) and 'Honey Bunny' (Amanda Plummer)."
                   ,'2h 58m'
                   ,'Crime film/Drama film'
                   ,'http://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg'
                   ,'https://www.youtube.com/watch?v=s7EdQ4FqbhY'
                   ,'Quentin Tarantino'
                   ,'1995-02-24'
                   ,'Quentin Tarantino, John Travolta, Uma Thurman, Samuel L. Jackson, Bruce Willis')

guardian = media.Movie('Guardians of Galaxy'
                       ,"Brash space adventurer Peter Quill (Chris Pratt) finds himself the quarry of"
                        " relentless bounty hunters after he steals an orb coveted by Ronan, a powerful"
                        " villain. To evade Ronan, Quill is forced into an uneasy truce with four"
                        " disparate misfits: gun-toting Rocket Raccoon, treelike-humanoid Groot,"
                        " enigmatic Gamora, and vengeance-driven Drax the Destroyer. But when he"
                        " discovers the orb's true power and the cosmic threat it poses, Quill must"
                        " rally his ragtag group to save the universe."
                       ,'2h 2m'
                       ,'Fantasy/Action'
                       ,'http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in'
                       ,'https://www.youtube.com/watch?v=B16Bo47KS2g'
                       ,'James Gunn'
                       ,'2014-07-31'
                       ,'Chris Pratt, James Gunn, Zoe Saldana, Dave Bautista, Vin Diesel')

life = media.Movie('Life Is Beautiful'
                   ,"A gentle Jewish-Italian waiter, Guido Orefice (Roberto Benigni), meets Dora"
                   " (Nicoletta Braschi), a pretty schoolteacher, and wins her over with his charm"
                   " and humor. Eventually they marry and have a son, Giosue (Giorgio Cantarini)."
                   " Their happiness is abruptly halted, however, when Guido and Giosue are"
                   " separated from Dora and taken to a concentration camp. Determined to shelter"
                   " his son from the horrors of his surroundings, Guido convinces Giosue that"
                   " their time in the camp is merely a game."
                   ,'2h 2m'
                   ,'Drama film/Comedy-drama'
                   ,'http://www.gstatic.com/tv/thumb/movieposters/22005/p22005_p_v8_aa.jpg'
                   ,'https://www.youtube.com/watch?v=4MpZyOdx4cs'
                   ,'Roberto Benigni'
                   ,'1997-12-20'
                   ,'Roberto Benigni, Giorgio Cantarini, Nicoletta Braschi, Giustino Durano, Horst Buchholz')

#print (egypt);
movies = [apocalyto, egypt, punisher, pulp, guardian, life]

#print (media.Movie.__doc__)
#print (media.Movie.__name__)
fresh_tomatoes.open_movies_page(movies)

