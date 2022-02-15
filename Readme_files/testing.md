
- <a href="#Manual-testing">1. Manual testing</a>
  - <a href="#Project">1.1. Project goals</a>
  - <a href="#User-story">1.2 User stories</a>
  - <a href="#Admin-story">1.3 Admin stories</a>
- <a href="#Automated-testing">2. Automated testing</a>
- <a href="#Code-validators">3. Code validators</a>
- <a href="#Responsiveness">4. Responsiveness</a>
- <a href="#Browser-compability">5. Browser compability</a>
- <a href="#bugs">6. Bugs</a>



<span id="Manual-testing"></span>
## 1. Manual testing:

**The following user stories were tested manually.**

<span id="Project"></span>

### 1. 1 Testing Project goals
- Sell alcoholic drinks online.

**Testing**

The site is successfully connected to stripe and the webhook responds to the events 
- **Result:** Test passed

- Be intuitive for users and easy to navigate.

**Testing**

The site counts with a navigation bar that is displays in all formats: mobiles, tablets and desktops. Each of the elements from the navbar where tested and they all work perfectly. 

**Result:** Test passed

- Make the user feel safe when buying on this site

**Testing**

When a user buy a product from the website he/she gets an modal notification which informs that the purchase has been successful. Besides they also get an e-mail with all details that confirms that the orden has been place and has been successful. furthermore, if shoppers are members of the site they can find a historial with a list of their last orders.

**Result:** Test passed

- Let the administrator add, edit, search and delete products from the stock.
**Testing**
The administrators of the site can add, read, edit, and delete not only products but also posts from the blog and reviews from the products. 

**Result:** Test passed

- Help users find drinks that can not be found easily on regular markets.

**Testing**

- Most of the products offered in the site are foreign products that are not easily found in common liqueur stores.

**Result:** Test passed

<span id="User-story"></span>
### 1. 2 Testing  User Stories
### As a first time visitor I want:

- To have access to all the produgit cts of the store

**Testing**

- When a user clicks on the all products link in the navigation bar have access to all the products that are offered in the site. Furthermore, users can make use of the search bar to find an specific product.

**Result:** Test passed

- To buy alcohol online

**Testing**

All products displayed on the site are to be bought by the users trhough the website. 

**Result:** Test passed

- To pay online

**Testing**

As the site is successfully linked to stripe users can pay their purchases using either a debit as well as a credit card to pay. 

**Result:** Test passed

- To buy online without an account

**Testing**

Users  do not need to be members to buy on this site. they will need to add the information required to get their products but their information will nor be storaged. Therefore, everytime this kind of user want to make a purchase they will need to introduce their information. 

**Result:** Test passed

- A confirmation mail after each purchase

**Testing**

Everytime users place an order they will get a confirmation email with all the details of the purchase.  

**Result:** Test passed


- To have a way to communicate with the store (Email, Tel, etc)

**Testing**

In the footer visitors can find the information required to contact the store. email, telephone and social media links.  

**Result:** Test passed

- To sort the products in order of price, category, rating and name.

**Testing**

In the header of the site users find the different ways to access the products offered in the site. Therefore, they products can be sorted out by its price, category, rating, or name.

**Result:** Test passed

- During the buying process i want to keep informed of errors and validations

**Testing**

As the users navigate trhough the site they will be informed about  the different actions taken during the shopping process. For example: if a user does not add the information required when submitting an order an error message will be displayed making the user aware of the mistakes done. Also if a product or review was added successfully a message will be shown to assure the user of the action just taken.  

**Result:** Test passed

- To have a searching box to find products easily
**Testing**

When navigating the site users can make use of the search bar in order to speed up the proccess of finding a product. This search bar is available in all kind of devices. thus it can be found in desktops, tablets and mobiles.  

**Result:** Test passed


- To add and removed items from the shopping bag

**Testing**

While shopping users can add and remove items from the shopping bag at any momment. They can acccess the shopping bag not matter in which section of the site they are.

**Result:** Test passed

- To be able to make purchases in different devices (mobile, tablet, desktop)

**Testing**

This site is responsive. it means that it works perfectly fine in all devices(desktops, tablets, and mobiles)

**Result:** Test passed

- To have the option to create an account in the site

**Testing**

All first time visitors have the option to register in the website and create an account in order to save their personal information and speed up future purchases. Besides, registered users have access to add, edit and remove reviews from our products. 

**Result:** Test passed

### As a member user I want: 

- To have a profile to keep a history of my purchases

**Testing**

 As soon as an user is registered a profile page is created. Here users can find their personal information which can easily be updated; A historial of all the purchases done by the user and a list of the reviews made by this user.  

**Result:** Test passed

- To keep my information saved for future purchases

**Testing**

As users create an account they have the chance to save their info by checking the check box  "Save this delivery information to my profile". This info can be found in the profile pagte of the user an can be easily updated based on the users needs. 

**Result:** Test passed

- To be able to log out my session

**Testing**
In the header of the site there is a link called "My account" there users find the option to log out if they are already logged in. Otherwise users will find the options to log in or register if they do not have an account yet. 

**Result:** Test passed

<span id="Admin-story"></span>
### As a Administrator user I want:
- To have access to the list of orders placed in the website
**Testing**
 Users can access the list of all the orders through django admin panel. There administrators can access all the information regarding the name of the users and the different orders they have placed 
 
**Result:** Test passed

- To have a section where i can  add, edit, delete and create new items

**Testing**

 - Administrators can access add, edit and delete products from the site in two different ways: The first option is thought the Django Admin panel which can be accessed by adding /admin at the end of the websites name. The second option is by loging in the website and clicking on the "my account" link and selecting the option "product management". Here Administratiors can also add, edit or delete products from the site.  
 
**Result:** Test passed

<span id="Automated-testing"></span>

## 2. Automates Testing:


<span id="Responsiveness"></span>

<span id="Code-validators"></span>

## 3. Code validators:
## Testing ##

- All the features of this project have been manually tested  in order to make sure they respond effectively. Moreover, users can move from page to page since all of them are interconnected. 


As part of the testing process, this website was tested using:
 - [W3C Markup Validator](https://validator.w3.org/) 
 - [Jigsaw W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [Jshint](https://jshint.com/)
- [Pep8](http://pep8online.com/) 

## W3C Markup Validator

![Html](/Readme_images/29-base_validation.JPG)

The Html code was validated by URI using the [Markup Validation Service](https://validator.w3.org/#validate_by_input). Therefore, the address of the deployed site was used to achive the validation. The errors found correspond to the jinja tool used.

## W3C CSS Validator

![CSS](/Readme_images/30-CSS.JPG)

No errors found in the css files

## Js hint Validator
![JavaScript](/Readme_images/)

## pep8 Python Validator
- When validating the python code there is a warning i could not get rid of. It says "no newline at end of file".
![Python](/Readme_images/)


## 4. Responsiveness:

![Responsiveness](/Readme_images/27-responsiveness-1.JPG)
![Responsiveness](/Readme_images/28-responsiveness-2.JPG)

## 5. Browser-compability
<span id="Browser-compability"></span>
![Responsiveness](/Readme_images/28-Browser.JPG)

## 6. Bugs
<span id="bugs"></span>

## 7. Credits
<span id="Credits"></span>







