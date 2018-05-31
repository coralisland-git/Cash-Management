from django.contrib import admin

from models import *# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'image', 'password', 'username']
    search_fields = ['firstname', 'lastname', 'email', 'image', 'password', 'username']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'system', 'license', 'tc', 'invoice_number', 'total_bill_amount']
    search_fields = ['batch_no', 'system', 'license', 'tc', 'invoice_number']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'payment_id','check', 'recon_key', 'check_amount']
    search_fields = ['batch_no', 'payment_id', 'recon_key', 'check_amount']

class TimeCard_KTAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'time_card_id', 'uid']
    search_fields = ['batch_no', 'time_card_id', 'uid']

class TimeCard_HBAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'time_card_id', 'uid']
    search_fields = ['batch_no', 'time_card_id', 'uid']

class ReconKeys_KTAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'key_id', 'invoice_no']
    search_fields = ['batch_no', 'key_id', 'invoice_no']

class ReconKeys_HBAdmin(admin.ModelAdmin):
    list_display = ['batch_no', 'key_id', 'invoice']
    search_fields = ['batch_no', 'key_id', 'invoice']

class Cash_PostAdmin(admin.ModelAdmin):
    list_display = ['cash_post_id', 'recon_key', 'invoice_amount', 'payment_amount', 'difference', 'posted_date']
    search_fields = ['cash_post_id', 'recon_key', 'invoice_amount', 'payment_amount', 'difference', 'posted_date']


admin.site.register(Account, AccountAdmin)

admin.site.register(Invoice, InvoiceAdmin)

admin.site.register(Payment,PaymentAdmin)

admin.site.register(TimeCard_KT,TimeCard_KTAdmin)

admin.site.register(TimeCard_HB,TimeCard_HBAdmin)

admin.site.register(ReconKeys_KT,ReconKeys_KTAdmin)

admin.site.register(ReconKeys_HB,ReconKeys_HBAdmin)

admin.site.register(Cash_Post,Cash_PostAdmin)