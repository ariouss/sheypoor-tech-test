# sheypoor-tech-test
Sheypoor nested comments technical interview test.

How to use?

First you need to install all requirements using pip -r install requirements.txt
Then you need to migrate using python manage.py migrate
Then you need run app using python manage.py runserver



You can see all active comments in /comments
You can create a comment using api/comments
You can activate or deactive a comment with set status on True or False using api/comments/{comment_id}
You can delete or update a comment using api/comments/{comment_id}
You can delete a parent comment and then that delete with all children using api/comments/{parent_id}
You can see data in django admin pannel with create a super user.

Good luck :D
