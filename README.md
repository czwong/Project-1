# Project-1
This project conducts exploratory analysis on Spotify's top 50 songs by country to look for trends between genre, danceability, and popularity. See [Abstract](https://github.com/czwong/Project-1/blob/master/Abstract.ipynb)


## Data Collection

* [Spotify's API](https://developer.spotify.com/documentation/web-api/) - Where we collected our data from
* [Converting To Excel with Playlist ID](https://github.com/czwong/Project-1/blob/master/Convert_To_Excel_PlaylistID.ipynb) - Pulling from Spotify's API
	* We created an excel sheet that listed the playlist IDs of each country's Top 50 Songs, which we pulled directly from the Spotify application. See [Top 50 playlists](https://github.com/czwong/Project-1/blob/master/Top50_Playlist_by_Country.xlsm).
	* We used nested for loops to pull audio data for each track in each country's playlist.
* [Datasets](https://github.com/czwong/Project-1/tree/master/Top%20Country%20CSV) - CSV outputs of each country's top 50 playlist

## Data Exploration
* [Danceability by Country](https://github.com/czwong/Project-1/blob/master/Country_Danceability_Boxplot.ipynb) - Loops through each country's playlist data to examine danceability scores. See [box plot](https://github.com/czwong/Project-1/blob/master/Images/Danceability__Per_Country_Boxplot.png)
* [Genre Popularity in US](https://github.com/czwong/Project-1/blob/master/Genre_Popularity_in_US.ipynb) - Loops through the Top 50 Songs of the US to count and display all genres in the playlist. See [box plot](https://github.com/czwong/Project-1/blob/master/Images/Top_3_Genre_Danceability_in_US_Boxplot.png)
* [Pop, rap and trap by country](https://github.com/czwong/Project-1/blob/master/Pop_Rap_Trap_Popularity_by_Country.ipynb) - See how pop, rap and trap dominates the charts. See [bar graph](https://github.com/czwong/Project-1/blob/master/Images/Percentage_of_Top_3_US_Genre_Per_Country.png)
* [Genre Popularity by Country](https://github.com/czwong/Project-1/blob/master/Genre_Popularity_Around_World.ipynb) - Loops through each country's playlist data to count the number times pop, rap, trap and other genres show up in the top charts. See [graphs](https://github.com/czwong/Project-1/tree/master/Images)

## Final Notebook
* [Analysis](https://github.com/czwong/Project-1/blob/master/Final_Presentation.ipynb)
