from selenium import webdriver
import unittest
# (1) 初始化Chrome浏览器实例
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser  = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title),"browser title was:"+self.browser.title
        self.fail('Finish the Test')

if __name__ == '__main__':
   unittest.main()
