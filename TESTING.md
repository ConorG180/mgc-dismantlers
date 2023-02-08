# Testing

# Browser Compatibility
Testing of the website was carried out in Firefox, Microsoft Edge, Opera and Google Chrome. Throughout the different browsers, no significant changes were observed, and the programme remained consistent both aesthetically and functionally.

# **Responsiveness**
Incorporating responsiveness into the project was made relatively straightforward due to bootstraps Grid feature. Nevertheless, testing on the programme was carried out manually to ensure responsiveness down to screen size of 350px. With Bootstrap, a burger button was also implemented in place of the navbar on smaller screens, along with the use of horizontal scrolling through tables.  

Whilst manually testing for responsiveness, some small changes had to be made to ensure that the programme was fully responsive, including:

* Change wishlist form so that each field takes up a full column on smaller screens.
* Using media queries to reduce the image size of images on carousel on smaller screens.
* Using media queries to reduce the image size of images of orders in the order history and checkout-success sections on smaller screens.
* Adding a ```min-width``` style property to the filter form on the ```products.html``` page to prevent fields in form from becoming too small.
* Removing margin and padding from carousel row and column to prevent horizontal scrolling on homepage.
* Removing price and order heading on ```cart.html``` on smaller screens.

## Homepage
#### **Images**
![Homepage](static/static-images/responsive-testing-homepage.PNG "Homepage")

## Products
#### **Images**
![Products](static/static-images/responsive-testing-products.PNG "Products")

## Profile
#### **Images**
![Profile large screen](static/static-images/responsive-testing-profile-large-screen.png "Profile large screen")
![Profile mobile](static/static-images/responsive-testing-order-history-mobile.png "Profile mobile")

## Order history
#### **Images**
![Order history large screen](static/static-images/responsive-testing-order-history-large-screen.png "Order history large screen")
![Order history mobile](static/static-images/responsive-testing-order-history-mobile.png "Order history mobile")

## Wishlist
#### **Images**
![Wishlist large screen](static/static-images/responsive-testing-wishlist-large-screen.png "Wishlist large screen")
![Wishlist mobile](static/static-images/responsive-testing-wishlist-mobile.png "Wishlist mobile")

## Cart
#### **Images**
![Cart large screen](static/static-images/responsive-testing-cart-large-screen.png "Cart large screen")
![Cart mobile](static/static-images/responsive-testing-cart-mobile.png "Cart mobile")

## Checkout
#### **Images**
![Checkout large screen](static/static-images/responsive-testing-checkout-large-screen.png "Checkout large screen")
![Checkout mobile](static/static-images/responsive-testing-checkout-mobile.png "Checkout mobile")

## Checkout success
#### **Images**
![Checkout success large screen](static/static-images/responsive-testing-checkout-success-large-screen.png "Checkout success large screen")
![Checkout success mobile](static/static-images/responsive-testing-checkout-success-mobile.png "Checkout success mobile")


# Testing and identified bugs
The following tools and technologies were used to test this project:
## **W3 HTML validator**
For each HTML template in the project, W3 HTML validator was used to test if there were any syntax mistakes or bad practices used within the template. However, W3 HTML validator unfortunately does not consider Jinja templating language being used within the .html files. As a result, many errors were displayed which seemed to be a result of the validator's shortcomings. Images can be seen below of errors/issues being displayed purely because of the Jinja templating language used within the .html files.  

After reviewing these errors/issues displayed by the W3 HTML validator, it was determined that these errors/issues were clearly the result of the Jinja templating language not being taken into consideration by the test. Jinja is clearly a key component of the templates and is designed to be used with django, therefore it was decided that these errors were irrelevant.  

With that in mind, all templates were still tested and any errors which were found not to be related to Jinja were identified and corrected.  

Below are images which display some irrelevant issues displayed from the W3 HTML validator relating to Jinja, and also examples of genuine errors which were fixed.


### **base.html**
Proving hard to test the ```base.html``` page accurately with jinja tags in the template, so they were removed from the validator to test accurately.
The ```title``` element was discovered not to be present in any templates, so this was updated according to each html template.

#### **images**
![base.html testing before](static/static-images/base.html-testing-before.png "base.html testing before")
![base.html testing after](static/static-images/base.html-testing-after.png "base.html testing after")


### **index.html**
removed ```bold``` element as child from ```p``` element. Replaced with ```span``` element.
Furthermore, ```alt``` attributes were discovered to be left out of ```img``` elements, so were added.

#### **images**
![index.html testing before](static/static-images/index.html-testing-before.png "index.html testing before")
![index.html testing after](static/static-images/index.html-testing-after.png "index.html testing after")

### **products.html**
no bugs were found, however, ```alt``` attributes were discovered to be left out of ```img``` elements, so were added.

### **add-product.html**
no bugs were found.

### **edit-product.html**
no bugs found.

### **cart.html**
Added alt attributes to images
Removed ```button``` element as child from ```anchor``` elements
Furthermore, ```alt``` attributes were discovered to be left out of ```img``` elements, so were added.

#### **images**
![cart.html testing before](static/static-images/cart.html-testing-before.png "cart.html testing before")
![cart.html testing after](static/static-images/cart.html-testing-after.png "cart.html testing after")

### **checkout.html**
no bugs were found, however, ```alt``` attributes were discovered to be left out of ```img``` elements, so were added.

### **checkout-success.html**
no bugs were found, however, ```alt``` attributes were discovered to be left out of ```img``` elements, so were added.

### **profile.html**
```button``` elements were turned to ```anchor``` elements as they contained ```href``` attributes

#### **images**
![profile.html testing before](static/static-images/profile.html-testing-before.png "profile.html testing before")
![profile.html testing after](static/static-images/profile.html-testing-after.png "profile.html testing after")

### **categories-navbar.html**
no bugs found.

### **navbar.html**
no bugs found.

### **footer.html**
no bugs found.


## **W3C CSS validator**
Whilst bootstrap was used for the majority of styling throughout this project, a custom css style sheet (```base.css```) was used to provide customer styling throughout the project. This can be seen in the orange coloring used throughout the website and in resizing certain elements media queries to make the website more responsive.

To test this custom-written CSS, the W3C CSS validator was used. Upon testing, five minor errors were discovered. These errors were easily fixed and were the result of using invalid units of measurement within css. 

Seven warnings were also found within the css, however these were not deemed to be problematic and in some cases were even needed to ensure cross-browser compatability of the project. Therefore, these were untouched.

The testing images of before and after can be seen below:  

![base.css testing before](static/static-images/base.css-testing-before.PNG "base.css testing before")
![base.css testing after](static/static-images/base.css-testing-after.PNG "base.css testing after")

## **PEP 8**
PEP 8 guidelines and practises were implemented when building this project. To test this, it was originally planned to use [pep8online.com](http://pep8online.com/). However, as of the time of creating this project, the website is currently not active and cannot be accessed. Therefore, it was decided to use the extention `pycodestyle` to test if the python code adhered to the PEP 8 guidelines and practises.

All python files contained PEP 8 errors of some kind, the most common of which included:  

* E2 - Whitespace errors
* E3 - Blank line errors
* E5 - Line length errors
* W2 - Whitespace warnings

Whilst these errors were not causing fatal errors within the project or preventing the software from functioning as expected, it can still be considered bad practise to leave these errors within the project. This is mainly from a "code readability" perspective. In correcting these errors, the code will be easier to maintain in the future should updates/changes need to be implemented. Furthermore, future debugging will also be made much easier.

## **Jshint Javascript validator**
The Jshint Javascript validator was used to test the project's Jquery scripts. It should be noted that in the configure options of Jshint, in the **"Assume"** tab, the **"New JavaScript features (ES6)"** and **"Jquery"** were selected, as the Js in the project uses ES6 features such as ```const``` and ```let```, and the majority is written with the Jquery framework.  
All of the errors that Jshint validator flagged were due to missing semi-colons.  
Images of the before and after testing for each html document containing Javascript can be seen below:  

### **products.html javascript**
the Javascript in the products.html page is used to control the filter form and the automated dropdown boxes which update automatically.  

#### **images**
![products.html Javascript testing before](static/static-images/products.html-js-testing-before.PNG "products.html Javascript testing before")
![products.html Javascript testing after](static/static-images/products.html-js-testing-after.PNG "products.html Javascript testing after")

### **add-product.html javascript**
the Javascript in the add-product.html page is used to control the automated dropdown boxes which update automatically in the form.  

#### **images**
![add-product.html Javascript testing before](static/static-images/add-product.html-js-testing-before.PNG "add-product.html Javascript testing before")
![add-product.html Javascript testing after](static/static-images/add-product.html-js-testing-after.PNG "add-product.html Javascript testing after")

### **edit-product.html javascript**
the Javascript in the edit-product.html page is used to control the automated dropdown boxes which update automatically in the form.  

#### **images**
![edit-product.html Javascript testing before](static/static-images/edit-product.html-js-testing-before.PNG "edit-product.html Javascript testing before")
![edit-product.html Javascript testing after](static/static-images/edit-product.html-js-testing-after.PNG "edit-product.html Javascript testing after")

### **footer.html javascript**
the Javascript in the footer.html page is used to control the automated dropdown boxes in the embedded wishlist form in the footer.  

#### **images**
![footer.html Javascript testing before](static/static-images/footer.html-js-testing-before.PNG "footer.html Javascript testing before")
![footer.html Javascript testing after](static/static-images/footer.html-js-testing-after.PNG "footer.html Javascript testing after")

### **base.html javascript**
the Javascript in the base.html page is used to control the toast messages/notifications, specifically to remove the notifications after 7.5 seconds.  

#### **images**
![base.html Javascript testing before](static/static-images/base.html-js-testing-before.PNG "base.html Javascript testing before")
![base.html Javascript testing after](static/static-images/base.html-js-testing-after.PNG "base.html Javascript testing after")

# Unfixed Bugs
One bug was discovered that is yet to be fixed.
  - If a user is logged out and attempts to add an item to their wishlist/or to their cart etc, they will be prompted to login before adding the item (This is thanks to the ```@login_required``` decorator in the ```views.py``` files) and once they log in, an error will be shown. However, this can easily be fixed by pressing the back button on the page, where the user will now be logged in.
