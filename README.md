# MGC Dismantlers
MCG Dismantlers are a company which specialise in the sale of second-hand discounted car parts. The company achieves this by purchasing cars, dismantling them, and stocking parts which they can then sell for profit. This project is an e-commerce website designed to facilitate all online activities of the company. While this main activity involves the selling of products online, it also sirves the business and it's users in other ways, such as product-browsing, an online wishlist, and company promotion. The company can easily add all products which they have in stock to the website for customers to browse, and can edit/delete them if needed also. Users have the option to add an item to their "cart" which will show users their currently selected products and offer them an option to checkout and have products delivered to an address. This allows the company to provide an online delivery service of their products, increase exposure of their products/services, and overall increase revenue within the company.  

<!-- The full [MGC Dismantlers](https://mcg-dismantlers.herokuapp.com/) programme can be accessed here. -->

# UX design
## Color scheme
The color scheme chosen for this programme is based on a simple color scheme of Orange and black/navy, with accompany light (usually white) text. The company's logo is also made from a gold/brown gradient, which aims to capture the user's attention and draw focus to the company. This color scheme was chose as it appears to blend aesthetically well with the company's industry of Automobile and stand out enough to draw user attention, whilst at the same time not be overbearing.
Bootstrap is used in the programme so as to easily and efficiently style the various template HTML files. There is also a custom styles.css file to allow for custom styling amongst bootstrap's default files, such as the the brand color of orange used in the logo and hover effects on some buttons. 

## Layout
The grid feature in bootstrap was used to easily and efficiently provide a responsive layout for the website. Bootstraps grid system is based and built from the CSS flexbox feature. This layout was chosen for a number of reasons. Using the grid feature within Bootstrap, elements within the project can very easily be manipulated, hidden, unhidden, swapped, replaced or repositioned in the future if needed. This is especially handy when working on a layout for smaller devices, as certain elements which are not deemed necessary can be hidden if needed, and be prevented from taking up excess space on smaller screens. Furthermore, the very nature of Bootstraps grid is based on a mobile-first design, which easily allows the project to be built responsively and work on devices of all sizes.


# Wireframes
Before starting development on MGC Dismantlers, Balsamiq was used to form wireframes for each separate page within the programme. Basamiq was chosen due to it's efficiency and it's ability to reproduce relatively simplistic, yet easy to understand wireframes. This helped me to visualise ideas for each of the programmes pages and features, and organise how certain features would be laid out and implemented within the programme. Each wireframe created prior to development can be seen below:

![index.html wireframe](wireframes/home.png "index.html (Home page)")
![cart.html wireframe](wireframes/cart.png "cart.html (Cart page)")
![checkout.html wireframe](wireframes/checkout.png "checkout.html (Checkout page)")
![Contact modal wireframe](wireframes/contact-us-modal.png "Contact modal")
![order-history.html wireframe](wireframes/order-history.png "order-history.html (Order history view)")
![products.html wireframe](wireframes/products.png "products.html (Products view)")
![product-info.html wireframe](wireframes/product-info.png "product-info.html (Product detail view)")
![profile.html wireframe](wireframes/profile.png "profile.html (Profile view)")

# Entity Relationship Diagram
Before starting development on MyRosterManagement, diagrams.net/draw.io was used to form an Entity Relationship Diagram (ERD) for the programme. As the programme relies heavily on models and databases, an ERD helped immensely in determining how to structure the database, including aiding in aspects such as relationships between tables, primary and foreign keys, and selecting fields for various tables. The ERD can be seen below:  

![MGC Dismantlers ERD](erd-diagrams/mgc-dismantlers-erd.jpg "MyRosterManagement ERD")

# Features
## Existing features

### Navigation
The programme offers a very simple and easy to use navigation system to navigate around the website. This is not only in the form of moving to different pages, but also for features such as a contact modal and product-category buttons attached to the navbar to allow the user to easily navigate to their category of required car parts. It should be noted that the navbar will 
#### **Images**  
##### **Navbar**
<!-- ![navigation bar](static/images/navigation-bar-logged-in-as-admin.png "navigation bar") -->


### Footer
An attractive footer is included in the programme to offer the user a simple way of easily navigating to the social media pages of the company. The wishlist feature is also included in the footer, to allow users to easily select a make and model and year of a car, and be notified when the product has come into stock.
#### **Images**  
<!-- ![footer](static/images/footer.png "footer") -->

### CRUD (Create, Read, Update, Delete) functionality
An authorised user of the website (Such as the owner/manager etc.) Will have the ability to manipulate the products database. For example, an authorized user may add a new product, delete a product which they no longer have in stock, and edit any details about a product if they wish. The authorised user also has the ability to add different makes/models of a car to the database via the django admin page.  
Read functionality comes from the products page. This allows users (Authorised and unauthorised) to access products via the website's front-end and view their details accordingly.

#### **Images**  
##### **Deleting product form**
<!-- ![Deleting product form](static/images/crud-functionality-delete-product.png "Deleting product form") -->
##### **Adding product form**
<!-- ![Adding product form](static/images/crud-functionality-add-product-form.png "Adding product form") -->
##### **Editing product form**
<!-- ![Editing product form](static/images/crud-functionality-edit-product-form.png "Editing product form") -->
##### **Products page**
<!-- ![Products page](static/images/products-page.png "Products page") -->

### Products page
A user will be able to access a products page to access all products which the company is currently selling. This will allow the user to look at all products which the company currently has in stock, and also give the user access to a host of other options, such as adding products to their cart, searching for products, and filtering products by category.
#### **Images**  
<!-- ![Products page](static/images/products-page.png "Products page") -->

### Product searching
A user will be able to search throught the company's array of products in order to try and find a product which they wish to purchase. This will be enabled through a search bar. The search bar is programmed to enable searches of colors, years, part names, makes and models of car parts.
#### **Images**  
<!-- ![Product searching](static/images/product-search.png "Product searching") -->

### Product categorisation
A user will also be able to categorize the company's array of products to try and find a product which they wish to purchase. To do this, a user can simply click on a category button in the products page or on a button in the category navbar, which will display a list of products to the user which are linked to that category. 
#### **Images**  
<!-- ![Product categorisation navbar](static/images/product-categorisation-navbar.png "Product categorisation navbar") -->
<!-- ![Product categorisation](static/images/product-categorisation-products-page.png "Product categorisation") -->

### Cart
A user will have access to their own "cart" once signing up to the website, which will allow them to manage a potential order. This saves the user time as it allows them to buy multiple products in a single order, as opposed to buying and purchasing each item individually.
#### **Images**  
<!-- ![cart](static/images/cart.png "cart") -->

### Add/Remove products to/from cart
A user will be able to add and remove products from their cart as they wish to allow them to manage a potential order.
#### **Images**  
<!-- ![Add product to cart](static/images/cart-add-product.png "Add product to cart") -->
<!-- ![Remove product from cart](static/images/cart-remove-product.png "Remove product from cart") -->

### Checkout
A user will be able to checkout and purchase items that they have added to their cart. The checkout option will be available from the cart.html page, and when clicked, will reveal a form which the user can enter their information and purchase their chosen items. The user will also be able to see their sub-total, delivery, and grand-total costs for their chosen items from the page. 
#### **Images**  
<!-- ![Checkout](static/images/checkout.png "Checkout") -->

### Checkout success
A user will be redirected to a checkout success page once they complete their order of their chosen products. In the checkout success page, the user will be able to see their order confirmation number, a list of the products that they have just purchased, and also receive a notification that they have been sent an email to their registered email address containing all relevant order information.
#### **Images**  
<!-- ![Checkout success](static/images/checkout-success.png "Checkout success") -->

### Wishlist
A user will be able to create their own wishlist provided they have an account and are logged in. The wishlist will allow them to receive automatic email notifications if a part is added to MCG-dismantler's stock. This helps the user to immediately know if a part is available, and will also increase revenue for the business as they are advertising parts to customers that they have expressed interest in, and letting them know that the part is now available.  
The user must choose a make and model for the wishlist entry, however can choose to include all years/parts, or a specific year/part.  
The wishlist also allows user to keep track of what they need and can be accessed from the wishlist section of the profile page. 
#### **Images**  
<!-- ![Wishlist](static/images/wishlist.png "Wishlist") -->

### Add and remove items from wishlist
A user will also have the ability to add and remove parts from their wishlist as they see fit. A user can remove items from their wishlist through accessing all their wishlist parts in the profile page. A user may add parts to their wishlist through the form available on the footer.
#### **Images**  
<!-- ![Remove product from wishlist](static/images/wishlist-remove-product.png "Remove product from wishlist") -->
<!-- ![Add product to wishlist](static/images/wishlist-add-product.png "Add product to wishlist") -->

### Profile
A user will also have access to their own profile page to store their personal and delivery information. This page can be updated and saved as the user wishes. It is planned that in the future, this page will be used to pre-populate the checkout form when the user wishes to buy something. This will improve the user experience when a user wishes to purchase products from the website.
#### **Images**  
<!-- ![Profile](static/images/profile.png "Profile") -->

### Order history
In the profile page, a user will also have access to an order history section. This section of the profile webpage will allow users to see all of their order history, including the total cost of each order, their items, the order number etc. This will help the user to keep track of what they have purchased from the company.
#### **Images**  
<!-- ![Order history](static/images/order-history.png "Order history") -->


## Future features