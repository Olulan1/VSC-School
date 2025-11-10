# Unit tests for the comfort_level() function

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class


from weather import comfort_level

def test_cold():
    assert comfort_level( 4  ) == "COLD"
    assert comfort_level( 13  ) == "COLD"

def test_hot():
    assert comfort_level( 26 ) == "HOT"
    assert comfort_level( 3 ) == "HOT"

def test_ok():
    assert comfort_level(16) == "OK"
    assert comfort_level(24) == "OK"

test_cold() # nothing happens therfore passs
test_hot() # incorrect params give session error