# Wexford | Berries

Wexford Berries is a leading B2C e-commerce platform, offering a wide selection of the freshest and highest quality berries directly to your doorstep. We pride ourselves on sourcing our berries from trusted local farms, ensuring every order is packed with flavor and nutrients. With our easy-to-navigate online store, customers can choose from a variety of berries, including strawberries, blueberries, raspberries, and more. Enjoy the convenience of farm-fresh deliveries and taste the difference with Wexford Berries—where premium quality meets unbeatable freshness.

Link to the live web app: [Wexford | Berries](https://wexford-berries-229479cc7505.herokuapp.com/)

For testing purposes, you can utilize the following [Stripe test card](https://docs.stripe.com/testing#use-test-cards) details:
- Card Number: 4242 4242 4242 4242
- Expiration Date: Enter any future date using the format MM/YY
- CVV: Enter any 3-digit number
- Postal Code: Enter any 5 numerical digits

Please note that payments made using valid debit/credit cards will not be processed, and the card will not be charged. Additionally, no orders placed will be fulfilled.

## Features

### Header and Footer

Header and page should be visible in every page, being also responsive on mobile.

#### Header

The first block at the top and displays the shop logo at the left, a searching box and menu options with 'Products', 'About Us' and 'Contact' which lead to the specific options at the middle and 'My Account' and shopping bag at the right side. If the user is logged in, within the menu options user will also see 'Wishlist' that leads to the products wishlist page. Below mains header content, there is an engaging message offering free delivery upon a spending threshold.

This block is always visible, fixed at the top working as the navigating menu for the entire application. For admin users, there will be another menu option for store management, where store owner can add / remove products in sale and also edit current products.

#### Footer

The third block is at the bottom of page, fixed there. It contains three main rows, with the first one holding the subscribe to the newsletter section. The second is split into three columns displaying the shop name and message, useful links where users and shoppers can find links to 'Home' page, 'Products' page, 'Contact' page, 'About Us' page and 'Privacy Policy' page, and contact information with shop address, email and social. The third one displays the copyright section.

**SECTION**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Header|anonymous|not logged in user|![header-anonymous](/documentation/features/header_annonymous.png)
Header|logged in|'My Account' as a shopper|![header-shopper](/documentation/features/header_shopper.png)
Header|logged in|'My Account' as store owner|![header-store-owner](/documentation/features/header_store_owner.png)
Footer|anonymous or logged in||![footer](/documentation/features/footer.png)

### Landing page

The landing page displays header at the top and footer at the bottom with the content in section in between them. In this case, the content section displays an image with multiple berry fruits to capture users' attention. Above the image, it is displayed an engaging message and a prominently 'Shop Now' button, easily accessible leading users to the products page.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Home|anonymous|landing page view on first access|![landing-page](/documentation/features/home.png)

### Products

The products page display all available products with simplicity and clean design. Each product should have an engaging image, name, price and rating. This page should have different viewing depending on users' status - either as a shopper or store owner. It also displays a shortcut button to bring users back to the top after scrolling down at the bottom left, making it easier return to the top of the page.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Products|shopper|viewing products page as a shopper|![products-shopper](/documentation/features/products_shopper.png)
Products|store owner|viewing products page as store owner, with the buttons to either edit or delete products|![products-store-owner](/documentation/features/products_store_owner.png)

### Product Details

Upon clicking on specific product, user is direct to the product details page. In this page the product will display a larger image, product name, price, rating, description, and option to add a quantity of the product to the shopping bag. Depending on the user status, where shoppers have the option to add product to their wishlist, while store owners also have the buttons to edit or delete product as well.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Product details|shopper|viewing product details page as a shopper|![product-details-shopper](/documentation/features/product_details_shopper.png)
Product details|store owner|viewing product details page as store owner, where it displays the buttons to either edit or delete products|![product-details-store-owner](/documentation/features/product_details_store_owner.png)

### Product Management

Available for store owner (or user admins) only, in this page products can be added to the shop including product name, price, rating, description and image. This complements the store management alongside buttons edit and delete previously mentioned, when clicking on edit button, store owner is lead to this page.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Product add|store owner|add product to the shop|![product-management-add](/documentation/features/product_management.png)
Product edit|store owner|edit product currently in the shop|![product-management-add](/documentation/features/product_management_edit.png)

### Wishlist

Logged in shoppers should have access to the wishlist page, where they an view all products added to their wishlist. In this page shoppers can view quantity of item in their wishlist and each product displayed following same layout as products page.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Wishlist|logged in shopper|view products in wishlist for logged in shoppers|![wishlist-page](/documentation/features/wishlist.png)

### Bag

This page allows shoppers to view all products in their shopping bag before completing a purchase. When the product is added to their shopping bag, from product details page, an alert banner will be displayed indicating item has been added and shoppers can go straight away to the bag page. Once in the bag page, users can view items, update quantities or remove them entirely before going to secure checkout.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Product details|shoppers (logged in or not)|when product is added to the bag, an alert message pops-up|![product-details-bag](/documentation/features/product_details_bag.png)
Bag|shoppers (logged in or not)|where shopper can view details of their shopping bag|![bag](/documentation/features/bag.png)

### Checkout

The checkout page allows shoppers to fill out their details, delivery and payment info. The payment is securely processed by Stripe API. After the checkout is complete, shopper will directed to a confirmation page with order details and a confirmation email is sent to the order email. If the shopper is not logged in, they order details will not be saved to any profile.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Checkout|shoppers (logged in or not)|where shoppers fill out details|![checkout](/documentation/features/checkout.png)
Checkout success|shoppers (logged in or not)|order confirmation details|![order-confirmation](/documentation/features/order_confirmation.png)
Email inbox|shoppers (logged in or not)|received confirmation email|![confirmation-email](/documentation/features/confirmation_email.png)

### Contact

In the contact page, shoppers and general users can easily get in touch with the shop by filling required contact fields. Once the message is submitted the sender gets an instant confirmation page and also an email with received message content and confirming the team will contact soon. This feature aims to improve overall customer satisfaction by facilitating feedback and problem solving.

**PAGE**|**USER**|**DETAILS**|**SCREENSHOT**
----------|----------|----------|----------
Contact|shoppers (logged in or not) and users in general|where all users and customer can easily get in touch with store|![contact](/documentation/features/contact.png)
Contact success|shoppers (logged in or not) and users in general|confirms message has been received|![contact](/documentation/features/contact_message_received.png)
Email inbox|shoppers (logged in or not) and users in general|confirmation email sent to sender|![contact](/documentation/features/email_message_received.png)

### About

- Anonymous
![about-anonymous](/documentation/features/about.png)

- Superuser
![about-superuser](/documentation/features/about_superuser.png)

[Back to top](#wexford--berries "Back to top")

## User Stories and Agile

### User Stories

#### Viewing and Navigation

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
shopper|view a list of products|I can select items to purchase
shopper|view product details|identify price, description, product rating and product image
shopper|easily view the total of my purchases at any time|avoid spending too much

#### Registration and User Accounts

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
site user|easily register for an account|have a personal account and be able to view my profile
site user|easily login or logout|access my personal account information
site user|easily recover my password in case I forget it|recover access to my account
site user|receive an email confirmation after registering|verify that my account registration was successful
site user|have a personalized user profile|view my personal order history and order confirmations, and save my payment information

#### Sorting and Searching

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
shopper|sort the list of available products|easily identify the best rated and best priced products
shopper|search for a product by name or description|find a specific product l'd like to purchase
shopper|easily see what I've searched for and the number of results|quickly decide whether the product I want is available

#### Purchasing and Checkout

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
shopper|easily select quantity of a product when purchasing it|ensure I don't accidentally select the wrong product or its quantity
shopper|easily edit quantity of a product when purchasing it|add or remove number of products in my shopping bag
shopper|view items in my bag to be purchased|identify the total cost of my purchase and all items I will receive
shopper|easily enter my payment information|checkout quickly and with no hassles
shopper|feel my personal and payment information is safe and secure|confidently provide the needed information to make a purchase
shopper|view an order confirmation after checkout|verify that I haven't made any mistakes
shopper|receive an email confirmation after checking out|keep the confirmation of what I've purchased for my records

#### Admin and Store Management

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
store owner|add a product|add new items to my store
store owner|edit/update a product|change product prices, descriptions, images, and other product criteria
store owner|delete a product|remove items that are no longer for sale

#### Wishlist

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
shopper|easily have access to a wish list|add, remove and view items in my wish list for future purchases

#### Contact us

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
shopper|easily send an email to the store|contact them if I have any questions about an order, product and delivery

#### About

**AS A**|**I CAN**|**SO THAT**
----------|----------|----------
store owner|easily update the about us page|I can update about page when needed

### Agile Development

Agile methodology applied considering available time to build project, where many features such as Reviews haven't been implemented yet. Users stories can be found in the Kanban board.

Kanban board available [here](https://github.com/users/jpgenari/projects/9/views/1).

[Back to top](#wexford--berries "Back to top")

## ENTITY RELATIONSHIP DIAGRAM

The Entity Relationship Diagram (ERD) for the Django project's created apps was generated using Graphviz. This visualization specifically represents the relationships and entities within the defined apps, providing a comprehensive overview of the data structure in the project.

  ![entity relationship diagram screenshot generated by Graphviz](/documentation/wexford_berries_erd.png)

[Back to top](#katask--manager "Back to top")

## Marketing Strategies for Wexford Berries

### Overview
Wexford Berries aims to connect directly with consumers who value fresh, high-quality berries. To achieve this, our marketing strategy focuses on building a strong online presence, engaging with our target audience through various digital channels, and leveraging the power of social media.

### Key Marketing Strategies

  1. **Social Media Engagement:**
    - **Facebook Page:** Create and maintain an active Facebook page where we share updates, promotions, and engaging content such as recipes, health benefits of berries, and behind-the-scenes looks at our farms. Encourage customer interactions through comments, reviews, and sharing user-generated content.

  2. **Content Marketing:**
    - Develop a blog on our website featuring articles on berry-related topics such as nutritional benefits, seasonal recipes, and tips for storing and using fresh berries. Share these posts across social media platforms to drive traffic to our site.

  3. **Email Marketing:**
    - Build a mailing list to send regular newsletters with exclusive offers, new product announcements, and personalized recommendations. Include visually appealing content and incentives for subscribers to make repeat purchases.

  4. **SEO and Paid Advertising:**
    - Optimize our website with targeted keywords and meta tags to improve search engine rankings and increase organic traffic. Implement Google Ads and Facebook Ads to target potential customers based on their interests and online behavior.

  5. **Influencer Partnerships (Future Strategy):**
    - Plan to collaborate with food bloggers, health influencers, and chefs to create sponsored content that showcases the versatility and quality of Wexford Berries. These partnerships can include recipe creations, unboxing videos, and social media takeovers.

### Meta Tags for SEO
```html
  <meta name="keywords" content="berries, strawberry, blueberry, blackberry, fresh fruits, wexford, healthy food, farmed in ireland, desserts, baking at home">
  ```

### Facebook Page

[Wexford Berries Page](https://www.facebook.com/people/Wexford-Berries/61560089931918/)

![Facebook Page](/documentation/facebook.png)

### Newsletter
Using integration with [Mailchimp](https://mailchimp.com/?currency=EUR).

#### Newsletter on footer
![Newsletter](/documentation/newsletter.png)

#### Mailchimp audience
![Mailchimp](/documentation/mailchimp.png)

[Back to top](#wexford--berries "Back to top")

## Validating and Testing

### HTML - W3C Validator

No errors flagged when testing on [W3C](https://validator.w3.org/nu/) with option checking by address, only few warnings flagged. Screenshots below displaying code from each file tested:

**PAGE**|**SCREENSHOT**
----------|----------
[Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2F)|![W3C validation screenshot homepage](/documentation/w3c_html/w3c-html-home.png)
[Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Faccounts%2Flogin%2F)|![W3C validation screenshot login page](/documentation/w3c_html/w3c-html-login.png)
[Register](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Faccounts%2Fsignup%2F)|![W3C validation screenshot sign up page](/documentation/w3c_html/w3c-html-signup.png)
[Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Faccounts%2Flogout%2F)|![W3C validation screenshot logout page](/documentation/w3c_html/w3c-html-logout.png)
[Verify Email](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Faccounts%2Fconfirm-email%2F)|![W3C validation screenshot verify email page](/documentation/w3c_html/w3c-html-email-verify.png)
[Email Confirmation](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Faccounts%2Fconfirm-email%2FMTY%3A1sOcHm%3AcB18SOlxDhrSrwiVYeJEXqJl9lkUY-pdrw1uqX55Njw%2F)|![W3C validation screenshot email confirmation page](/documentation/w3c_html/w3c-html-email-confirm.png)
[Password Reset](https://wexford-berries-229479cc7505.herokuapp.com/accounts/password/reset/)|![W3C validation screenshot password reset page](/documentation/w3c_html/w3c-html-password-reset.png)
[Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fproducts%2F)|![W3C validation screenshot products page](/documentation/w3c_html/w3c-html-products.png)
[Add Product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fproducts%2Fadd%2F)|![W3C validation screenshot add product page](/documentation/w3c_html/w3c-html-add-product.png)
[Edit Product](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fproducts%2Fedit%2F13%2F)|![W3C validation screenshot edit product page](/documentation/w3c_html/w3c-html-edit-product.png)
[Wishlist](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fwishlist%2F)|![W3C validation screenshot wishlist page](/documentation/w3c_html/w3c-html-wishlist.png)
[Bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fbag%2F)|![W3C validation screenshot bag page](/documentation/w3c_html/w3c-html-bag.png)
[Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fcheckout%2F)|![W3C validation screenshot checkout page](/documentation/w3c_html/w3c-html-checkout.png)
[Profile](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fprofile%2F)|![W3C validation screenshot profile page](/documentation/w3c_html/w3c-html-profile.png)
Order Details|![W3C validation screenshot order details page](/documentation/w3c_html/w3c-html-order-details.png)
[Contact](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fcontact%2F)|![W3C validation screenshot contact page](/documentation/w3c_html/w3c-html-contact.png)
[About](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fabout%2F)|![W3C validation screenshot about page](/documentation/w3c_html/w3c-html-about.png)
[Edit About](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fabout%2Fedit%2F)|![W3C validation screenshot edit about page](/documentation/w3c_html/w3c-html-edit-about.png)
[Privacy Policy](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwexford-berries-229479cc7505.herokuapp.com%2Fpolicies%2Fprivacy%2F)|![W3C validation screenshot privacy policy page](/documentation/w3c_html/w3c-html-privacy.png)

[Back to top](#wexford--berries "Back to top")

### CSS - Jigsaw W3C Validator

No errors flagged when testing on [Jigsaw W3C](https://jigsaw.w3.org/css-validator/) by direct input, only warnings - mostly 'vendor extension'. Screenshots below displaying code from each file tested:

**FILE**|**SCREENSHOT**
----------|----------
[/.../checkout.css](https://github.com/jpgenari/wexford_berries/blob/main/checkout/static/checkout/css/checkout.css)|![jigsaw css validation screenshot checkout.css](/documentation/w3c_css/css-checkout.png)
[/.../profiles.css](https://github.com/jpgenari/wexford_berries/blob/main/profiles/static/profiles/css/profile.css)|![jigsaw css validation screenshot profiles.css](/documentation/w3c_css/css-profiles.png)
[/.../base.css](https://github.com/jpgenari/wexford_berries/blob/main/static/css/base.css)|![jigsaw css validation screenshot base.css](/documentation/w3c_css/css-base.png)

[Back to top](#wexford--berries "Back to top")

### JavaScript - JS Hint

No errors flagged when testing on [JS Hint](https://jshint.com/), only warnings flagged. Screenshots below displaying code from each file tested:

**FILE**|**SCREENSHOT**
----------|----------
[/.../add_product.html](https://github.com/jpgenari/wexford_berries/blob/main/products/templates/products/add_product.html)|![JS Hint validation screenshot add_product.html](/documentation/jshint/edit_add_product.html.png)
[/.../bag.html](https://github.com/jpgenari/wexford_berries/blob/main/bag/templates/bag/bag.html)|![JS Hint validation screenshot bag.html](/documentation/jshint/bag.html.png)
[/.../base.html](https://github.com/jpgenari/wexford_berries/blob/main/templates/base.html)|![JS Hint validation screenshot base.html](/documentation/jshint/base.html.png)
[/.../checkout.html](https://github.com/jpgenari/wexford_berries/blob/main/checkout/templates/checkout/checkout.html)|![JS Hint validation screenshot checkout.html](/documentation/jshint/checkout.html.png)
[/.../countryfield.js](https://github.com/jpgenari/wexford_berries/blob/main/profiles/static/profiles/js/countryfield.js)|![JS Hint validation screenshot countryfield.js](/documentation/jshint/profiles_countryfield.js.png)
[/.../custom_quantity_imput_script.html](https://github.com/jpgenari/wexford_berries/blob/main/products/templates/products/custom_widget_templates/custom_clearable_file_input.html)|![JS Hint validation screenshot custom_clearable_file_input.html](/documentation/jshint/products_quantity_imput_script.html.png)
[/.../edit_product.html](https://github.com/jpgenari/wexford_berries/blob/main/products/templates/products/edit_product.html)|![JS Hint validation screenshot edit_product.html](/documentation/jshint/edit_add_product.html.png)
[/.../products.html](https://github.com/jpgenari/wexford_berries/blob/main/products/templates/products/products.html)|![JS Hint validation screenshot products.html](/documentation/jshint/products.html.png)
[/.../stripe_elements.js](https://github.com/jpgenari/wexford_berries/blob/main/checkout/static/checkout/js/stripe_elements.js)|![JS Hint validation screenshot stripe_elements.js](/documentation/jshint/stripe_elements.js.png)
[/.../wishlist.html](https://github.com/jpgenari/wexford_berries/blob/main/wishlist/templates/wishlist/wishlist.html)|![JS Hint validation screenshot wishlist.html](/documentation/jshint/wishlist.html.png)

[Back to top](#wexford--berries "Back to top")

### Python and Django - CI Python Linter

No errors flagged when testing on [CI Python Linter](https://pep8ci.herokuapp.com/). Screenshots below displaying code from each file tested:

**APP**|**FILE**|**SCREENSHOT**
----------|----------|----------
about|[admin.py](https://github.com/jpgenari/wexford_berries/blob/main/about/admin.py)|![Python Linter validation screenshot /about/admin.py](/documentation/python_linter/about_admin.png)
about|[forms.py](https://github.com/jpgenari/wexford_berries/blob/main/about/forms.py)|![Python Linter validation screenshot /about/forms.py](/documentation/python_linter/about_forms.png)
about|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/about/models.py)|![Python Linter validation screenshot /about/models.py](/documentation/python_linter/about_models.png)
about|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/about/urls.py)|![Python Linter validation screenshot /about/urls.py](/documentation/python_linter/about_urls.png)
about|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/about/views.py)|![Python Linter validation screenshot /about/views.py](/documentation/python_linter/about_views.png)
bag|[contexts.py](https://github.com/jpgenari/wexford_berries/blob/main/bag/contexts.py)|![Python Linter validation screenshot /bag/contexts.py](/documentation/python_linter/bag_contexts.png)
bag|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/bag/urls.py)|![Python Linter validation screenshot /bag/urls.py](/documentation/python_linter/bag_urls.png)
bag|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/bag/views.py)|![Python Linter validation screenshot /bag/views.py](/documentation/python_linter/bag_views.png)
checkout|[admin.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/admin.py)|![Python Linter validation screenshot /checkout/admin.py](/documentation/python_linter/checkout_admin.png)
checkout|[forms.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/forms.py)|![Python Linter validation screenshot /checkout/forms.py](/documentation/python_linter/checkout_forms.png)
checkout|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/models.py)|![Python Linter validation screenshot /checkout/models.py](/documentation/python_linter/checkout_models.png)
checkout|[signals.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/signals.py)|![Python Linter validation screenshot /checkout/signals.py](/documentation/python_linter/checkout_signals.png)
checkout|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/urls.py)|![Python Linter validation screenshot /checkout/urls.py](/documentation/python_linter/checkout_urls.png)
checkout|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/views.py)|![Python Linter validation screenshot /checkout/views.py](/documentation/python_linter/checkout_views.png)
checkout|[webhooks.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/webhooks.py)|![Python Linter validation screenshot /checkout/webhooks.py](/documentation/python_linter/checkout_webhooks.png)
checkout|[webhook_handler.py](https://github.com/jpgenari/wexford_berries/blob/main/checkout/webhook_handler.py)|![Python Linter validation screenshot /checkout/webhook_handler.py](/documentation/python_linter/checkout_webhooks_handler.png)
contact|[admin.py](https://github.com/jpgenari/wexford_berries/blob/main/contact/admin.py)|![Python Linter validation screenshot /contact/admin.py](/documentation/python_linter/contact_admin.png)
contact|[forms.py](https://github.com/jpgenari/wexford_berries/blob/main/contact/forms.py)|![Python Linter validation screenshot /contact/forms.py](/documentation/python_linter/contact_forms.png)
contact|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/contact/models.py)|![Python Linter validation screenshot /contact/models.py](/documentation/python_linter/contact_models.png)
contact|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/contact/urls.py)|![Python Linter validation screenshot /contact/urls.py](/documentation/python_linter/contact_urls.png)
contact|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/contact/views.py)|![Python Linter validation screenshot /contact/views.py](/documentation/python_linter/contact_views.png)
home|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/home/urls.py)|![Python Linter validation screenshot /home/urls.py](/documentation/python_linter/home_urls.png)
home|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/home/views.py)|![Python Linter validation screenshot /home/views.py](/documentation/python_linter/home_views.png)
products|[admin.py](https://github.com/jpgenari/wexford_berries/blob/main/products/admin.py)|![Python Linter validation screenshot /products/views.py](/documentation/python_linter/products_admin.png)
products|[forms.py](https://github.com/jpgenari/wexford_berries/blob/main/products/forms.py)|![Python Linter validation screenshot /products/forms.py](/documentation/python_linter/products_forms.png)
products|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/products/models.py)|![Python Linter validation screenshot /products/models.py](/documentation/python_linter/products_models.png)
products|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/products/urls.py)|![Python Linter validation screenshot /products/urls.py](/documentation/python_linter/products_urls.png)
products|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/products/views.py)|![Python Linter validation screenshot /products/views.py](/documentation/python_linter/products_views.png)
products|[widgets.py](https://github.com/jpgenari/wexford_berries/blob/main/products/widgets.py)|![Python Linter validation screenshot /products/widgets.py](/documentation/python_linter/products_widgets.png)
profiles|[forms.py](https://github.com/jpgenari/wexford_berries/blob/main/profiles/forms.py)|![Python Linter validation screenshot /profiles/forms.py](/documentation/python_linter/profiles_forms.png)
profiles|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/profiles/models.py)|![Python Linter validation screenshot /profiles/models.py](/documentation/python_linter/profiles_models.png)
profiles|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/profiles/urls.py)|![Python Linter validation screenshot /profiles/urls.py](/documentation/python_linter/profiles_urls.png)
profiles|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/profiles/views.py)|![Python Linter validation screenshot /profiles/views.py](/documentation/python_linter/profiles_views.png)
wexford_berries|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/wexford_berries/urls.py)|![Python Linter validation screenshot /wexford_berries/urls.py](/documentation/python_linter/main_urls.png)
wexford_berries|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/wexford_berries/views.py)|![Python Linter validation screenshot /wexford_berries/views.py](/documentation/python_linter/main_views.png)
wishlist|[admin.py](https://github.com/jpgenari/wexford_berries/blob/main/wishlist/admin.py)|![Python Linter validation screenshot /wishlist/admin.py](/documentation/python_linter/wishlist_admin.png)
wishlist|[models.py](https://github.com/jpgenari/wexford_berries/blob/main/wishlist/models.py)|![Python Linter validation screenshot /wishlist/models.py](/documentation/python_linter/wishlist_models.png)
wishlist|[urls.py](https://github.com/jpgenari/wexford_berries/blob/main/wishlist/urls.py)|![Python Linter validation screenshot /wishlist/urls.py](/documentation/python_linter/wishlist_urls.png)
wishlist|[views.py](https://github.com/jpgenari/wexford_berries/blob/main/wishlist/views.py)|![Python Linter validation screenshot /wishlist/views.py](/documentation/python_linter/wishlist_views.png)

[Back to top](#wexford--berries "Back to top")

### Performance - Google Lighthouse

No performance issues flagged when running Google Chrome Lighthouse, only warnings. Screenshots below displaying code from each file tested:

**PAGE**|**VERSION**|**SCREENSHOT**
----------|----------|----------
Home|Desktop|![Lighthouse validation screenshot home page on desktop](/documentation/performance_lighthouse/home_desktop.png)
Home|Mobile|![Lighthouse validation screenshot home page on mobile](/documentation/performance_lighthouse/home_mobile.png)
Products|Desktop|![Lighthouse validation screenshot products page on desktop](/documentation/performance_lighthouse/products_desktop.png)
Products|Mobile|![Lighthouse validation screenshot home products on mobile](/documentation/performance_lighthouse/products_mobile.png)

### Manual Testing

Manual testing following user stories and fully reproducing site user and site admin journey throughout application use. Tests carried over on Google Chrome, Mozilla Firefox, Safari on MacOS system, and mobile testing carried over throughout Google Chrome inspect tool.

**TEST**|**USER**|**EXPECTED**|**RESULT**
----------|----------|----------|----------
Viewing and navigation|shopper|view products and select items to purchase|pass
|||view product details, price, description, rating, image and size|pass
Registration and user accounts|site user|register/sign up an account|pass
|||login and logout easily|pass
|||recover lost password|pass
|||receive a registration confirmation email|pass
|||access personalized user profile displaying personal info and orders history|pass
Sorting and searching|shopper|sort list of available products by price and best rated|pass
|||sort list of available products by price and best rated|pass
|||search for products by name or description|pass
|||view search results and select items to purchase|pass
Purchasing and checkout|shopper|select quantity of an item when purchasing|pass
|||select quantity of an item in the shopping bag or remove it|pass
|||view shopping bag with all selected items inside|pass
|||enter payment info|pass
|||have a payment method that brings safe|pass
|||view an order confirmation after checkout is complete|pass
|||receive and email with order confirmation after checkout is complete|pass
Admin and store management|store owner|add a product to the shop when logged as admin|pass
|||edit a product details in the shop when logged as admin|pass
|||delete a product from the shop when logged as admin|pass
Wishlist|shopper|easily add and remove items from wishlist from product details page|pass
|||view wishlist with all items added to decide what to buy|pass
Contact|shopper|easily contact shop through a form and receive email confirmation my own email|pass
About page|store owner|update 'About Us' page from when logged in as admin|pass
||site user|view about us section|pass

[Back to top](#wexford--berries "Back to top")

## Deployment

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To create your Postgres Database, simply sign up with your GitHub account and follow these steps:

- Click on Create New Instance to initiate a new database.
Specify a name for your database (typically the project name, such as "wexford-berries").
- Choose the Tiny Turtle (Free) plan.
- You can opt to leave the Tags field empty.
- Select the nearest Region and Data Center.
- After creation, access your database by clicking on its name, where you'll find the database URL and Password.

### Amazon AWS
This project utilizes  [AWS](https://aws.amazon.com) for storing media and static files online, as Heroku does not retain this data type.

After creating an AWS account and logging in, navigate to the AWS Management Console page and follow these steps to connect your project.

#### S3 Bucket
- Find and select S3.
- Create a new bucket, providing a name typically matching your Heroku app name, and select the region closest to you.
- Disable "Block all public access" and acknowledge that the bucket will be public, as it's required for Heroku operation.
- Ensure ACLs are enabled and select "Bucket owner preferred" under Object Ownership.
- Navigate to the Properties tab, enable static website hosting, and input "index.html" and "error.html" in their respective fields. Save your changes.
- Move to the Permissions tab and paste the following CORS configuration:
```
[
 {
  "AllowedHeaders": [
   "Authorization"
  ],
  "AllowedMethods": [
   "GET"
  ],
  "AllowedOrigins": [
   "*"
  ],
  "ExposeHeaders": []
 }
]
```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:

- Policy Type: **S3 Bucket Policy**
  - Effect: **Allow**
  - Principal: `*`
  - Actions: **GetObject**
  - Amazon Resource Name (ARN): **paste-your-ARN-here**
  - Click **Add Statement**
  - Click **Generate Policy**
  - Copy the entire Policy, and paste it into the **Bucket Policy Editor**

```
{
 "Id": "Policy1234567890",
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "Stmt1234567890",
   "Action": [
    "s3:GetObject"
   ],
   "Effect": "Allow",
   "Resource": "arn:aws:s3:::your-bucket-name/*"
   "Principal": "*",
  }
 ]
}
```
Before you click "Save", add /* to the end of the Resource key in the Bucket Policy Editor (as shown above).
- Click Save.
#### IAM

- Navigate to IAM by searching for it on the AWS Services Menu. Once on the IAM page, proceed with the following steps:

- Under User Groups, click on Create New Group.
- Suggested Name: wexford-berries-manage (the group name combined with the project name)
- Tags are optional but must be clicked to access the review policy page.
- Select the newly created group from User Groups and move to the Permissions tab.
- Click on the Add Permissions dropdown and select Attach Policies.
- Choose the desired policy and click Add Permissions at the bottom to finish.
- Under the JSON tab, select the Import Managed Policy link.
```
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Action": "s3:*",
   "Resource": [
    "arn:aws:s3:::your-bucket-name",
    "arn:aws:s3:::your-bucket-name/*"
   ]
  }
 ]
}
```
- Click on Review Policy.
  - Suggested Name: policy-wexford-berries (policy combined with the project name)
   - Provide a description: "Access to S3 Bucket for wexford-berries static files."
   - Click Create Policy.
- Under User Groups, select your "group-wexford-berries".
- Click Attach Policy.
- Search for the policy you've just created ("policy-wexford-berries"), select it, then Attach Policy.
- Under User Groups, click Add User.
- Suggested Name: user-wexford-berries (user combined with the project name)
  - For "Select AWS Access Type," choose Programmatic Access.
  - Select the group to add your new user to: group-wexford-berries.
  - Tags are optional, but click it to access the review user page.
  - Click Create User once done.
- You should see a button to Download .csv, so click it to save a copy on your system.
***IMPORTANT: Once you pass this page, you cannot come back to download it again, so do it immediately!***
- This contains the user's Access key ID and Secret access key.
  - AWS_ACCESS_KEY_ID = Access key ID
  - AWS_SECRET_ACCESS_KEY = Secret access key.

#### Set up AWS

- If DISABLE_COLLECTSTATIC is still present in Heroku Config Vars, it can now be removed to allow AWS to handle static files.
- In the S3 dashboard, create a new folder named: media.
- Choose existing media images for your project to prepare them for upload into the new folder.
- Under Manage Public Permissions, select Grant public read access to this object(s)
- No further settings are required, so click Upload.

### Stripe API

This project utilizes [Stripe](https://stripe.com) to handle the ecommerce payments.
To integrate your project with Stripe, follow these steps:

- Navigate to your Stripe dashboard and expand "Get your test API keys".
Here you'll find two keys:
   - STRIPE_PUBLIC_KEY = Publishable Key (starts with pk)
  - STRIPE_SECRET_KEY = Secret Key (starts with sk)
As a backup in case users close the purchase-order page during payment, Stripe Webhooks can be included.

- In your Stripe dashboard, go to Developers, then select Webhooks.
- Click Add Endpoint.
- Use the endpoint: https://wexford-berries-229479cc7505.herokuapp.com/checkout/wh/
- Select receive all events.
- Click Add Endpoint to complete the process.
- You'll receive a new key:
   -STRIPE_WH_SECRET = Signing Secret (Webhook) Key (starts with wh)

### Gmail API
This project utilizes [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.
To integrate your project with Gmail, follow these steps:

- Click on the Account Settings (cog icon) in the top-right corner of Gmail.
Go to the Accounts and Import tab.
- Under "Change account settings", select Other Google Account settings.
- On the new page, choose Security from the left sidebar.
- Turn on 2-Step Verification. (verify your password and account)
- After verification, turn on 2FA.
- Return to the Security page and find App passwords.
- Confirm your password and account again if prompted.
- Select Mail for the app type.
- Choose Other (Custom name) for the device type.
- Use any custom name, like "Django" or "wexfordberries"
- You'll receive a 16-character password (API key).
- Save this securely, as it can't be accessed later!
  - EMAIL_HOST_PASS = user's 16-character API key
  - EMAIL_HOST_USER = user's personal Gmail email address

### Heroku


This project utilizes [Heroku](https://www.heroku.com), a platform as a service (PaaS) that empowers developers to build, run, and manage applications entirely in the cloud.
Follow these deployment steps after setting up your account:

- Navigate to your Heroku Dashboard and click New in the top-right corner, then select Create new app.
- Choose a unique app name, select a region (EU or USA), and click Create App.
- In the app's Settings, click Reveal Config Vars, and set the following environment variables:

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| **AWS_ACCESS_KEY_ID**     | user's own value                                                     |
| **AWS_SECRET_ACCESS_KEY** | user's own value                                                     |
| **DATABASE_URL**          | user's own value                                                     |
| **DISABLE_COLLECTSTATIC** | 1 (_this is temporary, and can be removed for the final deployment_) |
| **EMAIL_HOST_PASS**       | user's own value                                                     |
| **EMAIL_HOST_USER**       | user's own value                                                     |
| **SECRET_KEY**            | user's own value                                                     |
| **STRIPE_PUBLIC_KEY**     | user's own value                                                     |
| **STRIPE_SECRET_KEY**     | user's own value                                                     |
| **STRIPE_WH_SECRET**      | user's own value                                                     |
| **USE_AWS**               | True                                                                 |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- pip3 install -r requirements.txt

If you have your own packages that have been installed, then the requirements file needs updated using:

- pip3 freeze --local > requirements.txt

The **Procfile** can be created with the following command:

- echo web: gunicorn app_name.wsgi > Procfile
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a app_name (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - git push heroku main

Your project is now successfully connected and deployed on Heroku!

### Cloning Project

A local clone of this repository can be made on GitHub. Please follow the below steps:

- Navigate to GitHub and log in.
- The [Wexford Berries Repository](https://github.com/jpgenari/wexford_berries) can be found at this location.
- Above the repository file section, locate the 'Code' button.
- Click on this button and choose your clone method from HTTPS, SSH, or GitHub CLI, copy the URL to your clipboard by clicking the 'Copy' button.
- Open your Git Bash Terminal.
- Change the current working directory to the location you want the cloned directory to be made.
- Type git clone and paste in the copied URL from the step above.
- Press 'Enter' for the local clone to be created.
- Use the **pip3 install -r requirements.txt** command to install the dependencies and libraries needed for Wexford Berries.
- Set up your env.py file and gather the PostgreSQL URL from ElephantSQL, if applicable, and add your SECRET_KEY and STRIPE/AWS keys if using these services.
- Ensure that your env.py file is placed in your .gitignore file and follow the remaining steps in the Django Project Setup section before pushing your code to GitHub.

### Forking Project

You can create a copy of the original repository on GitHub by following these steps:

- Log in to GitHub.
- Visit the [Wexford Berries Repository](https://github.com/jpgenari/wexford_berries).
- Click the 'Fork' button at the top right of the repository page to make a copy in your own GitHub account.

You will now have a forked version of the repository in your GitHub account. 

[Back to top](#wexford--berries "Back to top")

## Tecnologies Used
### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks and Libraries

- Django
- Bootstrap
- jQuery
- Stripe

### Development and Deploy

- Heroku
- Git
- GitHub
- VsCode

## CREDITS

### Content

  - Core App structure and code inspired/taken from [Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546).
  - Some pieces inspired/taken from walkthrough project [Codestar Blog](https://github.com/Code-Institute-Solutions/blog/tree/main).
  - READme  structure and content and code inspired/taken from other Code Institute P5 projects: [Fungi Fantasy](https://github.com/Bruna-Andelieri/FungiFantasy?tab=readme-ov-file#marketing-and-seo), [Sleep Healthily](https://github.com/stephendawsondev/Sleep-Healthily) and [ShinyGarageMalta](https://github.com/GDV373/PP5_Shiny_Garage_Malta-).
  - Debugging and refactoring performed with support of [ChatGPT](https://chat.openai.com/).
  - All eCommerce photos and part of content generated by [Microsoft CoPilot](https://copilot.microsoft.com/).
  - Privacy policy generated by [TermsFeed](https://app.termsfeed.com/).

### Acknowledgement

 - A special thanks to my cohort, Amy Richardson, for her outstanding support and patience. Support for not keep pushing me and patience when I was complaining at 23:30 or even later.

 - A big thank you to Bruna Andelieri a friend I made throughout this corse and has been helping immensely - and extend my gratitude to her partner Ivan, how also help me.

 - A sincere appreciation to my wife, Ana, for her unwavering support and understanding. She didn't let me give up, even during the most challenging moments of coding. I'm deeply grateful for her constant presence and encouragement.

 [Back to top](#wexford--berries "Back to top")