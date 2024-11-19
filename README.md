# **EdenHub Social Media**

## Developer: Morgan Asare

EdenHub API is a Django-based web application for [EdenHub](https://github.com/CleanOak/diyconnect_PP4backend), designed for users to share their love for nature through posting inspirational photos from across the world. The API enables user authentication, profile management, leaving comments, liking other posts and following other users.

**LIVE SITE**

[You can view the live web application here.](https://edenhub-060ed3b8a582.herokuapp.com/)

# **CONTENTS**

<!-- TOC -->

- [**CONTENTS**](#contents)
- [**Planning**](#planning)
    - [**User Stories**](#user-stories)
    - [**Data Models**](#data-models)
    - [**Relationships**](#relationships)
        - [User Profile:](#user-profile)
        - [Posts:](#posts)
        - [Comments:](#comments)
        - [Likes:](#likes)
        - [Followers:](#followers)
        - [Notifications:](#notifications)
- [**Website Security**](#website-security)
    - [env.py File](#envpy-file)
- [**Features/Apps**](#featuresapps)
    - [**Profiles**](#profiles)
    - [**Posts**](#posts)
    - [**Category**](#category)
    - [**Comments**](#comments)
    - [**Likes**](#likes)
    - [**Followers**](#followers)
    - [**Notifications**](#notifications)
- [**Testing**](#testing)
- [**Technologies & Packages**](#technologies--packages)
    - [**Main Technologies**](#main-technologies)
    - [**Packages**](#packages)
- [**Deployment**](#deployment)
    - [**Environment & Settings**](#environment--settings)
    - [**Deploying to Heroku**](#deploying-to-heroku)
- [**Credits**](#credits)

<!-- /TOC -->

---

# **Planning**

## **User Stories**

A user story was created solely for the backend to ensure focus and consistency. You can view the user stories on [this project board](https://github.com/users/CleanOak/projects/5).


## **Data Models**

Various data models were drawn out before creating the actual models, to serve as a blueprint for database design, helping with concepts and organisation of the structure of a database.

| **MODEL**                    |          **KEY**                      |    **NAME**              |   **TYPE**              |
| ------------------------------------------ | ------------------------------------- | ---------------- |-----------------------|
| **CATEGORY APP**                               |                                                             |             |        |
| *Category List*                              |                                                             |             |          |
| **Testcase**                                   | **Expected Result**                        | **Test Result** |                    |
| GET /category/ Unauthenticated             | 200 OK, list of all categories                          | Pass✅       |               |
| GET /category/ Authenticated               | 200 OK, list of all categories                         | Pass✅       |                |
| POST /category/ Authenticated              | 201 Created, new category created                     | Pass✅       |                 |
| POST /category/ Unauthenticated            | 403 Forbidden, user not authenticated                 | Pass✅       |                  |
| *Category Detail*                            |                                          |                    |                      |

## **Relationships**

### User Profile:
- User (OneToOne): Each user has a user profile, establishing a OneToOne relationship. This ensures that each user has a single profile, and vice versa.

### Posts:
- User (OneToMany): Each post is created and uploaded by a user. This relationship indicates a OneToMany relationship, where one user can create multiple posts, but each post is associated with only one user.
- Category (ManyToOne): Each post can belong to a category (optional). This relationship indicates a ManyToOne relationship, where multiple posts can belong to the same category, but each post is linked to one category.

### Comments:
- Recipe Post (OneToMany): Comments are associated with posts, following a OneToMany relationship. Each post can have multiple comments, but each comment is linked to only one post.
- User (OneToMany): Similarly, comments are posted by users, forming another OneToMany relationship. A user can write multiple comments, but each comment is linked to only one user.

### Likes:
- Post (OneToMany): Likes are associated with posts, following a OneToMany relationship. Each post can have multiple likes, but each like is linked to only one post.
- User (OneToMany): Similarly, likes are made by users, forming another OneToMany relationship. A user can like multiple posts, but each like is attributed to only one user.

### Followers:
- User (ManyToMany): Followers represent a ManyToMany relationship with users. A user can follow many users, and each user can be followed by many users.

### Bookmark
- User (OneToMany): bookmarks are made by users, forming another OneToMany relationship. A user can bookmark multiple posts, but each bookmark is attributed to only one user.
- Post (OneToMany): Bookmarks are associated with posts, following a OneToMany relationship. Each post can have multiple bookmarks, but each bookmark is linked to only one post.


---

# **Website Security**

## env.py File
- API keys and databases are stored in the env.py which is not included in version control to prevent exposure.

---

# **Features/Apps**

To explain the features of the API, it is easier to break them down by Apps. A short explanation of each app is detailed below.

## **Profiles**

When a user registers on the app, a Profile is automatically created for them. This can then be updated by the user should they wish.

**API Endpoints:**
- **/profiles/**: to list (GET) profiles.
- **/profiles/:id/**: to show (GET) or update (PUT) a profile.

## **Posts**

Posts can be viewed by any user, whether they are logged in or not. However, only registered users who are logged in can create, update and delete a post. 

Posts can be filtered and searched.

**API Endpoints:**
- **/posts/**: to list (GET) or create (POST) posts.
- **/posts/:id/**: to show (GET), update (PUT) or delete (DELETE) a post.

**API Endpoints:**
- **/category/**: to list (GET) categories.

## **Comments**

Logged-in users can engage with posts by leaving their own comments. Users are able to create, update and delete comments.

**API Endpoints:**
- **/comments/**: to list (GET) all comments or create (POST) a new comment.
- **/comments/:id/**: to show (GET) a specific comment, update (PUT) or delete (DELETE) a comment.

## **Likes**

Logged-in users are able to like posts or other user profiles. Users are able to see their likes and delete them if they wish.

**API Endpoints:**
- **/likes/**: to list (POST) likes.
- **/likes/:id/**: to show (GET) or delete (DELETE) a like.

## **Bookmarks**
Logged-in users are able to bookmark posts of other user profiles. Users are able to see their bookmarked and delete them if they wish.

**API Endpoints:**
- **/bookmarks/**: to list (POST) bookmarks.
- **/bookmarks/:id/**: to show (GET) or delete (DELETE) a bookmark.

## **Followers**

Logged-in users are able to follow and unfollow other users.

**API Endpoints:**
- /followers/: to list (**GET**) profiles.
- /followers/:id/: to show (**GET**) or delete (**DELETE**) a follow.

# **Testing**

[Testing for the API can be found here in a separate file - TESTING.md](TESTING.md)

-----

# **Technologies & Packages**

## **Main Technologies**

- **Django** - a Python-based framework for backend development.
- **JavaScript** - for functionality.
- **PostgreSQL from CI** - a database to store all data.

## **Packages**

- **cloudinary==1.40.0 & django-cloudinary-storage==0.3.0** - Cloud-based media hosting and storage.
- **dj-database-url==0.5.0** - Utility library for Django.
- **dj-rest-auth==2.1.9** - Authentication and registration endpoints for Django REST framework.
- **Django==4.2** - Python framework.
- **django-allauth==0.50.0** - User authentication, registration, and account management.
- **django-cors-headers==4.4.0** - Middleware Cross-Origin Resource Sharing (CORS) to allow requests from different domains.
- **django-filter==24.2** - Filter querysets in Django REST framework.
- **django-heroku==0.3.1** - Configures Django to run on Heroku by managing settings for Heroku deployment.
- **djangorestframework==3.15.2** - Toolkit for building Web APIs in Django.
- **djangorestframework-simplejwt==5.3.1** - Provides JSON Web Token (JWT) authentication for Django REST framework.
- **gunicorn==22.0.0** - A WSGI HTTP server for running Django applications in production.
- **oauthlib==3.2.2** - Implementation of OAuth for Python.
- **pillow==10.4.0** - Python Imaging Library.
- **psycopg2==2.9.9** - PostgreSQL adapter for Python.
- **PyJWT==2.8.0** - Python library for encoding and decoding JSON Web Tokens (JWTs).
- **python3-openid==3.2.0** - A library for OpenID authentication in Python 3.
- **pytz==2024.1** - A library for cross-platform timezone calculations.
- **requests-oauthlib==2.0.0** - OAuthlib integration for the Requests library.
- **sqlparse==0.5.1** - SQL statements library.
- **whitenoise==6.6.0** - Serves static files in production.

---

# **Deployment**

You can view the deployed API here: [From House to Home API](https://home-api-58bb6b7692c8.herokuapp.com/).
- [Admin page](https://home-api-58bb6b7692c8.herokuapp.com/admin)
- [Profiles](https://home-api-58bb6b7692c8.herokuapp.com/profiles)
- [Posts](https://home-api-58bb6b7692c8.herokuapp.com/posts)
- [Comments](https://home-api-58bb6b7692c8.herokuapp.com/comments)
- [Categories](https://home-api-58bb6b7692c8.herokuapp.com/category)
- [Likes](https://home-api-58bb6b7692c8.herokuapp.com/likes)
- [Followers](https://home-api-58bb6b7692c8.herokuapp.com/followers)

## **Environment & Settings**

- In your IDE open your env.py file or create one in the main directory if it hasn't been created for you.
- Having created your cloud-based database, add the DATABASE_URL value and a SECRET_KEY value to the env.py file.
- Open the settings.py file and import the env.py file and the DATABASE_URL and SECRET_KEY file paths.
- Install Django and add to requirements.txt.
- Create your project.
- Add the STATIC files settings.
- Create a file called Procfile (with a capital P) in the main directory,
- For cloud-based image storage, add Cloudinary URL to env.py
- Add Cloudinary libraries to INSTALLED APPS.
- Add your IDE workspace and Heroku to ALLOWED_HOSTS.
- Make migrations and migrate.
- Create new Django project - *django-admin startproject <home_api>*.
- Create Superuser (email can be left blank) - *python manage.py createsuperuser (username>email>password1>password2)*.
- Create your apps - *python manage.py startapp <nameofapp>*.
- Before you add, commit & push your files to GitHub, ensure DEBUG is set to False in your settings.py file.

## **Deploying to Heroku**

- Log in or create an account on Heroku.com. Click 'New' and then 'Create New App'.
- Give your project a unique name and select a region, then click 'Create App'.
- Connect your Heroku project to your GitHub repository. Under deployment you can choose GitHub, find the relevant one and click 'Connect'.
- Once connected, go to the Settings tab and click on 'Reveal Config Vars'. Add the following:
  - CLOUDINARY_URL - copied URL from Cloudinary
  - DATABASE_URL - copied URL from PostgreSQL
  - SECRET_KEY - a unique secret key
  - ALLOWED_HOST - with the value of your deployed Heroku application URL
  - DISABLE_COLLECTSTATIC - add 1 if this is to be disabled to prevent errors, or 0 if the app is in a state where errors will not be generated.
- Navigate to the Deploy section, click on Github for the deployment method and confirm.
- Search for your repository name and click connect.
- At the bottom of the deploy section, make sure you are connected to the main branch and then click Deploy Branch.
- You can then view your live site.


# **Credits**

All credits and acknowledgements have been detailed in the main frontend repo. [Link to Frontend README file](https://github.com/CleanOak/edenhub_frontend/blob/main/README.md)

