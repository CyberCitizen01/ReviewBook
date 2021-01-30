from django.urls import path
#from . import views
from movies.views import(
    give_movie_review,
    select_movie,
    index,
    details,
    reccomend_to_add,
    review_detail,
    edit_review
)

app_name='movies'

urlpatterns = [
    path('review/movie/<int:movie_id>', give_movie_review, name="give_movie_review" ),
    path('selectmovie/', select_movie, name="select_movie" ),
    path('reccomendmovies/', reccomend_to_add, name="reccomend_to_add" ),
    path('<slug>/', review_detail, name="review_detail"),
    path('<slug>/edit', edit_review, name="edit_review"),
    path('', index, name="index"),
    path('<int:movie_id>', details, name="details"),
    
]
