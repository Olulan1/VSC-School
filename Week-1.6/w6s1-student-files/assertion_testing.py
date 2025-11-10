# docs.pytest.org
from weather import comfort_level
temp = 20.0                 # Arrange
level = comfort_level(temp) # Act
assert level == "OK"        # Assert

# assert comfort_level(20.0) == "OK"
