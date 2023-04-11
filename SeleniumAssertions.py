# Assert that the title of the web page is equal to "My Website"
actual_title = driver.title
expected_title = "My Website"
assertEqual(actual_title, expected_title)

# Assert that the value of a text input is not equal to "Hello"
text_input = driver.find_element_by_id("my_input")
actual_value = text_input.get_attribute("value")
expected_value = "Hello"
assertNotEqual(actual_value, expected_value)


# Assert that a certain element is displayed on the web page
element = driver.find_element_by_id("my_element")
assert assertTrue(element.is_displayed())


# Assert that a certain element is not selected
checkbox = driver.find_element_by_id("my_checkbox")
assert assertFalse(checkbox.is_selected())


# Assert that two elements are the same object
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")
assertIs(element1, element2)


# Assert that two elements are not the same object
element1 = driver.find_element_by_id("element1")
element2 = driver.find_element_by_id("element2")
assertIsNot(element1, element2)


# Assert that a certain element is None
element = driver.find_element_by_id("my_element")
assertIsNone(element)


# Assert that a certain value is present in a list
values = ["apple", "banana", "cherry"]
assertIn("banana", values)


# Assert that a certain value is not present in a list
values = ["apple", "banana", "cherry"]
assertNotIn("grape", values)



# Assert that an element is an instance of a certain class
element = driver.find_element_by_id("my_element")
assertIsInstance(element, WebElement)


# Assert that an element is not an instance of a certain class
element = driver.find_element_by_id("my_element")
assertNotIsInstance(element, CheckBox)


# Assert that the calculated result is approximately equal to the expected result
actual_result = 3.14159
expected_result = 3.14
assertAlmostEqual(actual_result, expected_result, places=2)


# Assert that two floating-point values are not approximately equal with a tolerance of 0.01
actual_result = 3.14159
expected_result = 2.98
assertNotAlmostEqual(actual_result, expected_result, places=2)


# Assert that a certain value is greater than another value
actual_value = 100
expected_value = 50
assertGreater(actual_value, expected_value)



# Assert that a certain value is greater than or equal to another value
actual_value = 100
expected_value = 100
assertGreaterEqual(actual_value, expected_value)


# Assert that a certain value is less than another value
actual_value = 50
expected_value = 100
assertLess(actual_value, expected_value)


# Assert that a certain value is less than or equal to another value
actual_value = 100
expected_value = 100
assertLessEqual(actual_value, expected_value)
