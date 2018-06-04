# -*-coding:utf-8-*-

from pageobjects.pim.employee_list import EmployeeList
from lib.log import Log

class EditPersonalDetails(EmployeeList):
    """
    edit personal details elements
    """
    page_head = ('xpath', '//input[@id="Personal Details"]')
    first_name = ('id', 'personal_txtEmpFirstName')
    middle_name = ('id', 'personal_txtEmpMiddleName')
    last_name = ('id', 'personal_txtEmpLastName')
    employee_id = ('id', 'personal_txtEmployeeId')
    other_id = ('id', 'personal_txtOtherID')
    license_number = ('id', 'personal_txtLicenNo')
    license_expiry_date = ('id', 'personal_txtLicExpDate')
    #ssn_number = ('id', '//input[@id="personal_txtNICNo"]')
    #sin_number = ('id', '//input[@id="personal_txtSINNo"]')
    gender_ele = '//ul[@class="radio_list"]//label[text()="{}"]'
    #gender_male = ('id', '//input[@id="personal_optGender_1"]')
    #gender_female = ('id', '//input[@id="personal_optGender_2"]')
    marital_status = ('id', 'personal_cmbMarital')
    nationality = ('id', 'personal_cmbNation')
    date_of_birth = ('id', 'personal_DOB')
    edit_btn = ('id', 'btnSave')
    add_btn = ('id', 'btnAddAttachment')
    select_file = ('id', 'ufile')
    comment = ('id', 'txtAttDesc')
    upload_btn = ('id', 'btnSaveAttachment')
    cancel_btn = ('id', 'cancelButton')
    save_btn = ('id', 'btnSave')
    edit_attachment_btn = ('class_name', 'editLink' )
    save_comment_only = ('id', 'btnCommentOnly')
    flag = ('xpath', '//div[@class="message success fadable"]')
    delete_attachment_btn = ('id', 'btnDeleteAttachment')
    file_name = ('xpath', '//td[2]/a')
    check_box =('class_name', 'checkboxAtch')
    check_allbox = ('id', 'attachmentsCheckAll')

    def __int__(self, browser):
        super(EditPersonalDetails,self).__init__(browser)

    def open_personal_details_via_adding_employee(self, firstname, lastname):
        self.add_employee(firstname, lastname)
        self.switch_employee_detail_page("Personal Details")
        page_ele = self.get_element(self.page_head)
        if page_ele is not None:
            Log.info("Arrive Pesonal Details page!")

    def open_personal_details_via_employee_list(self, firstname, lastname):
        self.click_employee_to_edit(firstname, lastname)
        self.switch_employee_detail_page("Personal Details")
        page_ele = self.get_element(self.page_head)
        if page_ele is not None:
            Log.info("Arrive Pesonal Details page!")

    def edit_personal_details_name(self,firstname, middlename, lastname):
        self.click(self.edit_btn)
        self.input_text(firstname, self.first_name)
        self.input_text(middlename, self.middle_name)
        self.input_text(lastname, self.last_name)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Edit name for personal details successfully!")

    def edit_personal_details_id(self, emp_id, oth_id, lic_num, lic_exp_date):
        self.click(self.edit_btn)
        self.input_text(emp_id, self.employee_id)
        self.input_text(oth_id, self.other_id)
        self.input_text(lic_num, self.license_number)
        self.input_text(lic_exp_date, self.license_expiry_date)
        #self.input_text(ssn_num, self.ssn_number)
        #self.input_text(sin_num, self.sin_number)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Edit id information for personal details successfully!")

    def edit_personal_details_basic_information(self,gender_sta, marital_sta, nation, DOB):
        self.click(self.edit_btn)
        gender = self.gender_ele.format(gender_sta)
        self.click(('xpath', gender))
        self.set_combox_value(marital_sta, self.marital_status)
        self.set_combox_value(nation, self.nationality)
        self.input_text(DOB, self.date_of_birth)
        self.click(self.save_btn)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Edit basic information for personal details successfully!")

    def edit_personal_details_cancel_add_attahment_comments(self, attachment, comments):
        self.click(self.add_btn)
        self.upload_file(attachment, self.select_file)
        self.input_text(comments, self.comment)
        self.click(self.cancel_btn)
        Log.info("Cancel add attachment and comments!")

    def edit_personal_details_add_attachment_comments(self, attachment, comments):
        self.click(self.add_btn)
        self.upload_file(attachment, self.select_file)
        self.input_text(comments, self.comment)
        self.click(self.upload_btn)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Add attachment and comments for personal details successfully!")

    def edit_personal_details_edit_commentsonly(self, attachment, comments):
        self.click(self.edit_attachment_btn)
        self.upload_file(attachment, self.select_file)
        self.input_text(comments, self.comment)
        self.click(self.save_comment_only)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Edit comments for personal details successfully!")

    def edit_personal_details_cancel_edit_attachment_comments(self, attachment, comments):
        self.click(self.edit_attachment_btn)
        self.upload_file(attachment, self.select_file)
        self.input_text(comments, self.comment)
        self.click(self.cancel_btn)
        Log.info("Cancel edit attachemnt and comments!")

    def edit_personal_details_edit_attachment_comments(self, attachment, comments):
        self.click(self.edit_attachment_btn)
        self.upload_file(attachment, self.select_file)
        self.input_text(comments, self.comment)
        self.click(self.upload_btn)
        assert "Successfully Saved" in self.get_element_text(self.flag)
        Log.info("Edit attachment and comments for personal details successfully!")

    def edit_personal_details_delete_record_for_attachment(self, filename):
        if filename == self.get_element_text(self.file_name):
            self.click(self.check_box)
            self.click(self.delete_attachment_btn)
            assert "Successfully Deleted" in self.get_element_text(self.flag)
            Log.info("The record for the file name %s is deleted!" % filename)
        else:
            Log.info("Not find the record for the file name %s!" % filename)

    def edit_personal_details_delete_all_records(self):
        self.click(self.check_allbox)
        self.click(self.delete_attachment_btn)
        assert "Successfully Deleted" in self.get_element_text(self.flag)
        Log.info("All records are deleted!")