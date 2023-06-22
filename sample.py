import pypasskey

# Save credentials for a service
pypasskey.save_credentials('my_service', 'my_username', 'my_password')

# Retrieve credentials for a service
credentials = pypasskey.get_credentials('my_service')
if credentials:
    print(f"Username: {credentials['username']}")
    print(f"Password: {credentials['password']}")
else:
    print("No credentials found for this service.")
