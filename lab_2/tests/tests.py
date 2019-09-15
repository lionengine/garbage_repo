import unittest
from app import main, home_work


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'
        self.date_am = 'here is the AM'
        self.date_pm = 'here is the PM'
        self.date_nopoint = 'here is nothing you can benefit from, okay, cool'
        
    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work_am(self):
        self.assertTrue(home_work(self.date_am) == 'am')

    def test_home_work_pm(self):
        self.assertTrue(home_work(self.date_pm) == 'pm')
    
    def test_home_work_nopoint(self):
        self.assertFalse(home_work(self.date_nopoint))
