from django.test import TestCase


class IndexFormLoginTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/login/')

    def test_get_login(self):
        self.assertEqual(200, self.resp.status_code)

    def test_csrf(self):
        """Html must contains csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_login_has_form(self):
        """Html has contains tags """
        tags = (('<form', 1),
                ('<input', 3),
                ('type="text"', 1),
                ('type="password"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
