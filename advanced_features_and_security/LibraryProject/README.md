
﻿# Permissions and Groups Setup

## Permissions
The following custom permissions have been added to the Book model:
- can_view_book
- can_create_book
- can_edit_book
- can_delete_book

## Groups
Three groups have been created with the following permissions:

1. Editors
   - can_create_book
   - can_edit_book

2. Viewers
   - can_view_book

3. Admins
   - can_view_book
   - can_create_book
   - can_edit_book
   - can_delete_book

## Usage
The permissions are enforced in the following views:
- book_list: requires can_view_book permission
- create_book: requires can_create_book permission
- edit_book: requires can_edit_book permission
- delete_book: requires can_delete_book permission

