"""
Working with classes follows a simple pattern:
1. Define the class - Create a blueprint with the class keyword
2. Add an __init__ method - Set up initial data when objects are created
3. Create instances - Make actual objects from your class
4. Access the data - Use the attributes you defined
"""

class APIConfig:
    def __init__(self, api_key, model = "gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

dev_config = APIConfig("SK-dev-key", max_tokens=50)
prod_config = APIConfig("sk-prod-key", model="gpt-4.0", max_tokens=150)

print(dev_config.model)
print(prod_config.api_key)
print(prod_config.max_tokens)



class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid Email: {email}")
            return False
        return True
    
    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True
    
    def get_errors(self):
        return self.errors


validator = DataValidator()

validator.validate_email("hasnain0122gmail.com")
validator.validate_age(30)

validator.get_errors()