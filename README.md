# Blogger
The title of the project is Blogger

## Description
Its a Flask application that allows writers to post blogs, edit and delete them. Signed in users can view, comment, like and dislike the blogs.

## Live link
[Blogger]().

## User Stories
- A user can view the blog posts on the site.
- A user can comment on blog posts.
- A user can view the most recent posts.
- A user can random quotes on the site.
- A writer can sign in to the application.
- A writer can create a blog from the application.
- A writer can delete comments that they find insulting or degrading
- A writer can update or delete blogs I have created.
- A user can  vote on the pitch they liked and give it a downvote or upvote.
- A user can view the different categories of blogs.

## Development Installation
1. Clone the repository:
    ```
    git clone git remote add origin https://github.com/Mash14/Blogger.git
    ```
2. Move to the folder, create a virtual environment and  install the requirements
    ```
    pip install virtualenv
    virtualenv virtual
    pip install -r requirements.txt
    ```
3. Export configurations in the config.py
    ```
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
    ```
4. Run the application and open the lie link
    ```
    python3 manage.py server
    # link
    http://127.0.0.1:5000/
    ```
5. Test the application
    ```
    python3 manage.py test
    ```

## Technology Used
- Python3.8
- Flask
- Heroku
- CSS3

## Known Bugs
There are no know bugs.

## Author's Details
The author of the project was Alan Macharia.

## Contact Information
You can reach him by: 
- Email: mashalonzo741@gmail.com
- Tel no: +254704485919

## License and Copyright Information
Copyright 2022 Alan Macharia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.