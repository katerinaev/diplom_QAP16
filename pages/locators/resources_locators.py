class ResourcesLocators:
    # DROPDOWNS = '//div[text()="Content Type"]'
    # DROPDOWN = '//*[@data-name="content_type"]'
    CONTENT_TYPE = '//*[@class="fs-label-wrap"]//*[text()="Content Type"]'
    # DROPDOWNS = '//*[contains(@class, "blog-filters")]'
    # DROPDOWNS = '//i[@class="facetwp-icon"]'
    DROPDOWNS = '//*[@class="alignwide py-14 md:py-20 on"]'
    # CONTENT_TYPE_DROPDOWN = '//select[@class="facetwp-dropdown fs-hidden"]'
    CONTENT_TYPE_DROPDOWN = '//*[@data-name="content_type"]/select'
    CASE_STUDY = '//*[@class="fs-option-label"][contains(text(),"Case Study")]'
    CASE_STUDY_OPTION = '//option[@value="case-study"]'
