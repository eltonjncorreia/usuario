from django.test import TestCase


class IndexFormCadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form_cadastro(self):
        tags = (('<form', 1),
                ('<input', 4),
                ('type="text"', 1),
                ('type="email"', 1),
                ('type="submit"', 1),
                )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

