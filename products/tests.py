from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Product
from django.utils import timezone


# Create your tests here.

# ------------ MODEL TESTING ------------

class TestCategory(TestCase):
    """Tests the Category model in the products app."""
    def setUp(self):
        """
        Makes a sample Category object
        """

        name = "test_category"
        display_name = "test_category_display"
        category1 = Category.objects.create(
            name=name,
            display_name=display_name
            )

        category1.save()

    def test_str(self):
        """Tests the string method on the category."""
        # Retrieves the most recently created email and gets its string
        category1 = Category.objects.latest('pk')
        category_string = str(category1.name)

        # Cofirms the email string is correct.
        self.assertEqual((category_string), (category1.name))


class TestProduct(TestCase):
    """Tests the Product model in the products app."""
    def setUp(self):
        """
        Makes a sample Product object
        """

        name = "test_product"
        description = "test_product_description"
        price = '999.99'
        date_created = timezone.now()
        product1 = Product.objects.create(
            name=name,
            description=description,
            price=price,
            date_created=date_created
            )

        product1.save()

    def test_str(self):
        """Tests the string method on the category."""
        # Retrieves the most recently created email and gets its string
        product1 = Product.objects.latest('pk')
        product_string = str(product1.name)

        # Cofirms the email string is correct.
        self.assertEqual((product_string), (product1.name))



# ------------ VIEWS TESTING ------------

class ProductViewTestCase(TestCase):
    """
    Test case for testing product views.
    """

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Then, creates a sample product.
        """

        username1 = "testUser"
        email1 = "testuser@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        username2 = "testUserStaff"
        email2 = "testuser2@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        user1 = User.objects.create(
            username=username1,
            email=email1,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2 = User.objects.create(
            username=username2,
            email=email2,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2.is_staff = True
        user2.is_superuser = True

        user1.save()
        user2.save()

        name = "test_product"
        description = "test_product_description"
        price = '999.99'
        date_created = timezone.now()
        product1 = Product.objects.create(
            name=name,
            description=description,
            price=price,
            date_created=date_created
            )

        product1.save()

    
    def test_courses_render_context(self):
        """
        Tests that the courses page is rendered properly
        """

        response = self.client.get('/products/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/courses.html', 'base.html'
            )

        # Checks whether the context item is passed in
        self.assertTrue(response.context['products'])

    
    def test_edit_product_render_form(self):
        """
        Tests the url path by passing in the primary key of new test
        product. Checks that the product detail page is rendered properly.
        Checks that the product detail view matches the test product passed
        into the url.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Tests the url path
        product1 = Product.objects.latest('pk')

        # Log in as testUser (no staff privileges)
        self.client.force_login(test_user)

        # Try to access edit product page (staff-only)
        response = self.client.get(f'/products/courses/edit/{product1.pk}/')

        # Check that page access is not granted
        self.assertNotEqual(response.status_code, 200)

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access product details page (staff-only)
        response = self.client.get(f'/products/courses/edit/{product1.pk}/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'products/edit_product.html',
            'base.html'
            )


        # Get the most recent product
        # (should be test_product that was just created)
        productToUpdate = Product.objects.latest('date_created')
       
        # update the product
        response = self.client.post((f'/products/courses/edit/{productToUpdate.pk}/'), {
            'name': "test_product_updated",
            'description': "test_product_description_updated",
            'price': '9.99',
            'date_created': timezone.now(),
            })

        # Get the most recent post
        # (should be test_product_updated that was just updated)
        newTestProduct = Product.objects.latest('date_created')

        product_string_name = str(newTestProduct.name)
        product_string_description = str(newTestProduct.description)
        product_string_price = str(newTestProduct.price)

        # Check that the post has been successfuly updated
        self.assertEqual((product_string_name), ("test_product_updated"))
        self.assertEqual((product_string_description), ("test_product_description_updated"))
        self.assertEqual((product_string_price), ("9.99"))


    def test_add_product_render_form(self):
        """
        Tests the url path by passing in the primary key of new test
        product. Checks that the product detail page is rendered properly.
        Checks that the product detail view matches the test product passed
        into the url.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Tests the url path
        product1 = Product.objects.latest('pk')

        # Log in as testUser (no staff privileges)
        self.client.force_login(test_user)

        # Try to access add product page (staff-only)
        response = self.client.get(f'/products/courses/add/')

        # Check that page access is not granted
        self.assertNotEqual(response.status_code, 200)

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access add product page (staff-only)
        response = self.client.get(f'/products/courses/add/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'products/add_product.html',
            'base.html'
            )

        # Get the ID of the most recently created product object
        originalProduct = Product.objects.latest('pk')
        originalProductId = originalProduct.pk

        # Create a new test product using the page form
        response = self.client.post(('/products/courses/add/'), {
            'name': 'test_product_created',
            'description': 'test_product_description_created',
            'price': '99.99',
            'date_created': timezone.now()
            })

        # Get the most recent product object
        # (should be test_product_created that was just created)
        newTestProduct = Product.objects.latest('pk')
        newTestProductId = newTestProduct.pk
        
        # Check that the most recent product created is
        # not the original product, meaning a new one
        # was successfully created
        self.assertNotEqual((originalProductId), (newTestProductId))

        # Check that the most recently created object is our test product object
        self.assertEqual('test_product_created', Product.objects.latest('pk').name)


    def test_delete_product_render_form(self):
        """
        Tests the url path by passing in the primary key of new test
        product. Checks that the product detail page is rendered properly.
        Checks that the product detail view matches the test product passed
        into the url.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Get the most recently created product object
        productToDelete = Product.objects.latest('pk')

        # Get the to-be-deleted product object's ID
        deletedProductId = (productToDelete.pk)

        # Log in as testUser (not superuser)
        self.client.force_login(test_user)

        # Attempt to delete the product object using the delete view
        response = self.client.post(
            f'/products/courses/delete/{productToDelete.pk}/'
            )

        # Check that access is denied
        self.assertNotEqual(response.status_code, 200)

        # Log in as testUserStaff (superuser)
        self.client.force_login(test_user_staff)

        # Delete the product object using the delete view
        response = self.client.post(
            f'/products/courses/delete/{productToDelete.pk}/', follow=True
            )
        self.assertEqual(response.status_code, 200)

        # Check if there are any product objects in the database,
        # if not, that means that the deletion was successful
        if Product.objects.exists():
            # If there are product objects remaining, we need to
            # check that the one we tried to delete has been deleted.
            # Get the ID of the last product object in the database
            newLastProduct = Product.objects.latest('pk')
            newLastProductId = newLastProduct.pk

            # Check if the last product object in the database is the
            # same one that we tried to delete, if not, that
            # means the deletion was successful
            self.assertNotEqual(deletedProductId, newLastProductId)
        