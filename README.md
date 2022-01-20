## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href="#Project">1.1. Project goals</a>
  - <a href="#User-story">1.2 User stories</a>
  - <a href="#Wireframes">1.3 Wireframes</a>
  - <a href="#Design">1.4 Design</a>
- <a href="#Features">2. Features</a>
- <a href="#Technologies">3. Technologies used</a>
- <a href="#Testing">4. Testing</a>
- <a href="#Deployment">5. Deployment</a>
- <a href="#Credits">6. Credits</a>
- <a href="#Media">7. Media</a>
- <a href="#Acknowledgements">8. Acknowledgements</a>
- <a href="#Github">9. 9. Github</a>
<span id="ux"></span>
##  1. UX
<span id="Project"></span>
### 1.1 Project goals
- Sell alcoholic drinks online. 
- Be intuitive for users and easy to navigate.
- Make the user feel safe when buying on this site   
- Let the administrator add, edit, search and delete products from the stock.
- Help users find drinks that can not be found easily on regular markets.



## 1.2 User Story: 
<span id="User-story"></span>
### As a first time visitor I want:

- To have access to all the products of the store
- To buy alcohol online
- To pay online
- To buy online without an account
- a confirmation mail after each purchase
- To have a way to communicate with the store (Email, Tel, etc)  
- To sort the products in order of price, category, rating and name.
- During the buying process i want to keep informed of errors and validations
- To have a searching box to find products easily
- To add and removed items from the shopping bag
- To be able to make purchases in different devices (mobile, tablet, desktop)
- To have the option to create an account in the site


### As a member user I want: 

- To have a profile to keep a history of my purchases
- To keep my information saved for future purchases
- To be able to log out my session
- To receive newsletters 


### As a Administrator user I want: 
 - To have access to the list of orders placed in the website
 - To have a section where i can  add, edit, delete and create new items
 - To have access to the information of the members 





## 1. 3  [Wireframes ](/wireframes/MS4.png)
[See Wireframes ](/wireframes/MS4.png)
<span id="Wireframes"></span>

These wireframes where designed  with [Figma](https://www.figma.com/file/4KmzBdwzyrvZAVXoKUaZVM/MS4?node-id=0%3A1)
which is a very instuitive prototyping tool that focuses in the user interface and user experience design.

## 1.4 Design
<span id="Design"></span>
This website was designed using [ecommerce](https://startbootstrap.com/templates/ecommerce)
A basic Bootstrap ecommerce page template from [startboostrap](https://startbootstrap.com/).
This template was chosen thinking on a minimalist 
concept which transmits serenity and tranquillity. Therefore, all pages are diaphanous but functional, avoiding the overuse of colors which could be stressful  and overwhelming for the users.
Hence, black and  white are the predominant colors. There are also some other colors such as yellow, green, red and blue in puntual elements as bottoms, icons and links.

**Colors**
- Black #000000: used for the font, icons, and some alerts.
- White #ffffff: used for the body  
- Gray ##636262: used when hover in the links 
- Green #26a69a: edit buttons in profile page
- Red #e15562: user for the delete button in the admin's edit form and in the revome link from the shopping bag. 
- Yellow #ffc107: user for the alert in the shopping bag when the shipping price has not been reached.

**Font**

The Fonts used in this site are Lato and Monserrat which were taken from google.fonts. The Monserrat is used in the landing page for the visual impact it has on the visitors due to its width. On the other hand, Lato is the predominant font found since its thickness offers the space between each letter making it easier for the user to read. In general terms these fonts fit perfectly with the eastethics of the site and offer a perfect contrast which helps the user to distinguis between title, notification and general information.

The defensive design on this site relays on the Djiango built-in models which makes the site secure and straightforward when setting parameters as placeholder, input length or compulsory requirements. 





## 2. Features
<span id="Features"></span>

2.1. Existing features

2.1.1 Home:
The home page counts with an image that welcomes the visitors introducing them to what they will find in the site.  

2.1.2 Navigation bar:
This website has a navigation bar that displays different features depending on the actions te user takes. If a user registers and logs in, then the features from the navigation bar will be different from those who do not do it. A first time visitor will only find in the Nabvar the chance to register and login. And if they sign up they navbar will display some other hidden links reserved to members. On this navbar the administrato will have the chance to manage and keep updated the products of the store.

2.1.3 Register:
On this feature users can create an account adding a user name and a password

2.1.4 Log In:
Through this feature user access to the content reserved to those who have an account.

2.1.5 Profile:
Is a page that contains some information from the user, as well as, the history of the purchases made. 

2.1.6 log Out:
When cliking on this option the user leaves his/her account, having access only to the home page. It means they are not allowed to add, edit or erase any recipe.

2.1.7 Product Management:
All administravie users have the chance to add new products to the page through a form linked to the dababase in order to keep it updated.

2.1.8 Search bar:
In order to help users to easily find a product there is a search bar located in the header of the home page in which they can type the term needed and it will be filtered and displayed in the screen.

2.1.9 Categories:
This features helps the user to sort the products by certain categories as price, rate.

2.2.0 Age filter: 
to enter the site the users are asked their age in order to let them have access to the site. 

2.2.1 stripe:
users can complete their purchase paying online thanks to stipe which is the software which handle the payments.

2.2.2 Email confirmation: 
After every purchase the users will recieve a confirmation E-mail with the information of the transaction.

## 3. Technologies used
<span id="Technologies"></span>
This website was built using:
- [HTML](https://html.com) **HTML**is used to create pages and make them functional.
- [CSS](https://css3.com) **Css** is used to style the page
- [Boostrap](https://Boostrap.com) **Boostrap** is used also to style the page
- [Fontawesome](https://fontawesome.com/) **Fontawesome** used to add icons
- [Googlefont](https://fonts.google.com/) **Googlefont** used to set the font
- [Gitpot](http://gitpod.io/) **Gitpod** use to edit and built the page
- [Github](http://github.com/) **Github** use to storage the page 
- [Figma](http://figma.com/) **Figma** used to creat a wireframe or mock-up 
- [Photoshop](http://photoshop.com/) **Photoshop** used to edit the images used in the page. 
- [Responsivedesign](http://ami.responsivedesign.is/) **Responsive Design** to show how it looks in defferent devices. 
- [Startbootstrap](https://startbootstrap.com/templates/ecommerce) **Startbootstrap** html and css template used to build the front-end
 - [materializecss](https://materializecss.com/) **Materialized** A modern responsive front-end framework based on Material Design 
 - [Python](https://www.python.org/) **Python** is a computer programming language used to build websites and software, automate tasks, and conduct data analysis.
 - [JavaScript](https://www.javascript.com/) **JavaScript** is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive 
- [Heroku](https://www.heroku.com/) **Heroku** is use to deploy, manage, and scale modern apps.
- [Django](https://www.django.com/)**Django** is a web framework. tahts provides tools, libraries and technologies that allows to build a web application.
- [AWS](https://www.AWS.com/)**AWS** Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
## 4. Testing 
<span id="Testing"></span>

## 5.  Deployment
<span id=" Deployment"></span>

##  6. Credits
<span id="Credits"></span>
https://www.youtube.com/watch?v=jSOKrzOKRoI
django admin name change 

## 7. Media
<span id="Media"></span>

## 8. Acknowledgements
<span id="Acknowledgements"></span>

## 9. Github
<span id="Github"></span>



