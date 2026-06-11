# 1. Scenrio: There is a COD already in e commerse site newly adde dthe credit card feature what all
# are the positve and negative scenario you think and write

# TC01 - Verify user can successfully place order using valid credit card
# TC02 - Verify all major cards accepted (Visa, Mastercard, Amex, Rupay)
# TC03 - Verify order confirmation page displayed after successful payment
# TC04 - Verify confirmation email/SMS received after credit card payment
# TC05 - Verify correct amount is charged to the credit card
# TC06 - Verify user can save credit card details for future use
# TC07 - Verify saved card is displayed during next checkout
# TC08 - Verify CVV is masked while entering
# TC09 - Verify card number is masked after entry (show only last 4 digits)
# TC10 - Verify 3D secure / OTP flow works correctly
# TC11 - Verify COD option still available after credit card feature added
# TC12 - Verify user can switch between COD and Credit Card at checkout
# TC13 - Verify COD orders are not affected by credit card integration
# TC14 - Verify credit card option visible on payment page
# TC15 - Verify order summary shows correct amount before payment
# TC16 - Verify user can apply coupon/discount with credit card payment
# TC17 - Verify EMI options displayed for eligible cards
# TC18 - Verify international credit cards are accepted
# TC19 - Verify error shown when invalid card number entered
# TC20 - Verify error shown when expired card is used
# TC21 - Verify error shown when wrong CVV is entered
# TC22 - Verify error shown when card holder name is left blank
# TC23 - Verify error shown when card number is less than 16 digits
# TC24 - Verify error when special characters entered in card number field
# TC25 - Verify error when incorrect expiry date format entered (e.g. 13/25)


# 2. Scenario: Searching for Iphone 17 in amazon if it gives suggestion on the same select that and make the test
#pass else make it fail write in selenium script
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Go to Amazon
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    # Step 2: Search for iPhone 17
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("iPhone 17")

    # Step 3: Wait for suggestions to appear
    suggestions = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='autocomplete-results-container']//div[@role='option']")
    ))

    # Step 4: Check if iPhone 17 suggestion exists and click
    suggestion_found = False

    for suggestion in suggestions:
        if "iPhone 17" in suggestion.text:
            suggestion.click()
            suggestion_found = True
            print("✅ TEST PASSED: iPhone 17 suggestion found and clicked")
            break

    # Step 5: Fail the test if suggestion not found
    if not suggestion_found:
        raise AssertionError("❌ TEST FAILED: iPhone 17 suggestion not found in dropdown")

except AssertionError as e:
    print(e)

except Exception as e:
    print(f"❌ TEST FAILED due to unexpected error: {e}")

finally:
    driver.quit()