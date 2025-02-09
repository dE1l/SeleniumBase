from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_demo_site(self):
        self.open("://seleniumbase.github.io/demo_page.html")

        # Assert that the element is visible on the page
        self.assert_element("tbody#tbodyId")

        # Assert that the text appears within a given element
        self.assert_text("Demo Page", "h1")

        # Update the text of various text fields on the page
        self.update_text("#myTextInput", "This is Automated")
        self.update_text("textarea.area1", "Testing Time!\n")
        self.update_text('[name="preText2"]', "Typing Text!")

        # Verify that a hover dropdown link changes page text
        self.assert_text("Automation Practice", "h3")
        self.hover_and_click("#myDropdown", "#dropOption2")
        self.assert_text("Link Two Selected", "h3")

        # Verify that a button click changes text on the page
        self.assert_text("This Text is Green", "#pText")
        self.click("#myButton")
        self.assert_text("This Text is Purple", "#pText")

        # Assert that the given SVG is visible on the page
        self.assert_element('svg[name="svgName"]')

        # Verify that a slider control updates a progrss bar
        self.assert_element('progress[value="50"]')
        self.press_right_arrow("#myslider", times=5)
        self.assert_element('progress[value="100"]')

        # Verify that a "select" option updates a meter bar
        self.assert_element('meter[value="0.25"]')
        self.select_option_by_text("#mySelect", "Set to 75%")
        self.assert_element('meter[value="0.75"]')

        # Assert an element located inside an iFrame
        self.assert_false(self.is_element_visible("img"))
        self.switch_to_frame("#myFrame1")
        self.assert_true(self.is_element_visible("img"))
        self.switch_to_default_content()

        # Assert text located inside an iFrame
        self.assert_false(self.is_text_visible("Frame Text"))
        self.switch_to_frame("#myFrame2")
        self.assert_true(self.is_text_visible("Frame Text"))
        self.switch_to_default_content()

        # Verify that clicking a radio button selects it
        self.assert_false(self.is_selected("#radioButton2"))
        self.click("#radioButton2")
        self.assert_true(self.is_selected("#radioButton2"))

        # Verify that clicking a checkbox makes it selected
        self.assert_false(self.is_selected("#checkBox1"))
        self.click("#checkBox1")
        self.assert_true(self.is_selected("#checkBox1"))

        # Verify clicking on multiple elements with one call
        self.assert_false(self.is_selected("#checkBox2"))
        self.assert_false(self.is_selected("#checkBox3"))
        self.assert_false(self.is_selected("#checkBox4"))
        self.click_visible_elements("input.checkBoxClassB")
        self.assert_true(self.is_selected("#checkBox2"))
        self.assert_true(self.is_selected("#checkBox3"))
        self.assert_true(self.is_selected("#checkBox4"))

        # Assert the title of the current web page
        self.assert_title("Web Testing Page")
