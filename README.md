# Wexford | Verries

Wexford Berries is a leading B2C e-commerce platform, offering a wide selection of the freshest and highest quality berries directly to your doorstep. We pride ourselves on sourcing our berries from trusted local farms, ensuring every order is packed with flavor and nutrients. With our easy-to-navigate online store, customers can choose from a variety of berries, including strawberries, blueberries, raspberries, and more. Enjoy the convenience of farm-fresh deliveries and taste the difference with Wexford Berries—where premium quality meets unbeatable freshness.

Link to the live web app: [Wexford | Berries](https://wexford-berries-229479cc7505.herokuapp.com/)

## User Stories and Agile

### User Stories

Agile methodology applied considering available time to build project, where many features such as Reviews haven't been implemented yet. Users stories can be found in the Kanban board.

Kanban board available [here](https://github.com/users/jpgenari/projects/9/views/1).

[Back to top](#wexford-berries "Back to top")


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

## Validating and Testing

### HTML - W3C Validator

No errors flagged by [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fkatask-9e69d33c7144.herokuapp.com%2Fhome).

### CSS - Jigsaw W3C Validator

No errors flagged on [Jigsaw W3C](https://jigsaw.w3.org/css-validator/)
![jigsaw css validation screenshot](/documentation/W3C_validator.png)

### JavaScript - JS Hint

No errors flagged on [JS Hint](https://jshint.com/). All JavaScript texts screenshots can be found in [jshnt](https://github.com/jpgenari/wexford_berries/tree/main/documentation/jshint) with naming containing where the code is.

  - Only few warnings flagged.

### Python and Django - CI Python Linter

No errors flagged on [CI Python Linter](https://pep8ci.herokuapp.com/). All Python Linter screenshots can be found in the folder [python_linter](https://github.com/jpgenari/wexford_berries/tree/main/documentation/python_linter) with naming containing **app_file**.

### Performance - Google Lighthouse

No performance issues flagged when running Google Chrome Lighthouse, only warnings. Screenshot stored in the folder [performance_lighthouse](https://github.com/jpgenari/wexford_berries/tree/main/documentation/performance_lighthouse) with naming corresponding with the placed tested.

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

## CREDITS

### Content

  - Core App structure and code inspired/taken from [Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546).
  - Some pieces inspired/taken from walkthrough project [Codestar Blog](https://github.com/Code-Institute-Solutions/blog/tree/main).
  - READme  structure and content and code inspired/taken from other Code Institute P5 projects: [Fungi Fantasy](https://github.com/Bruna-Andelieri/FungiFantasy?tab=readme-ov-file#marketing-and-seo), [Sleep Healthily](https://github.com/stephendawsondev/Sleep-Healthily) and [ShinyGarageMalta](https://github.com/GDV373/PP5_Shiny_Garage_Malta-).
  - Debugging and refactoring performed with support of [ChatGPT](https://chat.openai.com/).
  - All eCommerce photos and part of content generated by [Microsoft CoPilot](https://copilot.microsoft.com/).
  - Privacy policy generated by [TermsFeed](https://app.termsfeed.com/).

### Acknowledgement

- A special thanks to my mentor, [Chris Quin](https://github.com/10xOXR), for his outstanding support and patience during the development process. Chris, your encouragement kept me going, and your guidance was crucial to the project's success. I appreciate your unwavering commitment and expertise.

 - A big thank you to my wife, Ana, for her unwavering support and understanding. She, along with Chris, has been instrumental in keeping me motivated and preventing me from giving up, despite the long hours spent coding. Grateful for her constant presence and encouragement.