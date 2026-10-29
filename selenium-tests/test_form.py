"""Selenium test suite for the Student Feedback Form."""
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class TestStudentFeedbackForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        opts = Options()
        if os.environ.get("HEADLESS") == "1":
            opts.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=opts)
        page = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "index.html"))
        cls.url = "file:///" + page.replace("\\", "/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(self.url)

    def fill(self, name="Test Student", email="test@example.com", mobile="9876543210",
             dept="CSE", feedback="The DevOps lab sessions were clear useful and well organised overall"):
        d = self.driver
        d.find_element(By.ID, "name").send_keys(name)
        d.find_element(By.ID, "email").send_keys(email)
        d.find_element(By.ID, "mobile").send_keys(mobile)
        if dept:
            Select(d.find_element(By.ID, "department")).select_by_visible_text(dept)
        d.find_element(By.CSS_SELECTOR, "input[value='Male']").click()
        d.find_element(By.ID, "feedback").send_keys(feedback)
        d.find_element(By.ID, "submitBtn").click()
        return d.find_element(By.ID, "message").text

    def test_page_title(self):
        self.assertEqual(self.driver.title, "Student Feedback Form")

    def test_valid_submission(self):
        self.assertIn("successfully", self.fill())

    def test_invalid_email(self):
        self.assertIn("valid email", self.fill(email="wrong-email"))

    def test_short_feedback(self):
        self.assertIn("at least 10 words", self.fill(feedback="too short"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
