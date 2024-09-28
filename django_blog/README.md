# Overview
#    A simple Django blog application with user authentication, post management, and profile handling.

# Features
#    - User Authentication: Includes registration, login, and logout functionality.
#    - Post Management: Users can create, update, delete, and view blog posts.
#    - Profile Management: Users can update their profiles.

# Views
#    - Create Post: Accessible to authenticated users only, automatically setting the post author to the logged-in user.
#    - Update Post: Allows only the post author to edit their posts.
#    - Delete Post: Allows only the post author to delete their posts.
#    - List Posts: Displays all blog posts.
#    - Post Detail: Shows details for a specific post.

# URL Patterns
#    - /                : List all posts.
#    - /post/<int:pk>/   : Post detail view for a specific post.
#    - /post/new/        : Create a new post.
#    - /post/<int:pk>/edit/ : Edit an existing post.
#    - /post/<int:pk>/delete/ : Delete a post.
#    - /login/           : Login page.
#    - /logout/          : Logout page.
#    - /register/        : Registration page.
#    - /profile/         : User profile page.

# Authentication
#    - Uses `LoginRequiredMixin` to ensure users are logged in to create posts.
#    - Uses `UserPassesTestMixin` to restrict editing and deletion to the post authors only.
