from django.db import models

# Create your models here.

class Account(models.Model):

	firstname = models.CharField(max_length=255, blank=True, null=True)

	lastname = models.CharField(max_length=255, blank=True, null=True)

	username = models.CharField(max_length=255, blank=True, null=True)

	email = models.CharField(max_length=255, blank=True, null=True)

	# phone = models.CharField(max_length=255, blank=True, null=True)

	# address = models.CharField(max_length=255, blank=True, null=True)

	password = models.CharField(max_length=255, blank=True, null=True, default="")

	image = models.CharField(max_length=255, blank=True, null=True)

	role = models.CharField(max_length=255, blank=True, null=True, default="")



class Batch(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True, default="")

	batch_type = models.CharField(max_length=255, blank=True, null=True, default="")



class Invoice(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True)

	system = models.CharField(max_length=255, blank=True, null=True)

	license = models.CharField(max_length=255, blank=True, null=True)

	age = models.CharField(max_length=255, blank=True, null=True)

	discipline = models.CharField(max_length=255, blank=True, null=True)

	modes = models.CharField(max_length=255, blank=True, null=True)

	tc = models.CharField(max_length=255, blank=True, null=True)

	company = models.CharField(max_length=255, blank=True, null=True)

	branch_id = models.CharField(max_length=255, blank=True, null=True)

	employee_short_name = models.CharField(max_length=255, blank=True, null=True)

	cust_alph = models.CharField(max_length=255, blank=True, null=True)

	customer_name = models.CharField(max_length=255, blank=True, null=True)

	invoice_number = models.CharField(max_length=255, blank=True, null=True)

	straight_time_hours = models.CharField(max_length=255, blank=True, null=True)

	hourly_bill_rate = models.CharField(max_length=255, blank=True, null=True)

	overtime_hours = models.CharField(max_length=255, blank=True, null=True)

	sp_bill = models.CharField(max_length=255, blank=True, null=True)

	total_bill_amount = models.CharField(max_length=255, blank=True, null=True)

	invoice_date = models.CharField(max_length=255, blank=True, null=True)

	week_ending_date = models.CharField(max_length=255, blank=True, null=True)

	invoice_reference = models.CharField(max_length=255, blank=True, null=True)

	workers_comp_code = models.CharField(max_length=255, blank=True, null=True)

	job_description = models.CharField(max_length=255, blank=True, null=True)

	customer_po = models.CharField(max_length=255, blank=True, null=True)

	b_w_location_code = models.CharField(max_length=255, blank=True, null=True)

	address_1 = models.CharField(max_length=255, blank=True, null=True)

	spcl_paybill_de_code = models.CharField(max_length=255, blank=True, null=True)

	special_paybill_qty = models.CharField(max_length=255, blank=True, null=True)

	special_bill_rate = models.CharField(max_length=255, blank=True, null=True)



class TimeCard_KT(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True)

	uid = models.CharField(max_length=255, blank=True, null=True)

	time_card_id = models.CharField(max_length=255, blank=True, null=True)

	authorization = models.CharField(max_length=255, blank=True, null=True)

	bill_mode = models.CharField(max_length=255, blank=True, null=True)

	bill_rate = models.CharField(max_length=255, blank=True, null=True)

	billable = models.CharField(max_length=255, blank=True, null=True)

	case_manager_first_name = models.CharField(max_length=255, blank=True, null=True)

	case_manager_last_name = models.CharField(max_length=255, blank=True, null=True)

	checkin_time = models.CharField(max_length=255, blank=True, null=True)

	checkout_time = models.CharField(max_length=255, blank=True, null=True)

	client_first_name = models.CharField(max_length=255, blank=True, null=True)

	client_last_name = models.CharField(max_length=255, blank=True, null=True)

	client_dob = models.CharField(max_length=255, blank=True, null=True)

	clinician_first_name = models.CharField(max_length=255, blank=True, null=True)

	clinician_last_name = models.CharField(max_length=255, blank=True, null=True)

	clinician_id = models.CharField(max_length=255, blank=True, null=True)

	clinician_payroll_group = models.CharField(max_length=255, blank=True, null=True)

	clinician_payroll_id = models.CharField(max_length=255, blank=True, null=True)

	clinician_payroll_rule = models.CharField(max_length=255, blank=True, null=True)

	clinician_skills = models.CharField(max_length=255, blank=True, null=True)

	clinician_ssn = models.CharField(max_length=255, blank=True, null=True)

	cosign_staff_first_name = models.CharField(max_length=255, blank=True, null=True)

	cosign_staff_last_name = models.CharField(max_length=255, blank=True, null=True)

	edited_hours = models.CharField(max_length=255, blank=True, null=True)

	episode_duration = models.CharField(max_length=255, blank=True, null=True)

	episode_number = models.CharField(max_length=255, blank=True, null=True)

	episode_start_date = models.CharField(max_length=255, blank=True, null=True)

	episode_end_date = models.CharField(max_length=255, blank=True, null=True)

	has_split_schedules = models.CharField(max_length=255, blank=True, null=True)

	hcpcs_code = models.CharField(max_length=255, blank=True, null=True)

	location = models.CharField(max_length=255, blank=True, null=True)

	marital_status = models.CharField(max_length=255, blank=True, null=True)

	medicaid = models.CharField(max_length=255, blank=True, null=True)

	patient_id = models.CharField(max_length=255, blank=True, null=True)

	payroll = models.CharField(max_length=255, blank=True, null=True)

	payroll_mode = models.CharField(max_length=255, blank=True, null=True)

	payroll_rate = models.CharField(max_length=255, blank=True, null=True)

	payrolled = models.CharField(max_length=255, blank=True, null=True)

	schedule_status = models.CharField(max_length=255, blank=True, null=True)

	units = models.CharField(max_length=255, blank=True, null=True)

	visit_date = models.CharField(max_length=255, blank=True, null=True)

	client_lob = models.CharField(max_length=255, blank=True, null=True)

	insurance_id = models.CharField(max_length=255, blank=True, null=True)

	payer = models.CharField(max_length=255, blank=True, null=True)

	clinician_discipline = models.CharField(max_length=255, blank=True, null=True)

	service = models.CharField(max_length=255, blank=True, null=True)

	employment_type = models.CharField(max_length=255, blank=True, null=True)

	invoice_no = models.CharField(max_length=255, blank=True, null=True)

	miles = models.CharField(max_length=255, blank=True, null=True)

	visit_id = models.CharField(max_length=255, blank=True, null=True)

	payroll_batch_id = models.CharField(max_length=255, blank=True, null=True)

	authorization = models.CharField(max_length=255, blank=True, null=True)

	bill_mode = models.CharField(max_length=255, blank=True, null=True)

	shift = models.CharField(max_length=255, blank=True, null=True)


class TimeCard_HB(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True, default="")

	time_card_id = models.CharField(max_length=255, blank=True, null=True, default="")

	batch = models.CharField(max_length=255, blank=True, null=True, default="")

	worker_name = models.CharField(max_length=255, blank=True, null=True, default="")

	primary_job_desc = models.CharField(max_length=255, blank=True, null=True, default="")

	standard_pay_method = models.CharField(max_length=255, blank=True, null=True, default="")

	payroll_branch = models.CharField(max_length=255, blank=True, null=True, default="")

	client_branch = models.CharField(max_length=255, blank=True, null=True, default="")

	client_name = models.CharField(max_length=255, blank=True, null=True, default="")

	client_state = models.CharField(max_length=255, blank=True, null=True, default="")

	service_date = models.CharField(max_length=255, blank=True, null=True, default="")

	shift = models.CharField(max_length=255, blank=True, null=True, default="")

	drive_start_time = models.CharField(max_length=255, blank=True, null=True, default="")

	in_home_nva_start_time = models.CharField(max_length=255, blank=True, null=True, default="")

	in_home_nva_end_time = models.CharField(max_length=255, blank=True, null=True, default="")

	service_type = models.CharField(max_length=255, blank=True, null=True, default="")

	rate = models.CharField(max_length=255, blank=True, null=True, default="")

	service_code_rate_type = models.CharField(max_length=255, blank=True, null=True, default="")

	total_time = models.CharField(max_length=255, blank=True, null=True, default="")

	qty = models.CharField(max_length=255, blank=True, null=True, default="")

	payroll_transmittal_group = models.CharField(max_length=255, blank=True, null=True, default="")

	prod_points = models.CharField(max_length=255, blank=True, null=True, default="")

	travel_am = models.CharField(max_length=255, blank=True, null=True, default="")

	travel_tf = models.CharField(max_length=255, blank=True, null=True, default="")

	travel_cv = models.CharField(max_length=255, blank=True, null=True, default="")

	mileage_payment_method = models.CharField(max_length=255, blank=True, null=True, default="")

	service_payable = models.CharField(max_length=255, blank=True, null=True, default="")

	service_payment_method = models.CharField(max_length=255, blank=True, null=True, default="")

	worker_id = models.CharField(max_length=255, blank=True, null=True, default="")

	full_time = models.CharField(max_length=255, blank=True, null=True, default="")

	default_milleage_payment_method = models.CharField(max_length=255, blank=True, null=True, default="")

	worker_class = models.CharField(max_length=255, blank=True, null=True, default="")

	worker_category = models.CharField(max_length=255, blank=True, null=True, default="")

	payroll_department = models.CharField(max_length=255, blank=True, null=True, default="")

	payroll_number = models.CharField(max_length=255, blank=True, null=True, default="")

	expected_prod_points = models.CharField(max_length=255, blank=True, null=True, default="")

	team = models.CharField(max_length=255, blank=True, null=True, default="")

	municipality_code = models.CharField(max_length=255, blank=True, null=True, default="")

	date_of_hire = models.CharField(max_length=255, blank=True, null=True, default="")

	uid = models.CharField(max_length=255, blank=True, null=True, default="")


class ReconKeys_KT(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True)

	key_id = models.CharField(max_length=255, blank=True, null=True)

	authorization = models.CharField(max_length=255, blank=True, null=True)

	bill_rate = models.CharField(max_length=255, blank=True, null=True)

	billable = models.CharField(max_length=255, blank=True, null=True)

	case_manager_first_name = models.CharField(max_length=255, blank=True, null=True)

	case_manager_last_name = models.CharField(max_length=255, blank=True, null=True)

	checkin_time = models.CharField(max_length=255, blank=True, null=True)

	checkout_time = models.CharField(max_length=255, blank=True, null=True)

	client_first_name = models.CharField(max_length=255, blank=True, null=True)

	client_last_name = models.CharField(max_length=255, blank=True, null=True)

	client_dob = models.CharField(max_length=255, blank=True, null=True)

	clinician_first_name = models.CharField(max_length=255, blank=True, null=True)

	clinician_last_name = models.CharField(max_length=255, blank=True, null=True)

	clinician_id = models.CharField(max_length=255, blank=True, null=True)

	clinician_payroll_group = models.CharField(max_length=255, blank=True, null=True)

	clinician_payroll_id = models.CharField(max_length=255, blank=True, null=True)	

	clinician_payroll_rule = models.CharField(max_length=255, blank=True, null=True)

	clinician_skills = models.CharField(max_length=255, blank=True, null=True)

	clinician_ssn = models.CharField(max_length=255, blank=True, null=True)

	cosign_staff_first_name = models.CharField(max_length=255, blank=True, null=True)

	cosign_staff_last_name = models.CharField(max_length=255, blank=True, null=True)

	edited_hours = models.CharField(max_length=255, blank=True, null=True)

	episode_duration = models.CharField(max_length=255, blank=True, null=True)

	episode_number = models.CharField(max_length=255, blank=True, null=True)

	episode_start_date = models.CharField(max_length=255, blank=True, null=True)

	episode_end_date = models.CharField(max_length=255, blank=True, null=True)

	has_split_schedules = models.CharField(max_length=255, blank=True, null=True)

	hcpcs_code = models.CharField(max_length=255, blank=True, null=True)

	location = models.CharField(max_length=255, blank=True, null=True)

	material_status = models.CharField(max_length=255, blank=True, null=True)

	medicaid = models.CharField(max_length=255, blank=True, null=True)

	patient_id = models.CharField(max_length=255, blank=True, null=True)

	payroll = models.CharField(max_length=255, blank=True, null=True)	

	payroll_mode = models.CharField(max_length=255, blank=True, null=True)

	payroll_rate = models.CharField(max_length=255, blank=True, null=True)

	payrolled = models.CharField(max_length=255, blank=True, null=True)

	schedule_status = models.CharField(max_length=255, blank=True, null=True)

	units = models.CharField(max_length=255, blank=True, null=True)

	visit_date = models.CharField(max_length=255, blank=True, null=True)

	client_lob = models.CharField(max_length=255, blank=True, null=True)

	insurance_id = models.CharField(max_length=255, blank=True, null=True)

	payer = models.CharField(max_length=255, blank=True, null=True)

	clinician_discipline = models.CharField(max_length=255, blank=True, null=True)

	service = models.CharField(max_length=255, blank=True, null=True)

	employment_type = models.CharField(max_length=255, blank=True, null=True)

	invoice_no = models.CharField(max_length=255, blank=True, null=True)

	miles = models.CharField(max_length=255, blank=True, null=True)

	visit_id = models.CharField(max_length=255, blank=True, null=True)

	payroll_batch_id = models.CharField(max_length=255, blank=True, null=True)

	shift = models.CharField(max_length=255, blank=True, null=True)

	visit_split_id = models.CharField(max_length=255, blank=True, null=True)

class ReconKeys_HB(models.Model):

	batch_no = models.CharField(max_length=255, blank=True, null=True)

	key_id = models.CharField(max_length=255, blank=True, null=True)

	row_id = models.CharField(max_length=255, blank=True, null=True)

	branch = models.CharField(max_length=255, blank=True, null=True)

	funding_source = models.CharField(max_length=255, blank=True, null=True)

	post_date = models.CharField(max_length=255, blank=True, null=True)

	date_created = models.CharField(max_length=255, blank=True, null=True)

	client_facility_name = models.CharField(max_length=255, blank=True, null=True)

	shift_date = models.CharField(max_length=255, blank=True, null=True)

	invoice = models.CharField(max_length=255, blank=True, null=True)

	description = models.CharField(max_length=255, blank=True, null=True)

	rev_code = models.CharField(max_length=255, blank=True, null=True)

	hcpcs_cpt_code = models.CharField(max_length=255, blank=True, null=True)

	quantity_units = models.CharField(max_length=255, blank=True, null=True)

	orig_charge = models.CharField(max_length=255, blank=True, null=True)

	adjustments = models.CharField(max_length=255, blank=True, null=True)

	amount = models.CharField(max_length=255, blank=True, null=True)

	balance = models.CharField(max_length=255, blank=True, null=True)


class Payment(models.Model):

	# batch_id = models.CharField(max_length=255, blank=True, null=True)

	batch_no = models.ForeignKey(Batch, on_delete=models.CASCADE)

	check = models.CharField(max_length=255, blank=True, null=True)

	recon_key = models.CharField(max_length=255, blank=True, null=True)

	check_amount = models.CharField(max_length=255, blank=True, null=True)




	






		







