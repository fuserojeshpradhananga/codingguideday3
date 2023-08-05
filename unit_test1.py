import re
import unittest

def validate_email(email):
    # Proper email format such as presence of "@", no space in the address
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Presence of valid email providers such as yahoo, gmail, and outlook
    valid_providers = ["yahoo", "gmail", "outlook"]
    domain = email.split("@")[1].split(".")[0]
    if domain not in valid_providers:
        return False

    # Make sure there are no disposable email providers such as yopmail
    disposable_providers = ["yopmail"]
    if domain in disposable_providers:
        return False

    return True

# Unit tests
class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "john.doe@gmail.com",
            "jane_smith@yahoo.com",
            "mike.smith@outlook.com",
        ]

        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email), f"Failed for email: {email}")

    def test_invalid_emails(self):
        invalid_emails = [
            "john.doe@company",  # No valid domain
            "user@yopmail.com",  # Disposable email provider
            "user @domain.com",  # Space in the address
            "test@invalid@provider.com",  # Multiple "@" characters
        ]

        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email), f"Failed for email: {email}")

if __name__ == "__main__":
    unittest.main()
