# [WEB PIANO ACADEMY](https://web-piano-academy-16cd779294ab.herokuapp.com)


![screenshot](documentation/mockup.png)

Web Piano Academy is a fully functioning e-commerce web application. The site allows users to view and purchase digital piano courses online. Users can easily create personal accounts and profiles and see information on the site, and the courses themselves. The site also enables administrators to add, edit and remove products, as well as view and respond to contact enquiries.

## UX

The design philosophy was to create a fun, engaging look, while keeping relevant information presented in a salient and clean manner, allowing the user to easily and pleasingly navigate through the site.

### Colour Scheme


I used [coolors.co](https://coolors.co/2c6967-f8ddd0-e67e7c-ed8500-000000-ffffff) to generate my colour palette.

![screenshot](documentation/coolors.png)

### Typography

- [DM Sans](https://fonts.google.com/specimen/DM+Sans) was used for the primary headers and titles and text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site.

## User Stories

All user stories can be found in a linked GitHub project [here](https://github.com/users/LewisMDillon/projects/5)


## Features

### Existing Features

### Site Pages

- **Homepage**

    - The main homepage for the site. Hero image is large and striking. Large heading tells users they are in the right place. Call to action button to invite users to enter and explore the site products.

![screenshot](documentation/features/sitepages/home.png)

- **Courses Page**

    - Courses page. Displays the site products available for the user to purchase. Displays images of products and their essential information including title, description, price, category & level. Courses are displayed in a pleasing responsive grid layout, making it easy for a user to browse the courses. Courses utilise a mouse-hover animation to add to the interactivity of the page. Courses can also be filtered and sorted by name, price and other criteria.
    Administrators viewing this page can see links under each course to edit or delete the course.

![screenshot](documentation/features/sitepages/courses.png)

- **About Page**

    - About page. Gives users essential information about Web Piano Academy. Text content interspersed with pictures helps to break up the page and keep the user engaged with the presented information. 

![screenshot](documentation/features/sitepages/about.png)

- **FAQ Page**

    - FAQ Page. Displays the most frequently asked questions about the site. Lets users know essential information and quells worries that they may have about the site and its products. Animation and accordion serve to make the information engaging and clean.

![screenshot](documentation/features/sitepages/faq.png)

- **Contact Page**

    - Contact Page. Users can contact the site owner using the contact form. If the user is logged in, their email is pre-filled in the email input field. Users can choose from a selection of subjects and leave their message via the text box. 

![screenshot](documentation/features/sitepages/contact.png)

- **Contact Success Page**

    - Contact Success Page. Users see this page after sending a contact message via the contact page. This page serves to confirm to the user that their message has been sent successfully. A short message informs the user that their contact message has been received, and that one of the team will respond as soon as possible.

![screenshot](documentation/features/sitepages/contact-success.png)

- **Contact Requests Page - Admin Only**

    - Contact Requests Page. Admins can see a list of all of the contact messages sent by users. Messages are displayed in an easy-to-read table, with all of the salient information presented. Messages are automatically sorted with those messages which have not been responded to at the top of the list, with the oldest (the message which has gone unanswered the longest) at the top. Admins can click on the view details links to see the full contact messages, as well as respond to the message.

![screenshot](documentation/features/sitepages/contact-requests.png)

- **Contact Details Page - Admin Only**

    - Contact Details Page. Admins can see details of a contact message left by the user. All of the contact message's information can be seen, including email, name, subject, message, and whether this contact message has been respond to. Contact messages can be responded to or deleted via the large buttons at the bottom of the page. A link navigates back to the contact requests page.

![screenshot](documentation/features/sitepages/contact-details.png)

- **Contact Delete Page - Delete - Admin Only**

    - Contact Message Delete Page. An admin sees this page after clicking the delete message button on the Contact Details Page. This page double checks that deletion of the contact message is the intended course of action and allows an admin to either confirm the action or return to the contact message's detail page.

![screenshot](documentation/features/sitepages/contact-delete.png)

- **Signup Page**

    - Signup Page. Displays a signup form that new users can use to register an account on the site. Simple input fields for email, username and password make it easy for users to sign up for an account, an confirmation inputs insure that users do not accidentally register with incorrect information. A sign in link at the top of the page lets users who already have an account easily find the login page.

![screenshot](documentation/features/sitepages/signup.png)

- **Login Page**

    - Login Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in to their account. A 'remember me' checkbox allows users to choose to have their login information stored for faster login in future. A Forgot Password link takes users to another page where they can recover their password. A sign up link at the top of the page lets users who do not yet have an account easily find the register page.

![screenshot](documentation/features/sitepages/login.png)

- **Logout Page**

    - Logout Page. Displays a logout confirmation message with two buttons allowing the user to confirm the action and logout, or to return to the previous page and stay logged in.

![screenshot](documentation/features/sitepages/logout.png)

- **Profile Page**

    - Profile page. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an update form that users can use to update their profile information. Users can also see their order history, with full details of their order as well as links to see past order confirmations.

![screenshot](documentation/features/sitepages/profile.png)

- **Shopping Basket Page**

    - Shopping Basket page. Displays all items currently in the user's shopping basket. Users get a message if their basket is empty, otherwise they will see a list of courses that they have selected with a button to navigate to the courses page, and another to navigate to the checkout page.

![screenshot](documentation/features/sitepages/basket.png)

- **Checkout Page**

    - Checkout page. Displays an order summary of the items that are being prepared for purchase with accompanying item details. Displays a total cost of the order to the user. The user also sees a form to fill in their personal details. For logged in users, these details will be pre-filled if the user has provided that information in the past. A tooltip explains to users why their address details might be needed despite ordering a digital product. A checkbox allows users to save entered information to their profile. A payment input form exists at the bottom of the page for a user to enter their payment card information. A message below this warns the user that advancing will complete the purchase and incur a charge to their card.

![screenshot](documentation/features/sitepages/checkout1.png)
![screenshot](documentation/features/sitepages/checkout2.png)
![screenshot](documentation/features/sitepages/checkout3.png)

- **Checkout Success Page**

    - Checkout Success Page. Displays a thank you message to the user, as well as a message describing how to access their purchased course. Also displays an order summary with all the relevant information, including a unique order number beginning with WPA (for Web Piano Academy) followed by 10 random digits & letters generated by uuid.

![screenshot](documentation/features/sitepages/checkout-success.png)

- **Add Product Page - Admin Only**

    - Add Product Page. Admins can use this form to add new products to the site. User-friendly form inputs allow product objects to be created simply and quickly.

![screenshot](documentation/features/sitepages/add-product.png)

- **Edit Product Page - Admin Only**

    - Edit Product Page. Admins can use this form to add edit products to the site. User-friendly form inputs allow product objects to be edited simply and quickly. A message at the top of the page informs the admin which product they are editing.

![screenshot](documentation/features/sitepages/edit-product.png)

- **Custom Error Pages**

    - Custom error handler pages. These pages display when a user encounters one of the following common errors: 400, 403, 404, 500. These provide a more user-friendly error page than the user would see otherwise and includes an informative message and button to return home to the site. 

![screenshot](documentation/features/sitepages/400.png)
![screenshot](documentation/features/sitepages/403.png)
![screenshot](documentation/features/sitepages/404.png)
![screenshot](documentation/features/sitepages/500.png)

### User Features

- **User Registration**

    - Users can register for an account using a front-end form. This creates a user object in the database and automatically secures the user's sensitive information.

![screenshot](documentation/features/user/register.png)

- **User Login**

    - Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.

![screenshot](documentation/features/user/login.png)

- **User Logout**

    - Users who are logged in can easily log out in order to stop access to their account-based information and functionality.

![screenshot](documentation/features/user/logout.png)

- **User Password Recovery**

    - Users who have forgotten their password can recover their password via the forgot password link on the login page. Users will enter their email and get a password reset link sent to their account email which they can use to set a new password.

![screenshot](documentation/features/user/password-recover.png)

- **Toasts**

    - Users see helpful popup messages when performing actions on the site. These messages inform the user of the success or failure of their actions, as well as providing information about an action taken, or steps that the user must take in order to correct an action.

![screenshot](documentation/features/user/toast1.png)
![screenshot](documentation/features/user/toast2.png)
![screenshot](documentation/features/user/toast3.png)

- **Basket Updates**

    - Via toasts, users can see a summary of their basket whenever an item is added, allowing the user to quickly see the new state of their basket, without having to navigate away from the page they are currently on.

![screenshot](documentation/features/user/basket-update.png)


- **Login Dependant Navbar Links**

    - Users who are logged in see new links in the navbar. 'Register' and 'Login' links are replaced with 'My Account' links. This provides the user with visual feedback upon logging in, as well as removing links that they will not need.

![screenshot](documentation/features/user/login-navbar-links1.png)
![screenshot](documentation/features/user/login-navbar-links2.png)

- **Login Redirect**

    - Users who are not logged in who attempt to access an area of the site which requires login are redirected to the login page. After logging in, they are sent to the page they first intended to visit.

![screenshot](documentation/features/user/login-redirect.png)

- **User Profile Creation**

    - User profiles are automatically created upon user registration. This assigns each user a profile which they can use to see/update their user information.

![screenshot](documentation/features/user/profile-creation.png)

- **User Profile Update**

    - Users can update their profile information using a front-end form located on their user profile page. This allows users to update profile information or correct possible mistakes made at registration.

![screenshot](documentation/features/user/profile-update.png)

- **User Contact**

    - Users can use a front-end form to message the site owners. The form is easy to use and pre-fills the user's email address if they are logged in. Users get confirmation that their message was sent, and a message that someone from the site will be in touch as soon as possible

![screenshot](documentation/features/user/contact.png)


- **User Email Confirmations**

    - After making a purchase or subscribing to the newsletter, the site automatically sends the user a confirmation email which contains their purchase details, or in the case of newsletter subscription, a thank you message and a link to unsubscribe.

![screenshot](documentation/features/user/email-confirmation1.png)
![screenshot](documentation/features/user/email-confirmation2.png)

- **Course Sort**

    - Users can use a front-end dropdown box to sort the available courses by criteria such as price, name, category, and level. This allows the user to get to the relevant content more quickly, without having to manually sort through the entire product list.

![screenshot](documentation/features/user/course-sort.png)

- **Course Search**

    - Users can use a front-end dropdown to enter search criteria for the purposes of searching for courses to purchase. This allows users to instantly find courses related to their search keywords, allowing them to navigate straight to the relevant products.

![screenshot](documentation/features/user/course-search.png)

- **Newsletter Subscribe**

    - Users can use a button in the footer of all site pages to subscribe to the site newsletter. If the user is logged in, the email input field will pre-fill with the user's email. Users see a confirmation screen after subscribing, and receive a confirmation email to the address they provided.

![screenshot](documentation/features/user/newsletter1.png)
![screenshot](documentation/features/user/newsletter2.png)

- **Newsletter Unsubscribe**

    - Users can click the link in their newsletter email to unsubscribe from the site newsletter. Once the user is logged in, the email input field will pre-fill with the user's email. Users see a confirmation screen after unsubscribing.

![screenshot](documentation/features/user/newsletter-unsubscribe1.png)
![screenshot](documentation/features/user/newsletter-unsubscribe2.png)
![screenshot](documentation/features/user/newsletter-unsubscribe3.png)

### Admin Features

- **Create Products**

    - Administrators can use a front-end form to create new site products. The form is simple and clean and automatically formats and displays the created product in the same manner as existing products.

![screenshot](documentation/features/admin/create-product.png)

- **Edit Products**

    - Administrators can use a front-end form to update existing products. If the current logged-in user has superuser privileges, an edit button will appear under products which allows that user to edit the product's details.

![screenshot](documentation/features/admin/update-product.png)

- **Delete Products**

    - Administrators can use a front-end form to delete existing products. If the current logged-in user has superuser privileges, a delete button will appear under posts which allows that user to delete that product.

![screenshot](documentation/features/admin/delete-product.png)

- **Webhooks**

    - The site uses a secure and robust webhook system to ensure that the payment process cannot be interrupted and corrupted, either through user error or malicious intent. Webhooks are incorporated via the Stripe payment system and are handled on the Stripe website, by way of the python code in `checkout > webhook_handler.py` and `checkout > webhooks.py`

![screenshot](documentation/features/admin/webhooks.png)


- **Contact Requests**

    - Admins can see a list of all of the contact messages sent by users. Messages are displayed in an easy-to-read table, with all of the salient information presented. Messages are automatically sorted with those messages which have not been responded to at the top of the list, with the oldest (the message which has gone unanswered the longest) at the top. Admins can click on the view details links to see the full contact messages, as well as respond to the message.

![screenshot](documentation/features/admin/contact-requests.png)

- **Contact Details**

    - Admins can see details of a contact message left by the user. All of the contact message's information can be seen, including email, name, subject, message, and whether this contact message has been respond to. Contact messages can be responded to or deleted via the large buttons at the bottom of the page. A link navigates back to the contact requests page.

![screenshot](documentation/features/admin/contact-details.png)

- **Contact Message Delete**

    - Admins can delete contact messages from the database using a front end delete function inside the contact message details page.

![screenshot](documentation/features/admin/contact-delete.png)

- **Contact Respond**

    - Admins can respond to user contact messages using an email form which appears upon clicking the 'respond to message' button on the contact details page. A text area appears with the user's name and the default email signoff link pre-populated for efficiency in the typing of the response. The 'Send Email' button sends an email response to the user's given email address with the content of the text box as the body of the email.

    The contact message is then automatically marked as 'Responded' and the 'respond to message' button no longer appears on that message's details page.

![screenshot](documentation/features/admin/contact-respond1.png)
![screenshot](documentation/features/admin/contact-respond2.png)
![screenshot](documentation/features/admin/contact-respond3.png)

- **Newsletter Confirmation Emails**

    - Emails are automatically sent out to all new subscribers of the site newsletter. The email contains a 'thank you' message, as well as a link to allow users to unsubscribe from the mailing list.

![screenshot](documentation/features/admin/newsletter-confirmation-email.png)


### Future Features

- Subscription Payments
    - Possible subscription payment model which would include access to all courses for a recurring fee. Could implement this via django groups with subscriber accounts given privileges to view subscriber-only areas of the site. Would also need to implement this in the stripe backend and update webhooks.
- Newsletter Template and Front-End Customisation
    - A system in which an admin could easily customise and send out a newsletter to all subscribers. Would need a front-end form which could take text & images, and would need to add the functionality into the newsletter views.
- Digital Music Sheet Sales
    - Sale of digital music sheets to accompany the course material. Could sell the music sheets in PDF format or as interactive sheets as part of another interactive music learning app. This would not be difficult to implement, but would need some revision of the user shopping experience as shopping for courses and for digital sheets is quite different. Things like item quantity would need to be revised.

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Psycopg2](https://pypi.org/project/psycopg2/) used as a PostgreSQL database adapter
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.
- [Allauth](https://docs.allauth.org/en/latest/) used as the user authentication system
- [Pillow](https://pypi.org/project/Pillow/) used as the Python framework for the site.
- [Gunicorn](https://docs.gunicorn.org/en/stable/index.html) used for WSGI server
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used for auto-formatting of front-end forms


## Database Design

While planning this project, I drew up an Entity Relationship Diagram to help me to visualise the database models and their relationships.

![screenshot](documentation/erd.png)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/LewisMDillon/web-piano-academy/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

The MoSCoW method was used with accompanying custom Github project labels to help me to prioritise the important tasks in the time I had available.

Epics were decomposed into smaller User Stories, which were themselves further broken down into Tasks. The Github issue linking system was utilised to ensure that user stories which were children of an epic were kept organised and easily accessible through these links


![screenshot](documentation/github/project.png)
![screenshot](documentation/github/milestones.png)
![screenshot](documentation/github/epic.png)
![screenshot](documentation/github/user-story.png)

### GitHub Issues

[GitHub Issues](https://github.com/LewisMDillon/web-piano-academy/issues) served as an another Agile tool.
There, I used my own **User Story Template** and **Epic Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/LewisMDillon/web-piano-academy/issues)

    ![screenshot](documentation/github/issues-open.png)

- [Closed Issues](https://github.com/LewisMDillon/web-piano-academy/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/github/issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- ![screenshot](documentation/github/must-have.png)  : guaranteed to be delivered (*max 60% of stories*) 
- ![screenshot](documentation/github/should-have.png)  : adds significant value, but not vital (*the rest ~20% of stories*) 
- ![screenshot](documentation/github/could-have.png)  : has small impact if left out (*20% of stories*) 
- ![screenshot](documentation/github/wont-have.png)  : not a priority for this iteration 

## Ecommerce Business Model

This site sells goods to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions.

It is still in its early development stages, although it already has a newsletter system, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send regular messages to site users.
For example, what items are on special offer, new items in stock,
updates to business hours, notifications of events, and much more!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

I also played around with [Word Tracker](https://www.wordtracker.com) a bit
to check the frequency of some of my site's primary keywords (only until the free trial expired).

- ![screenshot](documentation/wordtracker.png)

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://web-piano-academy-16cd779294ab.herokuapp.com

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://web-piano-academy-16cd779294ab.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the
[Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip)
provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more. 


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment


The live deployed application can be found deployed on [Heroku](https://web-piano-academy-16cd779294ab.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: web-piano-academy).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
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

		```shell
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

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-web-piano-academy` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
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
	
	- Click **Review Policy**.
	- Suggested Name: `policy-web-piano-academy` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for web-piano-academy static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-web-piano-academy".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-web-piano-academy") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-web-piano-academy` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-web-piano-academy`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://web-piano-academy-16cd779294ab.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or web-piano-academy
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/LewisMDillon/web-piano-academy) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/LewisMDillon/web-piano-academy.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/LewisMDillon/web-piano-academy)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LewisMDillon/web-piano-academy)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Credits

### Content


| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/questions/3578882) | Django Authentication | How to specify the login_required redirect url in django |
| [StackOverflow](https://stackoverflow.com/questions/47089450) | automated testing | How to test content of a Django email |
| [Cornell Music Academy](https://cornellmusicacademy.com/) | entire site | Used as a basis for text on various site pages |
| [Bootstrap Components](https://getbootstrap.com/docs/5.3/examples/) | entire site | Bootstrap stock components used as a base for various site features such as navbar & footer |
| [Codepen](https://codepen.io/AramayisO/pen/xzoYeM) | Navbar | Scrolling transition navbar |
| [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) | entire site | Various code sections taken from the CI Boutique Ado Walkthrough Project |
| [Rory Sheridan](https://github.com/Ri-Dearg/neverlost-thrift/blob/master/products/views.py) | Testing | My mentor's code repository - various code snippets taken from tests.py for automated python testing |
| [Lewis Dillon (me)](https://github.com/LewisMDillon/bushy-park-tennis-club-ld) | entire site | Various code snippets taken from my previous project |
| [Alvarotrigo](https://alvarotrigo.com/blog/css-accordion/) | FAQ page | HTML & CSS for FAQ Accordion |

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Leonardo.ai](https://app.leonardo.ai) | Landing Page | image | hero image on homepage |
| [Pexels](https://www.pexels.com/photo/music-teacher-looking-at-a-boy-playing-piano-8520467/) | About Page | image | 'who we are' image |
| [Gear4Music](https://www.gear4music.com/blog/piano-learning-apps/) | About Page | image | 'what we do' image |
| [Unsplash](https://images.unsplash.com/photo-1626541650317-6ac1c2325995?auto=format&fit=crop&q=80&w=2080&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D) | About Page | image | 'your journey' image |
| [Wikipedia](https://en.wikipedia.org/wiki/Johann_Sebastian_Bach) | courses page | image | course image |
| [Wikipedia](https://en.wikipedia.org/wiki/Ludwig_van_Beethoven) | courses page | image | course image |
| [Wikipedia](https://en.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin) | courses page | image | course image |
| [Wikipedia](https://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart) | courses page | image | course image |
| [Dreamstime](https://www.dreamstime.com/stock-image-hand-pen-music-sheet-pointing-to-book-handwritten-notes-image38899901) | courses page | image | course image |
| [Getty Images](https://www.gettyimages.ie/photos/composer) | courses page | image | course image |
| [Unsplash](https://unsplash.com/s/photos/music-writing) | courses page | image | course image |
| [Freepik](https://www.freepik.com/premium-photo/close-up-young-beautiful-redhead-caucasian-girl-playing-piano_2017729.htm) | courses page | image | course image |
| [Facebook](https://m.facebook.com/AlexaPianoSinger/) | courses page | image | course image |
| [Istockphoto](https://www.istockphoto.com/photo/african-male-playing-beautiful-song-on-piano-gm1255997445-367613276) | courses page | image | course image |
| [Unsplash](https://unsplash.com/s/photos/guitar-singer-composer) | courses page | image | course image |
| [Unsplash](https://unsplash.com/s/photos/piano-hands) | courses page | image | course image |
| [Last Minute Musicians](https://www.lastminutemusicians.com/blog/how-to-maximize-efficiency-in-your-piano-practice/) | courses page | image | course image |
| [Getty Images](https://www.gettyimages.ie/photos/composer) | courses page | image | course image |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements


- I would like to thank my partner Rachel, for believing in me, and helping me to make this transition into software development.
- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
