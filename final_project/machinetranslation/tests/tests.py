from translator import english_to_french, french_to_english

def test_print(test_case_id, test_case_description, expected_output, actual_output):
    print(f"Test Case {test_case_id}")
    print(f"Description: {test_case_description}")
    print(f"Expected Output: {expected_output}")
    print(f"Actual Output: {actual_output}")
    if(actual_output == expected_output):
        print("Result: PASS")
    else:
        print("Result: FAIL")
    print("")

# Null case test for english to french
test_print(
    test_case_id = 1,
    test_case_description = "Null Case for English to French Conversion",
    expected_output = "",
    actual_output = english_to_french("")
)

# Normal case for english to french
test_print(
    test_case_id = 2,
    test_case_description = "Normal Case for English to French Translation",
    expected_output = "Bonjour",
    actual_output = english_to_french("Hello")
)

# Null case test for french to english
test_print(
    test_case_id = 3,
    test_case_description = "Null Case for French to English Conversion",
    expected_output = "",
    actual_output = french_to_english("")
)

# Normal case for french to english
test_print(
    test_case_id = 4,
    test_case_description = "Normal Case for French to English Translation",
    expected_output = "Hello",
    actual_output = french_to_english("Bonjour")
)
