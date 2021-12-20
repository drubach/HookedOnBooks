# Hooked on Books

How many times have you heard someone say "This book changed my life!". 
Some actually do. We love books and are always on the lookout for our 
next read. This site is meant to help do that.
                
Now, while we can't promise that you will definitely find one to change 
your life, we can promise you the opportunity to find some that others have  
found entertaining, informative or motivational or not worth the time. 

How can we promise that? This platform is meant to allow you the opportunity 
to provide reviews and on books you've read and to consider reviews 
others have posted on books they've read.

We want people to be able to share their reviews with others and to connect 
with people across the world. You'll be able to share your reviews, and save 
other titles so you can try them yourself later. What's best, it doesn't cost 
a thing to become a part of our book lover community!

[Feel free to view the live project here](https://hooked-on-books-project.herokuapp.com/)!

## UX

This site is designed to give everyone an enjoyable experience when exploring and sharing book reviews with others online.

#### User Stories:

* First Time Visitor Goals:
    * Easily understand the purpose of the site and why it's important.
    * Quickly learn how to navigate the site and make sure it is intuitively accessible.
    * Visual appeal to have a pleasant first experience.
    * Register easily.

* Returning Visitor Goals:
    * Be able to login easily so my specific information can be seen.
    * Search, save, and create book reviews to share with others.
    * Easily search by author, title or descriptions of books.
    * Read others opinions of books so as to choose new books to read for myself.

* Frequent User Goals:
    * Edit my current reviews/profile information
    * Delete my reviews.
    * Delete my profile.

* Site Owners Goals:
    * Earn money on each book purchased via a link from the site.
    * Start a platform that can be expanded to include other potential paid services.

#### Design Features Include:

* **Mobile Menu** - Consolidating the menu down for mobile devices lets it be flexible for device size.

* **Gradual Fade Ins** - The content on the page has gradual fade in transitions so it's appealing to the user. ##########

### Wireframes

* **Desktop** - [View](HookedOnBooks_Desktop.pdf)

* **Tablet** - [View](HookedOnBooks_Tablet.pdf)

* **Mobile** - [View](HookedOnBooks_Mobile.pdf)

## Features

* **User Registration** - Allows user to store, edit & delete their personal information.

* **User Functions** - Allow user to create, edit & delete their book entries and descripitons.

## Technologies Used

**Languages Used**

* HTML5
* CSS3
* JavaScript
* Python
* Jinja

**Frameworks, Libraries & Programs Used**

1. [Materialilze 1.0.0](https://materializecss.com/)
    * Materialize was used to assist with the responsiveness and styling of the website.

2. [Font Awesome](https://fontawesome.com/)
    * Font Awesome was used on most pages throughout the website to add icons for aesthetic purposes.

3. [Git](https://git-scm.com/)
    * Git was used for version control by utilizing VS Code to commit to Git and Push to GitHub.

4. [GitHub](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git.

5. [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes during the design process.

6. [JQuery](https://jquery.com/)
    * JQuery was used to write shorter, simpler Javascript.

7. [Hover.css](https://ianlunn.github.io/Hover/)
    * Hover.css is used to change the text and background color of buttons and links upon hovering over them.

8. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Flask is the web microframework this project is built on.

9. [PyMongo](https://pypi.org/project/pymongo/)
    * The PyMongo library is how this project interacts with the MongoDB where information is housed.

10. [MongoDB](https://www.mongodb.com/)
    * MongoDB is used as a cloud database solution to store every piece of data my site uses.

## Testing

I used the W3C Markup Validator, W3C CSS Validator Services, and JSHint to validate every page of the project, and all JS code to ensure there were no major syntax errors in the project.

[W3C Markup Validator](https://validator.w3.org/)
[W3C CSS Validator](http://jigsaw.w3.org/css-validator/)
[JSHint](https://jshint.com/)

Results were saved to a pdf for easy review, take a look! [View](HookedOnBooks-TestResults.pdf)

### Testing User Stories from UX Section

* First Time Visitor Goals:
    * Easily understand the purpose of the site and why it's important.
        * The homepage has an About section that outlines the purpose of HookedOnBooks.
    * Quickly learn how to navigate the site and make sure it is intuitively accessible.
        * Intuitive menu along with helpful redirects help users to navigate the site with ease.
    * Visual appeal to have a pleasant first experience.
        * Clean & pleasant look.

* Returning Visitor Goals:
    * Be able to login/register so my specific information can be seen.
        * Users will be able to register with a unique username & password, so they can view information relevant to them on their profile page.
    * Search, save, and create reviews to share with others.
        * Users are able to search by book titles, authors and descriptions. They can create their own reviews to be seen by others.

* Frequent User Goals:
    * Edit current reviews/profile information.
        * Users can edit every bit of their own reviews, minus the owner.
        * Users can edit every bit of their profile, minus the date registered.
    * Delete books I have no need of anymore.
        * Once in their own book, there is a delete button at the bottom if they so choose to delete the.

### Further Testing

* The site was tested on a variety of devices from desktop to mobile to tablet. Other devices were simulated through Chrome dev tools.
    * It did not perform well on the variety of sizes. 

* Lighthouse was used to test the pages of this site.
    * All results are above 90 and "Best Practices" was even rated 100.

* Browsers used to test include Chrome, Edge, Safari, Opera, and Firefox.

* The Home Page was tested on a variety of different device sizes and it looks great on desktop, tablet, and mobile.

* The login process has been tested and verified. Users are not able to login if they enter an invalid username or password.

* The register process has been tested and verified. User will be stopped from registering if an existing username is being used. They will also be stopped if ithe password doesn't meet the data validation rules to do with special characters.

* The search function has been tested and verified. Users can search by title, auther or description and the site returns a list of reviews that match said criteria. If no match exists, the page will say that no "Results not Found", and prompt them to search again. 

* The add a book function has been tested and verified. Users can add books with titles, authors and a short description. 

* The edit a book function has been tested and verified. On books they have entered, users can update a book title, authors and a short description. 

* The delete a book function has been tested and verified. On books they have entered, users can delete a book completely from the database. 

* The Profile page has been tested and verified. Users can manage their profile by changing their user name and password. They can also delte their profile.

* All pages were tested on a variety of different device sizes and it looks great on desktop, tablet, and mobile.

* All links on all pages are tested and operational.

### Known Bugs

*   Currently, the footer stays in position and interferes with the lower reviews.

*   The sizing and layout in other size devices besides the desktop are not working right. 
    
## Future Work

*   Obviously fix known bugs.

*   Add in a longer review text box, and the ability to save multiple reviews to each book, with full CRUD ability.

*   Add in a rating function, perhaps even automating a hidden rating system driven sentiment analysis of the reviews.

*   Improve the UI to be more attractive.

*   Add in the ability to have a picture of the book cover from a URL.

*   Add in automated Amazon links to generate referral income.

*   Add in a chat or zoom integration to be able to run online book clubs.

## Deployment

### Heroku

This project was deployed to Heroku using the steps below:

1. Log into GitHub and locate the [GitHub Repository](https://github.com/drubach/hooked-on-books).
2. Log into Heroku and create a new Python app.
3. Under deploy, find Deployment method, and select Github.
4. Select the appropriate repository as shown in step one, and select deploy from master.
5. Enable automatic deploys so when a change is pushed to Github, Heroku automatically adopts the new changes.

### Forking the Repository

You can fork the repository and create a copy for yourself in your own account.

1. Log into GitHub and locate the [GitHub Repository](https://github.com/drubach/hooked-on-books).
2. Locate the Fork button, next to the repository settings button.
3. Go to your repositories, and you should see a copy made for you to edit as you please.

### Local Clone

If you'd like to have a copy on your local machine, follow the steps below:

1. Log into GitHub and locate the [GitHub Repository](https://github.com/drubach/hooked-on-books).
2. Under the name of the repository, click 'Clone or Download'.
3. Click 'Clone with HTTPS', and copy the link.
4. Open Git Bash on your local computer.
5. Change the directory to where you want the clone located.
6. Type ```git clone``` and paste the URL from step 3.
7. Hit enter. A local clone was now created in the directory you specified.

## Credits

#### Media

* 1 image is saved to use a background in future upgrades. [library-shelves](https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGlicmFyeXxlbnwwfHwwfHw%3D&w=1000&q=80).

#### Content

* All content was written by the developer.

#### ReadMe

*   The outline and format for the ReadMe was inspired by [Jake Rubach's MS3 project](https://github.com/StoneMasons4106/connect-recipes). I also borrowed his footer which he got from a template.

#### Code

* The majority of the code in this project is taken from the mini-project and just tweaked to do what I wanted it to do. Thanks to the instructors for this!!

* I also borrowed his part of his footer which he got from a template. [Jake Rubach's MS3 project](https://github.com/StoneMasons4106/connect-recipes)

* To get an automatic time and date stamp, I used the package 'datetime' and got the code to implement it from this [site](https://www.geeksforgeeks.org/get-utc-timestamp-in-python/) .

#### Acknowledgments

* My mentor for continuous and helpful support/design suggestions.