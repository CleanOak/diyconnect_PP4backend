# **TESTING**

[Back to the README document.](README.md)

# **CONTENTS**

<!-- TOC -->

- [**TESTING**](#testing)
- [**CONTENTS**](#contents)
- [**VALIDATION**](#validation)
    - [**JSHint Validator**](#jshint-validator)
    - [**MANUAL TESTING**](#manual-testing)

<!-- /TOC -->

---

# **VALIDATION**

## **JSHint Validator**

- I went through all code and checked that all imports were in the order of standard library imports first, then third party imports and finally local imports. There were only a couple that needed changing.
- All code was put through the Code Institute Python Linter. Other than a few blank line spaces and no new lines at the end of the file (which were fixed), it all passed without errors.

---

## **MANUAL TESTING**

- I manually tested each page and feature, which despite coming back with passes, didn't necessarily mean it was going to tie up when I started my front end, as I realised. I did come across a few bugs, but these will be listed in my Frontend README document which I will cross reference.

| **HOME_API MANUAL TESTING**                    |                                                             |             |
| ------------------------------------------ | ----------------------------------------------------------- | ----------- |
| **CATEGORY APP**                               |                                                             |             |
| *Category List*                              |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /category/ Unauthenticated             | 200 OK, list of all categories                              | Pass✅       |
| GET /category/ Authenticated               | 200 OK, list of all categories                              | Pass✅       |
| POST /category/ Authenticated              | 201 Created, new category created                           | Pass✅       |
| POST /category/ Unauthenticated            | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Category Detail*                            |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /category/<id>/ Unauthenticated        | 200 OK, details of the category with given id               | Pass✅       |
| GET /category/<id>/ Authenticated          | 200 OK, details of the category with given id               | Pass✅       |
| PUT /category/<id>/ Owner                  | 200 OK, category updated                                    | Pass✅       |
| PUT /category/<id>/ Not Owner              | 403 Forbidden, user not authorized to update                | Pass✅       |
| PUT /category/<id>/ Unauthenticated        | 403 Forbidden, user not authenticated                       | Pass✅       |
| DELETE /category/<id>/ Owner               | 204 No Content, category deleted                            | Pass✅       |
| DELETE /category/<id>/ Not Owner           | 403 Forbidden, user not authorized to delete                | Pass✅       |
| DELETE /category/<id>/ Unauthenticated     | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **COMMENT APP**                                |                                                             |             |
| *Comment List*                               |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /comments/ Unauthenticated             | 200 OK, list of all comments                                | Pass✅       |
| GET /comments/ Authenticated               | 200 OK, list of all comments                                | Pass✅       |
| POST /comments/ Authenticated              | 201 Created, new comment created                            | Pass✅       |
| POST /comments/ Unauthenticated            | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Comment Detail*                             |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /comments/<id>/ Unauthenticated        | 200 OK, details of the comment with given id                | Pass✅       |
| GET /comments/<id>/ Authenticated          | 200 OK, details of the comment with given id                | Pass✅       |
| PUT /comments/<id>/ Owner                  | 200 OK, comment updated                                     | Pass✅       |
| PUT /comments/<id>/ Not Owner              | 403 Forbidden, user not authorized to update                | Pass✅       |
| PUT /comments/<id>/ Unauthenticated        | 403 Forbidden, user not authenticated                       | Pass✅       |
| DELETE /comments/<id>/ Owner               | 204 No Content, comment deleted                             | Pass✅       |
| DELETE /comments/<id>/ Not Owner           | 403 Forbidden, user not authorized to delete                | Pass✅       |
| DELETE /comments/<id>/ Unauthenticated     | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **FOLLOWERS APP**                              |                                                             |             |
| *Follower List*                              |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /followers/ Unauthenticated            | 200 OK, list of all follower relationships                  | Pass✅       |
| GET /followers/ Authenticated              | 200 OK, list of all follower relationships                  | Pass✅       |
| POST /followers/ Authenticated             | 201 Created, new follower relationship created              | Pass✅       |
| POST /followers/ Unauthenticated           | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Follower Detail*                            |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /followers/<id>/ Unauthenticated       | 200 OK, details of the follower relationship with given id  | Pass✅       |
| GET /followers/<id>/ Authenticated         | 200 OK, details of the follower relationship with given id  | Pass✅       |
| DELETE /followers/<id>/ Owner              | 204 No Content, follower relationship deleted               | Pass✅       |
| DELETE /followers/<id>/ Not Owner          | 403 Forbidden, user not authorized to delete                | Pass✅       |
| DELETE /followers/<id>/ Unauthenticated    | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Followed Posts*                             |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /followed-posts/ Authenticated         | 200 OK, list of posts from followed users                   | Pass✅       |
| GET /followed-posts/ Unauthenticated       | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **LIKES APP**                                  |                                                             |             |
| *Like List*                                  |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /likes/ Unauthenticated                | 200 OK, list of all likes                                   | Pass✅       |
| GET /likes/ Authenticated                  | 200 OK, list of all likes                                   | Pass✅       |
| POST /likes/ Authenticated                 | 201 Created, new like created                               | Pass✅       |
| POST /likes/ Unauthenticated               | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Like Detail*                                |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /likes/<id>/ Unauthenticated           | 200 OK, details of the like with given id                   | Pass✅       |
| GET /likes/<id>/ Authenticated             | 200 OK, details of the like with given id                   | Pass✅       |
| DELETE /likes/<id>/ Owner                  | 204 No Content, like deleted                                | Pass✅       |
| DELETE /likes/<id>/ Not Owner              | 403 Forbidden, user not authorized to delete                | Pass✅       |
| DELETE /likes/<id>/ Unauthenticated        | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Liked Posts*                                |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /liked-posts/ Authenticated            | 200 OK, list of posts liked by the authenticated user       | Pass✅       |
| GET /liked-posts/ Unauthenticated          | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **POSTS APP**                                  |                                                             |             |
| *Post List*                                  |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /posts/ Unauthenticated                | 200 OK, list of all posts                                   | Pass✅       |
| GET /posts/ Authenticated                  | 200 OK, list of all posts                                   | Pass✅       |
| POST /posts/ Authenticated                 | 201 Created, new post created                               | Pass✅       |
| POST /posts/ Unauthenticated               | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| *Post Detail*                                |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /posts/<id>/ Unauthenticated           | 200 OK, details of the post with given id                   | Pass✅       |
| GET /posts/<id>/ Authenticated             | 200 OK, details of the post with given id                   | Pass✅       |
| PUT /posts/<id>/ Owner                     | 200 OK, post updated                                        | Pass✅       |
| PUT /posts/<id>/ Not Owner                 | 403 Forbidden, user not authorized to update                | Pass✅       |
| PUT /posts/<id>/ Unauthenticated           | 403 Forbidden, user not authenticated                       | Pass✅       |
| DELETE /posts/<id>/ Owner                  | 204 No Content, post deleted                                | Pass✅       |
| DELETE /posts/<id>/ Not Owner              | 403 Forbidden, user not authorized to delete                | Pass✅       |
| DELETE /posts/<id>/ Unauthenticated        | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **PROFILES APP**                               |                                                             |             |
| *Profile List*                               |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /profiles/ Unauthenticated             | 200 OK, list of all profiles                                | Pass✅       |
| GET /profiles/ Authenticated               | 200 OK, list of all profiles                                | Pass✅       |
|                                            |                                                             |             |
| Profile Detail                             |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /profiles/<id>/ Unauthenticated        | 200 OK, details of the profile with given id                | Pass✅       |
| GET /profiles/<id>/ Authenticated          | 200 OK, details of the profile with given id                | Pass✅       |
| PUT /profiles/<id>/ Owner                  | 200 OK, profile updated                                     | Pass✅       |
| PUT /profiles/<id>/ Not Owner              | 403 Forbidden, user not authorized to update                | Pass✅       |
| PUT /profiles/<id>/ Unauthenticated        | 403 Forbidden, user not authenticated                       | Pass✅       |
|                                            |                                                             |             |
| **HOME_API**                                   |                                                             |             |
| *Root Route*                                 |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET / Unauthenticated                      | 200 OK, welcome message                                     | Pass✅       |
| GET / Authenticated                        | 200 OK, welcome message                                     | Pass✅       |
|                                            |                                                             |             |
| *Logout Route*                               |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| POST /dj-rest-auth/logout/ Unauthenticated | 200 OK, cookies cleared, no session                         | Pass✅       |
| POST /dj-rest-auth/logout/ Authenticated   | 200 OK, cookies cleared, no session                         | Pass✅       |
|                                            |                                                             |             |
| *Current User Serializer*                    |                                                             |             |
| **Testcase**                                   | **Expected Result**                                             | **Test Result** |
| GET /dj-rest-auth/user/ Unauthenticated    | 403 Forbidden, user not authenticated                       | Pass✅       |
| GET /dj-rest-auth/user/ Authenticated      | 200 OK, user details including profile_id and profile_image | Pass✅       |
|                                            |                                                             |             |