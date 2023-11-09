from django.test import TestCase
from .models import Faq

# ------------ MODEL TESTING ------------

class TestFaq(TestCase):
    """Tests the Faq model in the faq app."""
    
    def setUp(self):
        """
        Makes a sample Faq object
        """

        question = "test_question"
        answer = "test_answer"
        faq1 = Faq.objects.create(
            question=question,
            answer=answer,
            )

        faq1.save()

    def test_str(self):
        """Tests the string method on the faq."""
        # Retrieves the most recently created faq and gets its string
        faq1 = Faq.objects.latest('pk')
        faq_string_question = str(faq1.question)

        # Cofirms the faq string is correct.
        self.assertEqual((faq_string_question), (faq1.question))


# ------------ VIEWS TESTING ------------

class FaqViewTestCase(TestCase):
    """
    Test case for testing Faq views.
    """

    def setUp(self):
        """
        Makes a sample Faq object
        """

        question = "test_question"
        answer = "test_answer"
        faq1 = Faq.objects.create(
            question=question,
            answer=answer,
            )

        faq1.save()


    def test_faq_render_context(self):
        """
        Tests that the faq page is rendered properly and all of
        the correct context is passed into the page
        """

        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'faq/faq.html', 'base.html'
            )
        # Checks whether the context item is passed in
        self.assertTrue(response.context['faqs'])