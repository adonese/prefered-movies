# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:54:16 2016

@author: mohamed
"""

import media
import fresh_tomatoes
toy_story = media.Movie('Toy Story', 'A story of a boy and his toy that comes to life', 
                        'https://en.wikipedia.org/wiki/File:Toy_Story.jpg', 
                        'https://www.youtube.com/watch?v=4KPTXpQehio')
                    
shawshank = media.Movie('Shawshank', 
                        'Its the great story ever. I can spend a lot of time just saying it is perfect',
                        'http://ecx.images-amazon.com/images/I/91x1IBNmGuL._SL1500_.jpg',
                        'https://www.youtube.com/watch?v=6hB3S9bIaco')                    
pirates_of_carribean = media.Movie('The pirates of the carribean', 'If you love comedy, drama, thriller, etc. you will love this one.',
                                   'http://vignette1.wikia.nocookie.net/disney/images/6/67/Pirates-Of-The-Caribbean-On-Stranger-Tides-Character-Movie-Poster.jpg/revision/latest?cb=20110515180235',
                                   'https://www.youtube.com/watch?v=G7z74BvLWUg')
#print(toy_story.story_line)
    
    
#toy_story.show_trailer()

movies = [toy_story, shawshank, pirates_of_carribean]

fresh_tomatoes.open_movies_page(movies)