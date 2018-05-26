from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.template import RequestContext
from django.contrib.auth.models import *
from mydemo.models import *
from functools import wraps
from django.shortcuts import render
import datetime
from django.http import HttpResponse
from myProject import settings
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook
from openpyxl import Workbook 
from openpyxl.styles import colors
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
from django.db.models import Count
from django.forms.models import model_to_dict
import os
import pdb

# Create your views here.

def index(request):
    return HttpResponse("Welcome visit our page")

def login_required():
    def login_decorator(function):
        @wraps(function)
        def wrapped_function(request):

            # if a user is not authorized, redirect to login page
            if 'user' not in request.session or request.session['user'] is None:
                return redirect("/")
            # otherwise, go on the request
            else:
                return function(request)

        return wrapped_function

    return login_decorator


# login view
def login(request):
    error = 'none'
    request.session['user'] = None

    if 'username' in request.POST:

        # get username and password from request.
        username = request.POST['username']
        password = request.POST['password']
        # check whether the user is in database or not
        if username == settings.ADMIN_NAME and password == settings.ADMIN_PASSWORD:
            request.session['user'] = {
                # "id": user[0].id,
                "username": settings.ADMIN_NAME, #user[0].email,
                "password": settings.ADMIN_PASSWORD, #user[0].name.split(" ")[0],
                "role": "admin"
            }

            return redirect("/home")
        else :
            error = 'block'

        user = Account.objects.filter(username=username, password=password) or Account.objects.filter(email=username, password=password)

        if len(user) > 0:
            request.session['user'] = {
                # "id": user[0].id,
                "firstname" : user[0].firstname,
                "lastname" : user[0].lastname,
                "username": user[0].username,
                "email": user[0].email,
                "password": user[0].password,
                "image" : user[0].image,
                "role" : "client",
            }

            return redirect("/home")
        else:
            error = 'block'

    return render(request, 'login.html', locals())

    # return render_to_response('login.html', {'error':error}, context_instance=RequestContext(request))

def logout(request):

    request.session['user'] = None

    request.session['input_invoice_arr'] = '[]'

    request.session['input_payment_arr'] = '[]'

    request.session['reconkeys_arr'] = '[]'

    request.session['reconkeys_hb_arr'] = '[]'

    request.session['timecard_kt_arr'] = '[]'

    request.session['timecard_hb_arr'] = '[]' 

    request.session['invoice_arr'] = '[]'   

    return redirect("/")


def clear_data(request):

    if 'refresh' in request.POST and request.POST['refresh'] == 'invoice_raw_data':

        request.session['invoice_arr'] = '[]'

        request.session['invoice_batch_no'] = ''

        return redirect('/invoice_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'invoice_simple_data':

        request.session['input_invoice_arr'] = '[]'

        return redirect('/invoice_simple_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'input_payment_data':

        request.session['input_payment_arr'] = '[]'

        return redirect('/payment_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'reconkeys_kt_data':

        request.session['reconkeys_arr'] = '[]'

        return redirect('/reconkeys_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'reconkeys_hb_data':

        request.session['reconkeys_hb_arr'] = '[]'

        return redirect('/reconkeys_hb_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'timecard_kt_data':

        request.session['timecard_kt_arr'] = '[]'

        return redirect('/timecard_board')

    if 'refresh' in request.POST and request.POST['refresh'] == 'timecard_hb_data':

        request.session['timecard_hb_arr'] = '[]'

        return redirect('/timecard_hb_board')


def search_batch_no(request):

    if 'selected_batch_no' in request.POST:

        selected_invoices = Invoice.objects.filter(batch_no=str(request.POST['selected_batch_no']))

        invoice_arr = []

        for invoice in selected_invoices:

            invoice_arr.append(model_to_dict(invoice))

        request.session['invoice_arr'] = json.dumps(invoice_arr)

        request.session['invoice_batch_no'] = str(request.POST['selected_batch_no'])
            
    return redirect('/invoice_board')



def post_data(request):

    pass

    # batch_no = request.session.get('batch_no', '')

    # if batch_no != '':

    #     batch = Batch()

    #     batch.batch_no = batch_no

    #     batch.save()





def main(request):
    # clients = Client.objects.all().order_by("-created_on")
    return render(request, 'black.html')
    # return render_to_response('blank.html', locals(), context_instance=RequestContext(request))


def home(request):

    # latest_batch = Batch.objects.filter().latest('batch_no')

    # batch_no = 'BH'+str(int(latest_batch.batch_no.replace('BH',''))+1)

    # request.session['batch_no'] = batch_no

    # request.session['input_invoice_arr'] = '[]'

    # request.session['input_payment_arr'] = '[]'

    # request.session['reconkeys_arr'] = '[]'

    # request.session['reconkeys_hb_arr'] = '[]'

    # request.session['timecard_kt_arr'] = '[]'

    # request.session['timecard_hb_arr'] = '[]' 

    # request.session['invoice_arr'] = '[]'   


    return render(request, 'home.html')


def invoice_board(request):

    inv_bhs = Invoice.objects.values('batch_no').annotate(count=Count('batch_no'))

    invoice_batch_no_arr = []

    for batch in inv_bhs:

        invoice_batch_no_arr.append(batch['batch_no'])

    request.session['invoice_batch_no_arr'] = invoice_batch_no_arr


    if request.method == 'POST' and request.FILES:

        latest_batch = ''

        try:

            latest_batch = Invoice.objects.latest('batch_no').batch_no

        except:

            latest_batch = 'BH-INV-0000'

        num = str(int(latest_batch.split('-')[2])+1)

        if len(num) < 4:

            for ind in range(0, 4-len(num)):

                num = '0'+num

        batch_no = '-'.join(latest_batch.split('-')[:2])+'-'+num

        request.session['invoice_batch_no'] = batch_no

        invoice_arr = []

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading Invoice Data ...')

        input_invoice_data_sheet = workbook[workbook.sheetnames[0]]

        input_invoice_data_col_max_count = 0

        invoice_row = 1

        invoice_header = [
            'company', 
            'branch_id', 
            'employee_short_name', 
            'cust_alph', 
            'customer_name', 
            'invoice_number', 
            'straight_time_hours', 
            'hourly_bill_rate', 
            'overtime_hours', 
            'sp_bill', 
            'total_bill_amount', 
            'invoice_date', 
            'week_ending_date', 
            'invoice_reference', 
            'workers_comp_code', 
            'job_description', 
            'customer_po', 
            'b_w_location_code', 
            'address_1', 
            'spcl_paybill_de_code', 
            'special_paybill_qty', 
            'special_bill_rate'
         ]

        for invoice in input_invoice_data_sheet.rows:

            try:

                data = {'batch_no' : batch_no}

                for invoice_col in range(0, len(invoice)) :

                    data[invoice_header[invoice_col]] = str(invoice[invoice_col].value)

                if invoice_row > 1:

                    items = data['invoice_reference'].split('@')

                    try:

                        data['system'] = items[0]

                        data['license'] = items[1]

                        data['age'] = items[2]

                        data['discipline'] = items[3]

                        data['modes'] = items[4]

                        data['tc'] = items[5]

                    except:

                        pass

                    invoice_arr.append(data)

                    check = Invoice.objects.filter(invoice_reference=data['invoice_reference'])

                    if len(check) == 0:

                        invoice_model = Invoice(**data)

                        invoice_model.save()

                    else :

                        check.update(**data)

                invoice_row += 1

            except:

                pass

        request.session['invoice_arr'] = json.dumps(invoice_arr)

        # data_table = Template("""
        #     """)
        # html = data_table.render(Context({'invoice_arr': json.loads(request.session.get('invoice_arr', '[]'))}))

        return HttpResponse("success")


    else:

        return render(request, 'invoice/index.html',
            {

                'invoice_arr' : json.loads(request.session.get('invoice_arr', '[]')),

                'invoice_batch_no_arr' : request.session.get('invoice_batch_no_arr', '[]'),

                'invoice_batch_no' : request.session.get('invoice_batch_no', '[]')

            })



def invoice_simple_board(request):

    if request.method == 'POST' and request.FILES:

        invoice_arr = []

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading Invoice Data ...')

        invoice_data_sheet = workbook[workbook.sheetnames[0]]        

        invoice_header = [
           'invoice',
           'invoice_amount',
           'recon_key'
         ]        

        input_invoice_arr = []

        invoice_row = 1

        for invoice in invoice_data_sheet.rows:

            try:

                amount = 0

                recon_key = []

                if invoice[1].value != None and invoice[1].value != '':

                    amount = str(invoice[1].value)

                for cnt in range(2, len(invoice) ) :

                    if invoice[cnt].value != None and invoice[cnt].value != '':

                        recon_key.append( str(invoice[cnt].value).replace(' ', '').replace('-', '').strip() )

                item = {

                    'invoice' : str(invoice[0].value),

                    'invoice_amount' : amount,

                    'recon_key' : recon_key,

                }

                if invoice_row > 1:

                    input_invoice_arr.append( item )

                invoice_row += 1

            except :

                pass

        # pdb.set_trace()

        request.session['input_invoice_arr'] = json.dumps(input_invoice_arr)

        # data_table = Template("""
        #     """)
        # html = data_table.render(Context({'invoice_arr': json.loads(request.session.get('invoice_arr', '[]'))}))

        return HttpResponse("success")

    else:
        
        return render(request, 'invoice/invoice_simple.html',
            {

                'invoice_arr' : json.loads(request.session.get('input_invoice_arr', '[]')),

            })



def timecard_board(request):

    # if 'refresh' in request.POST:

    #     request.session['timecard_kt_arr'] = '[]'           

    if request.method == 'POST' and request.FILES:

        latest_batch = ''

        try:

            latest_batch = TimeCard_KT.objects.latest('batch_no').batch_no

        except:

            latest_batch = 'BH-KT-TC-0000'

        num = str(int(latest_batch.split('-')[3])+1)

        if len(num) < 4:

            for ind in range(0, 4-len(num)):

                num = '0'+num

        batch_no = '-'.join(latest_batch.split('-')[:3])+'-'+num

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading KT Time Card Time Card Data ...')

        kt_tc_raw_sheet = workbook[workbook.sheetnames[0]]

        timecard_kt_arr = []

        kt_tc_row = 1

        timecard_header = [
            'time_card_id',
            'authorization',
            'bill_mode',
            'bill_rate',
            'billable',
            'case_manager_first_name',
            'case_manager_last_name',
            'checkin_time',
            'checkout_time',
            'client_first_name',
            'client_last_name',
            'client_dob',
            'clinician_first_name',
            'clinician_last_name',
            'clinician_id',
            'clinician_payroll_group',
            'clinician_payroll_id',
            'clinician_payroll_rule',
            'clinician_skills',
            'clinician_ssn',
            'cosign_staff_first_name',
            'cosign_staff_last_name',
            'edited_hours',
            'episode_duration',
            'episode_number',
            'episode_start_date',
            'episode_end_date',
            'has_split_schedules',
            'hcpcs_code',
            'location',
            'marital_status',
            'medicaid',
            'patient_id',
            'payroll',
            'payroll_mode',
            'payroll_rate',
            'payrolled',
            'schedule_status',
            'units',
            'visit_date',
            'client_lob',
            'insurance_id',
            'payer',
            'clinician_discipline',
            'service',
            'employment_type',
            'invoice_no',
            'miles',
            'visit_id',
            'payroll_batch_id',
            'authorization_2',
            'bill_mode_2',
            'shift',
            'uid'
        ]


        for kt_tc_raw in kt_tc_raw_sheet.rows:

            try:

                data = { 'batch_no' : batch_no } 

                for kt_tc_col in range(0, len(kt_tc_raw) ) :

                    data[timecard_header[kt_tc_col]] = kt_tc_raw[kt_tc_col].value
                    

                temp = datetime.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

                date = ''

                try:

                    delta = data['visit_date'] - temp

                    date = str(int(float(delta.days) + (float(delta.seconds) / 86400)))

                except : 

                    date = '0'
                
                time = ''

                try:

                    time = float(float(data['checkin_time'].hour)+float(data['checkin_time'].minute)/60+float(data['checkin_time'].second)/3600)/24     

                    if time == 0:

                        time = '0'

                except :

                    time = '0'

                uid = str(data['clinician_ssn']) + '@' + str(data['location']) + '@' + str(data['patient_id']) + '@' + date + '@' + str(time) + '@' + str(data['service'])

                data['uid'] = uid.strip()

                for header in timecard_header:

                    data[header] = str(data[header])

                if kt_tc_row > 1 and data['time_card_id'] != '':

                    timecard_kt_arr.append(data)

                    check = TimeCard_KT.objects.filter(time_card_id=data['time_card_id'])

                    if len(check) == 0:

                        timecard_kt_model = TimeCard_KT(**data)

                        timecard_kt_model.save()

                    else :

                        check.update(**data)

                kt_tc_row += 1

            except:

                pass


        request.session['timecard_kt_arr'] = json.dumps(timecard_kt_arr)

        # data_table = Template("""
        #     """)
        # html = data_table.render(Context({'timecard_kt_arr': json.loads(request.session.get('timecard_kt_arr', '[]'))}))

        return HttpResponse("success")

    else:
        
        return render(request, 'timecard/timecard_kt.html',
            {

                'timecard_kt_arr' : json.loads(request.session.get('timecard_kt_arr', '[]')),

            })


def timecard_hb_board(request):

    # if 'refresh' in request.POST:

    #     request.session['timecard_kt_arr'] = '[]'           

    if request.method == 'POST' and request.FILES:

        latest_batch = ''

        try:

            latest_batch = TimeCard_HB.objects.latest('batch_no').batch_no

        except:

            latest_batch = 'BH-KT-HB-0000'

        num = str(int(latest_batch.split('-')[3])+1)

        if len(num) < 4:

            for ind in range(0, 4-len(num)):

                num = '0'+num

        batch_no = '-'.join(latest_batch.split('-')[:3])+'-'+num


        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading HB Time Card Time Card Data ...')

        hb_tc_raw_sheet = workbook[workbook.sheetnames[0]]

        timecard_hb_arr = []

        hb_tc_row = 1

        timecard_header = [
            'time_card_id',
            'batch',
            'worker_name',
            'primary_job_desc',
            'standard_pay_method',
            'payroll_branch',
            'client_branch',
            'client_name',
            'client_state',
            'service_date',
            'shift',
            'drive_start_time',
            'in_home_nva_start_time',
            'in_home_nva_end_time',
            'service_type',
            'rate',
            'service_code_rate_type',
            'total_time',
            'qty',
            'payroll_transmittal_group',
            'prod_points',
            'travel_am',
            'travel_tf',
            'travel_cv',
            'mileage_payment_method',
            'service_payable',
            'service_payment_method',
            'worker_id',
            'full_time',
            'default_milleage_payment_method',
            'worker_class',
            'worker_category',
            'payroll_department',
            'payroll_number',
            'expected_prod_points',
            'team',
            'municipality_code',
            'date_of_hire',
            'uid'
        ]

        for hb_tc_raw in hb_tc_raw_sheet.rows:

            data = { 'batch_no' : batch_no } 

            for hb_tc_col in range(0, len(hb_tc_raw) ) :

                data[timecard_header[hb_tc_col]] = hb_tc_raw[hb_tc_col].value

            temp = datetime.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

            date = ''

            try:

                delta = data['service_date'] - temp

                date = str(int(float(delta.days) + (float(delta.seconds) / 86400)))

            except : 

                date = '0'

            uid = str(data['client_branch']) + '@' + date + '@' + str(data['service_type']) + '@' + str(data['client_name']).replace(' ', '').replace('.', '').strip()

            data['uid'] = uid.strip()

            for header in timecard_header:

                data[header] = str(data[header])

            if hb_tc_row > 1 and data['time_card_id'] != '' :

                timecard_hb_arr.append(data)

                check = TimeCard_HB.objects.filter(time_card_id=data['time_card_id'])

                if len(check) == 0:

                    timecard_hb_model = TimeCard_HB(**data)

                    timecard_hb_model.save()

                else :

                    check.update(**data)

            hb_tc_row += 1


        request.session['timecard_hb_arr'] = json.dumps(timecard_hb_arr)

        # data_table = Template("""
        #     """)
        # html = data_table.render(Context({'timecard_kt_arr': json.loads(request.session.get('timecard_kt_arr', '[]'))}))

        return HttpResponse("success")

    else:
        
        return render(request, 'timecard/timecard_hb.html',
            {

                'timecard_hb_arr' : json.loads(request.session.get('timecard_hb_arr', '[]')),

            })


def reconkeys_board(request):

    # if 'refresh' in request.POST:

    #     request.session['reconkeys_arr'] = '[]'      

    if request.method == 'POST' and request.FILES:

        latest_batch = ''

        try:

            latest_batch = ReconKeys_KT.objects.latest('batch_no').batch_no

        except:

            latest_batch = 'BH-KT-RK-0000'            

        num = str(int(latest_batch.split('-')[3])+1)

        if len(num) < 4:

            for ind in range(0, 4-len(num)):

                num = '0'+num

        batch_no = '-'.join(latest_batch.split('-')[:3])+'-'+num

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading KT RK Data ...')

        kt_key_raw_sheet = workbook[workbook.sheetnames[0]]

        reconkeys_arr = []

        reconkeys_header = [
            'authorization',
            'bill_mode',
            'bill_rate',
            'billable',
            'case_manager_first_name',
            'case_manager_last_name',
            'checkin_time',
            'checkout_time',
            'client_first_name',
            'client_last_name',
            'client_dob',
            'clinician_first_name',
            'clinician_last_name',
            'clinician_id',
            'clinician_payroll_group',
            'clinician_payroll_id', 
            'clinician_payroll_rule',
            'clinician_skills',
            'clinician_ssn',
            'cosign_staff_first_name',
            'cosign_staff_last_name',
            'edited_hours',
            'episode_duration',
            'episode_number',
            'episode_start_date',
            'episode_end_date',
            'has_split_schedules',
            'hcpcs_code',
            'location',
            'material_status',
            'medicaid',
            'patient_id',
            'payroll',  
            'payroll_mode',
            'payroll_rate',
            'payrolled',
            'schedule_status',
            'units',
            'visit_date',
            'client_lob',
            'insurance_id',
            'payer',
            'clinician_discipline',
            'service',
            'employment_type',
            'invoice_no',
            'miles',
            'visit_id',
            'payroll_batch_id',
            'shift',
            'visit_split_id',
            'key_id'
        ]

        kt_key_row = 1

        for kt_key_raw in kt_key_raw_sheet.rows:

            try:

                data = { 'batch_no' : batch_no } 

                for kt_key_col in range(0, len(kt_key_raw) ) :

                    data[reconkeys_header[kt_key_col]] = kt_key_raw[kt_key_col].value

                temp = datetime.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

                date = ''

                try:

                    delta = data['visit_date'] - temp

                    date = str(int(float(delta.days) + (float(delta.seconds) / 86400)))

                except : 

                    date = '0'

                key_id = str(data['clinician_ssn']) + '@' + str(data['location']) + '@' + str(data['patient_id']) + '@' + date + '@' + str(data['checkin_time']) + '@' + str(data['service'])

                data['key_id'] = key_id.strip()

                for header in reconkeys_header:

                    data[header] = str(data[header])

                if kt_key_row > 1 and data['insurance_id'] != '':

                    reconkeys_arr.append(data)

                    check = ReconKeys_KT.objects.filter(key_id=data['key_id'])

                    if len(check) == 0:

                        reconkeys_kt_model = ReconKeys_KT(**data)

                        reconkeys_kt_model.save()

                    else :

                        check.update(**data)


                kt_key_row += 1


            except :

                pass

        request.session['reconkeys_arr'] = json.dumps(reconkeys_arr)

        # data_table = Template("""
        #     """)

        # html = data_table.render(Context({'reconkeys_arr': json.loads(request.session.get('reconkeys_arr', '[]'))}))

        if len(reconkeys_arr) == 0:

            request.session['msg'] = 'Invalid Format'

        else :

            request.session['msg'] = ''            

        return HttpResponse("success")

    else:
        
        return render(request, 'reconkeys/reconkeys_kt.html',
            {

                'reconkeys_arr' : json.loads(request.session.get('reconkeys_arr', '[]')),

                'msg' : request.session.get('msg', '')

            })


def reconkeys_hb_board(request):

    # if 'refresh' in request.POST:

    #     request.session['reconkeys_arr'] = '[]'      

    if request.method == 'POST' and request.FILES:

        latest_batch = ''

        try:

            latest_batch = ReconKeys_HB.objects.latest('batch_no').batch_no

        except:

            latest_batch = 'BH-HB-RK-0000'            

        num = str(int(latest_batch.split('-')[3])+1)

        if len(num) < 4:

            for ind in range(0, 4-len(num)):

                num = '0'+num

        batch_no = '-'.join(latest_batch.split('-')[:3])+'-'+num

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        print(' Loading HB RK Data ...')

        hb_key_raw_sheet = workbook[workbook.sheetnames[0]]

        reconkeys_hb_arr = []

        reconkeys_header = [
            'row_id',
            'branch',
            'funding_source',
            'post_date',
            'date_created',
            'client_facility_name',
            'shift_date',
            'invoice',
            'description',
            'rev_code',
            'hcpcs_cpt_code',
            'quantity_units',
            'orig_charge',
            'adjustments',
            'amount',
            'balance',
            'key_id'
        ]

        hb_key_row = 1

        for hb_key_raw in hb_key_raw_sheet.rows:

            try:

                data = { 'batch_no' : batch_no } 

                for hb_key_col in range(0, len(hb_key_raw) ) :

                    data[reconkeys_header[hb_key_col]] = hb_key_raw[hb_key_col].value

                temp = datetime.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

                date = ''

                try:

                    delta = data['shift_date'] - temp

                    date = str(int(float(delta.days) + (float(delta.seconds) / 86400)))

                except : 

                    date = str(data['shift_date'])

                key_id = str(data['branch']) + '@' + date + '@' + str(data['description']) + '@' + str(data['client_facility_name']).replace(' ', '').replace('.', '').strip()

                data['key_id'] = key_id.strip()

                for header in reconkeys_header:

                    data[header] = str(data[header])

                if hb_key_row > 1 and data['branch'] != '':

                    reconkeys_hb_arr.append(data)

                    check = ReconKeys_HB.objects.filter(key_id=data['key_id'])

                    if len(check) == 0:

                        reconkeys_hb_model = ReconKeys_HB(**data)

                        reconkeys_hb_model.save()

                    else :

                        check.update(**data)

                hb_key_row += 1

            except :

                pdb.set_trace()

        request.session['reconkeys_hb_arr'] = json.dumps(reconkeys_hb_arr)

        # data_table = Template("""
        #     """)

        # html = data_table.render(Context({'reconkeys_arr': json.loads(request.session.get('reconkeys_arr', '[]'))}))

        if len(reconkeys_hb_arr) == 0:

            request.session['msg'] = 'Invalid Format'

        else :

            request.session['msg'] = ''            

        return HttpResponse("success")

    else:
        
        return render(request, 'reconkeys/reconkeys_hb.html',
            {

                'reconkeys_hb_arr' : json.loads(request.session.get('reconkeys_hb_arr', '[]')),

                'msg' : request.session.get('msg', '')

            })



def payment_board(request):

    # if 'refresh' in request.POST:

    #     request.session['payment_arr'] = '[]'           

    if request.method == 'POST' and request.FILES:

        myfile = request.FILES['file']

        fs = FileSystemStorage()

        filename = fs.save('uploaded_files/'+myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        workbook = load_workbook( myfile )

        input_payment_data_sheet = workbook[workbook.sheetnames[0]]

        payment_arr = []

        payment_header = [
            'check',
            'recon_key',
            'check_amount'
        ]

        payment_row = 1

        for payment in input_payment_data_sheet.rows:

            try:

                item = {

                    'check' : str(payment[0].value),

                    'recon_key' : str(payment[1].value),

                    'check_amount' : str(payment[2].value).replace('$',''),

                }

                if payment_row > 1:

                    payment_arr.append( item )

                payment_row += 1


            except:

                pass

        request.session['input_payment_arr'] = json.dumps(payment_arr)

        # data_table = Template("""
        # """)
        # html = data_table.render(Context({'payment_arr': json.loads(request.session.get('payment_arr', '[]'))}))

        return HttpResponse("success")

    else:
        
        return render(request, 'payment/index.html',
            {

                'input_payment_arr' : json.loads(request.session.get('input_payment_arr', '[]')),

            })


def generated_invoice(request):

    return render(request, 'report/generated_invoice.html',
        {

            'input_invoice_arr' : json.loads(request.session.get('input_invoice_arr', '[]')),

        })


def imported_payment(request):

    return render(request, 'report/imported_payment.html',
        {

            'imported_payment_arr' : json.loads(request.session.get('imported_payment_arr', '[]')),

        })


def unused_payment(request):

    return render(request, 'report/unused_payment.html',
        {

            'unused_payment_arr' : json.loads(request.session.get('unused_payment_arr', '[]')),

        })


def unused_invoice(request):

    return render(request, 'report/unused_invoice.html',
        {

            'unused_invoice_arr' : json.loads(request.session.get('unused_invoice_arr', '[]')),

        })


def matching_by_recon_key(request):

    return render(request, 'report/matching_by_recon_key.html',
        {

            'matching_by_recon_key_arr' : json.loads(request.session.get('matching_by_recon_key_arr', '[]')),

        })



def cash_post(request):

    # input_invoice_arr = json.loads(request.session.get('input_invoice_arr', '[]'))

    input_invoice_arr = []

    if len(input_invoice_arr) == 0:

        input_invoice_arr = []

        max_recon_count = 0

        invoices_with_rks_count = 0

        invoices_without_rks_count = 0


        used_kt_tc_data = []

        unused_kt_tc_data = []


        used_kt_key_data = []

        unused_kt_key_data = []


        used_hb_tc_data = []

        unused_hb_tc_data = []

        used_hb_key_data = []

        unused_hb_key_data = []

        # invoice_data_arr = json.loads(request.session.get('invoice_arr', '[]'))

        # kt_tc_raw_arr = json.loads(request.session.get('timecard_kt_arr', '[]'))

        # kt_key_raw_arr = json.loads(request.session.get('reconkeys_arr', '[]'))

        # hb_tc_raw_arr = json.loads(request.session.get('timecard_hb_arr', '[]'))

        # hb_key_raw_arr = json.loads(request.session.get('reconkeys_hb_arr', '[]'))

        invoice_db = Invoice.objects.all()

        invoice_data_arr = []

        for invoice in invoice_db:

            invoice_data_arr.append(model_to_dict(invoice))


        timecard_kt_db = TimeCard_KT.objects.all()

        kt_tc_raw_arr = []

        for timecard_kt in timecard_kt_db:

            kt_tc_raw_arr.append(model_to_dict(timecard_kt))


        timecard_hb_db = TimeCard_HB.objects.all()

        hb_tc_raw_arr = []

        for timecard_hb in timecard_hb_db:

            hb_tc_raw_arr.append(model_to_dict(timecard_hb))   


        reconkeys_kt_db = ReconKeys_KT.objects.all()

        kt_key_raw_arr = []

        for reconkeys_kt in reconkeys_kt_db:

            kt_key_raw_arr.append(model_to_dict(reconkeys_kt))   


        reconkeys_hb_db = ReconKeys_HB.objects.all()

        hb_key_raw_arr = []

        for reconkeys_hb in reconkeys_hb_db:

            hb_key_raw_arr.append(model_to_dict(reconkeys_hb))   


        for invoice_data in invoice_data_arr:

            try:

                res = { }

                res['invoice'] = invoice_data['invoice_number']

                res['recon_key'] = []

                res['invoice_amount'] = invoice_data['total_bill_amount']

                recon_count = 0

                for kt_tc_raw in kt_tc_raw_arr : 

                    try:

                        if str(invoice_data['system']) + str(invoice_data['tc']) == str(kt_tc_raw['time_card_id']):


                            for kt_key_raw in kt_key_raw_arr : 

                                try:

                                    if kt_tc_raw['uid'] == kt_key_raw['key_id'] and kt_key_raw['invoice_no'] not in res['recon_key']: 

                                        # pdb.set_trace()

                                        res['recon_key'].append(kt_key_raw['invoice_no'])

                                        if kt_key_raw not in used_kt_key_data:

                                            used_kt_key_data.append(kt_key_raw)

                                        if kt_tc_raw not in used_kt_tc_data:

                                            used_kt_tc_data.append(kt_tc_raw)

                                        recon_count += 1

                                except : 

                                    pdb.set_trace()

                    except :

                        pass

                for hb_tc_raw in hb_tc_raw_arr : 

                    try:

                        if str(invoice_data['system']) + str(invoice_data['tc']) == str(hb_tc_raw['time_card_id']) :

                            for hb_key_raw in hb_key_raw_arr : 

                                try:

                                    if hb_tc_raw['uid'] == hb_key_raw['key_id'] and hb_key_raw['invoice'] not in res['recon_key']: 

                                        res['recon_key'].append(hb_key_raw['invoice'])

                                        if hb_key_raw not in used_hb_key_data:

                                            used_hb_key_data.append(hb_key_raw)

                                        if hb_tc_raw not in used_hb_tc_data:

                                            used_hb_tc_data.append(hb_tc_raw)

                                        recon_count += 1
                                except : 

                                    pass

                    except : 

                        pass

                if recon_count != 0:

                    invoices_with_rks_count += 1

                else :

                    invoices_without_rks_count += 1


                if max_recon_count < recon_count :

                    max_recon_count = recon_count

                input_invoice_arr.append(res)

            except :

                print('something went wrong')

                pdb.set_trace()

        request.session['input_invoice_arr'] = json.dumps(input_invoice_arr)

    # start cash posting.

    input_invoice_arr = json.loads(request.session.get('input_invoice_arr', '[]'))

    input_payment_arr = json.loads(request.session.get('input_payment_arr', '[]'))

    # calculating unused invoices 

    unused_invoice_arr = []

    imported_invoice_arr = []

    imported_payment_arr = []

    unused_payment_arr = []

    matching_by_recon_key_arr = []


    total_invoice_amount = 0

    reconned_invoice_amount = 0

    unused_invoice_amount = 0

    total_payment_amount = 0

    reconned_payment_amount = 0

    unused_payment_amount = 0

    balance_on_recon_invoice = 0

    try:

        for invoice in input_invoice_arr:

            flag = 0

            for payment in input_payment_arr:

                if payment['recon_key'] in invoice['recon_key']:

                    flag += 1

            if flag == 0:

                unused_invoice_arr.append(invoice)

                unused_invoice_amount += float(invoice['invoice_amount'])

            else :

                imported_invoice_arr.append(invoice)

                reconned_invoice_amount += float(invoice['invoice_amount'])

            total_invoice_amount += float(invoice['invoice_amount'])


        unique_recon_list = []

        for invoice in imported_invoice_arr:

            if invoice['recon_key'][0] not in unique_recon_list:

                unique_recon_list.append(invoice['recon_key'][0])

        # calculating imported payment and unused payment

        for payment in input_payment_arr:

            flag = 0

            sub_invoice_amt = 0

            for invoice in input_invoice_arr:

                if payment['recon_key'] in invoice['recon_key']:

                    sub_invoice_amt += float(invoice['invoice_amount'])

            for invoice in input_invoice_arr:

                if payment['recon_key'] in invoice['recon_key']:

                    imported_payment = {

                        'invoice' : invoice['invoice'],

                        'payment' : payment['check'],

                        'check_amount' : float(payment['check_amount']) * float(invoice['invoice_amount']) / sub_invoice_amt ,

                        'recon_key' : payment['recon_key']

                    }

                    imported_payment_arr.append(imported_payment)

                    flag += 1

            if flag == 0:

                unused_payment_arr.append(payment)

                unused_payment_amount += float(payment['check_amount'])

            else :

                reconned_payment_amount += float(payment['check_amount'])

            total_payment_amount += float(payment['check_amount'])


        balance_on_recon_invoice = reconned_invoice_amount - reconned_payment_amount

        # calculation matching by recon key data

        for unique_recon in unique_recon_list:

            matching = {}

            sub_invoice = 0

            sub_payment = 0

            multiple = []

            for invoice in imported_invoice_arr:            

                if unique_recon in invoice['recon_key']:

                    sub_invoice += float(invoice['invoice_amount'])

                    multiple = invoice['recon_key']

            for recon in multiple:

                for payment in imported_payment_arr:

                    if recon in payment['recon_key']:

                        sub_payment += float(payment['check_amount'])

            matching = {

                    'recon_key' : multiple,

                    'invoice_amount' : sub_invoice,

                    'payment_amount' : sub_payment,

                    'difference' : float(sub_invoice - sub_payment)

                }

            matching_by_recon_key_arr.append(matching)

    except:

        pass


    request.session['imported_payment_arr'] = json.dumps(imported_payment_arr)

    request.session['unused_payment_arr'] = json.dumps(unused_payment_arr)

    request.session['unused_invoice_arr'] = json.dumps(unused_invoice_arr)

    request.session['matching_by_recon_key_arr'] = json.dumps(matching_by_recon_key_arr)

    
    # return redirect("/generated_invoice")

    return render(request, 'report/index.html',

        {

            'total_invoice_amount' : total_invoice_amount,

            'reconned_invoice_amount' : reconned_invoice_amount,

            'unused_invoice_amount' : unused_invoice_amount,

            'total_payment_amount' : total_payment_amount,

            'reconned_payment_amount' : reconned_payment_amount,

            'unused_payment_amount' : unused_payment_amount,

            'balance_on_recon_invoice' : balance_on_recon_invoice

        })



def signup(request):
    
    if request.POST:

        uploaded_file_url = ''

        try:

            myfile = request.FILES['myfile']

            fs = FileSystemStorage()

            filename = fs.save('uploaded_files/images/'+myfile.name, myfile)

            uploaded_file_url = fs.url(filename)

        except:

            pass

        account = Account()

        account.firstname = request.POST["firstname"]

        account.lastname = request.POST["lastname"]

        account.username = request.POST["username"]

        account.email = request.POST["email"]

        account.password = request.POST["password"]

        account.image = uploaded_file_url

        account.role = "user"

        request.session['user'] = {
            # "id": user[0].id,
            "firstname" : request.POST["firstname"],

            "lastname" : request.POST["lastname"],

            "username": request.POST["username"],

            "email": request.POST["email"],

            "password": request.POST["password"],

            "image" : uploaded_file_url,

	        "role" : "user",
	    }

        account.save()
	   
        return render(request, 'login.html')

    return render(request, 'signup.html')

    # return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

def changePwd(request):
    if request.POST:
        if request.POST["opassword"] == request.session['user']['password']:
            if request.POST["password"] == request.POST["rpassword"]:
                account = Account.objects.filter(email=request.session['user']['email']).update(password=request.POST["password"])
                request.session['user']['password'] = request.POST['password']
                return redirect("/home") 


    return render(request, 'changePwd.html', locals())

	# return render_to_response("changePwd.html",locals(),context_instance=RequestContext(request))       

def forgot(request):
    if request.POST:
        if request.POST["password"] == request.POST["rpassword"]:
            account = Account.objects.filter(email=request.POST["email"]).update(password=request.POST["password"])
            return redirect("login") 

    return render(request, 'forgot.html')
    # return render_to_response("forgot.html",locals(),context_instance=RequestContext(request))           