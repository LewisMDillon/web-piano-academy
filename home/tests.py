from django.test import TestCase

class HomeViewTestCase(TestCase):
    """
    Test case for testing home views.
    """

    def test_home_render(self):
        """
        Tests that the home page is rendered properly
        """

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'home/index.html', 'base.html'
            )


    def test_about_render(self):
        """
        Tests that the home page is rendered properly
        """

        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'home/about.html', 'base.html'
            )


    def test_render_404_error(self):
        """
        Confirms the rendering of a 404 page when an invalid
        page ID is entered.
        """

        response = self.client.get('/invalidtestpage123/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(
            response, '404.html', 'base.html'
        )
