from django.test import TestCase

from parse_helpers import Tokenizer
from parse_helpers import extract_contacts
from contact.models import Contact

class TestTokenizer(TestCase):
    def test_normal(self):
        line = 'Tina L. Watsontarver, Contract Specialist, Email tina.watsontarver.1@us.af.mil - Jaclyn G. Rodriguez, Contracting Officer, Email jaclyn.rodriguez@us.af.mil'

        tokenizer = Tokenizer(line)
        answers = [
            'Tina',
            'L.',
            'Watsontarver',
            ',',
            'Contract',
            'Specialist',
            ',',
            'Email',
            'tina.watsontarver.1@us.af.mil',
            '-',
            'Jaclyn',
            'G.',
            'Rodriguez',
            ',',
            'Contracting',
            'Officer',
            ',',
            'Email',
            'jaclyn.rodriguez@us.af.mil'
        ]

        self.assertEqual(tokenizer.get_tokens(), answers)

    def test_phone(self):
        line = 'First M. Last, Phone 1234567890, Email test@test.com'

        tokenizer = Tokenizer(line)
        answers = [
            'First',
            'M.',
            'Last',
            ',',
            'Phone',
            '1234567890',
            ',',
            'Email',
            'test@test.com'
        ]

        self.assertEqual(tokenizer.get_tokens(), answers)

    def test_phone_dashes(self):
        line = 'First M. Last, Phone (123)-456-7890, Fax: +49 123-456-7890, Email test@test.com'

        tokenizer = Tokenizer(line)
        answers = [
            'First',
            'M.',
            'Last',
            ',',
            'Phone',
            '(123)',
            '-',
            '456',
            '-',
            '7890',
            ',',
            'Fax',
            '+49',
            '123',
            '-',
            '456',
            '-',
            '7890',
            ',',
            'Email',
            'test@test.com'
        ]

        self.assertEqual(tokenizer.get_tokens(), answers)

    def test_apostrophe(self):
        line = 'Sean O\'Grandy'

        tokenizer = Tokenizer(line)
        answers = [
            'Sean',
            'O\'Grandy',
        ]

        self.assertEqual(tokenizer.get_tokens(), answers)

    def test_alphanumerc_split(self):
        line = 'Test Person123-432-4567'

        tokenizer = Tokenizer(line)
        answers = [
            'Test',
            'Person',
            '123',
            '-',
            '432',
            '-',
            '4567',
        ]

        self.assertEqual(tokenizer.get_tokens(), answers)


class TestExtractContacts(TestCase):

    def test_normal(self):

        line = 'Tina L. Watsontarver, Contract Specialist, Email tina.watsontarver.1@us.af.mil - Jaclyn G. Rodriguez, Contracting Officer, Email jaclyn.rodriguez@us.af.mil'
        tokens = [
            'Tina',
            'L.',
            'Watsontarver',
            ',',
            'Contract',
            'Specialist',
            ',',
            'Email',
            'tina.watsontarver.1@us.af.mil',
            '-',
            'Jaclyn',
            'G.',
            'Rodriguez',
            ',',
            'Contracting',
            'Officer',
            ',',
            'Email',
            'jaclyn.rodriguez@us.af.mil'
        ]

        tokenizer = Tokenizer(tokens)

        contacts = extract_contacts(tokenizer)

        tina = Contact(
            name='Tina L. Watsontarver',
            title='Contract Specialist',
            email='tima.watsontarver.1@us.af.mil'
        )

        jaclyn = Contact(
            name='Jaclyn G. Rodriguez',
            title='Contracting Officer',
            email='jaclyn.rodriguez@us.af.mil'
        )

        answer = [tina, jaclyn]

        self.assertEqual(answer, contacts)
