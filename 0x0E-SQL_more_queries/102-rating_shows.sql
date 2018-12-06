-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT title, COUNT(rate) AS rating FROM tv_shows LEFT JOIN (tv_show_genres, tv_genres, tv_show_ratings) ON (tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_show_ratings.show_id) GROUP BY title ORDER BY rating DESC;
