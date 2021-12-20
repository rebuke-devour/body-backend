"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
        RouteGroup([
        Get("/", "BodyController@index").name("index"),
        Get("/@id", "BodyController@show").name("show"),
        Post("/", "BodyController@create").name("create"),
        Put("/@id", "BodyController@update").name("update"),
        Delete("/@id", "BodyController@destroy").name("destroy")
    ],prefix="/body",name= "Body")
]
