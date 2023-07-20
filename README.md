# Overview
Media App is a web application that allows users to create posts and user accounts, view posts and user accounts, update user accounts, and delete user accounts. As a database PostgreSQL is used. Users can also log in to the application to access additional features(get a notification email). For sending the emails Celery and RabbitMQ were implemented. In this project, caching has also been implemented using the Django cache framework. The @method_decorator(cache_page(60*60)) decorator has been applied to the get method of the PostList and UserProfileFilter classes to cache the responses for 1 hour. This helps to reduce the server load and improve the performance of the application.

# Features
View a list of posts sorted by the date created.
Create a post by entering a topic and content.
View a list of user accounts.
Create a user account by entering a username and password.
Log in to an existing user account with a username and password and get a notification email.
Update an existing user account by changing the username and/or password.
Delete an existing user account.
Filter user accounts by username.
When retrieving the posts and user profiles, caching is used. As the caching system Memcached is implemented.
# Acknowledgement 
DRF(Django Rest Framework) official documentation.
