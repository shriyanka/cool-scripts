import dicttoxml, xmltodict
from collections import OrderedDict
import requests

def dict2xml(**kwargs):

    if kwargs.pop("is_cod_booking") == "null": #Prepaid
        Mode, Awb_C, collectable_amount='P', '7', 0.0
    else:
        Mode, Awb_C, collectable_amount='C', 'I', kwargs['content_info']['value'] #COD
    
    if kwargs.pop('pickup') is not "null":
        Mode,Awb_C='R','7' #Reverse

    if kwargs.pop("collect_on_delivery") > 0.0:
        collectable_amount = kwargs.pop("collect_on_delivery")
    
    if 'packages' in kwargs:
        quantity = len(kwargs.pop('packages'))
    else:
        quantity = 1
    
    phone = kwargs.pop("delivery_tel")

    xml_dict = OrderedDict({
        "Customer":
        {   
            "CUSTCD": kwargs.pop("user_id")
        },
        "Docket":
        {
            "Order_No": kwargs.pop("order_id"),
            "AGENT_ID": kwargs.pop("vendor_id"),
            "Product_Code": kwargs.pop("product_id"),
            "Item_Name": kwargs["content_info"].pop("description"),
            "AWB_No": Awb_C+kwargs.pop("awb"),
            "N0_of_Pieces": quantity,
            "Customer_Name": kwargs.pop("delivery_name"),
            "Shipping_Add1": kwargs["receiver_address"].pop("street1"),
            "Shipping_Add2": kwargs["receiver_address"].pop("street2"),
            "Shipping_City": kwargs.pop("delivery_city"),
            "Shipping_State": kwargs.pop("delivery_state"),
            "Shipping_Zip": kwargs.pop("delivery_zip"),
            "Shipping_TeleNo": phone,
            "Shipping_MobileNo": phone,
            "Shipping_TeleNo2": phone,
            "Total_Amt": kwargs["content_info"].pop("value"),
            "Mode": Mode,
            "Collectable_amount": collectable_amount,
            "Weight": kwargs.pop("courier_weight"),
            "UOM":"Per KG",
            "Type_of_Service": "Economy",
            "VendorName":kwargs.pop("billing_name"),
            "VendorAddress1":kwargs['sender_address'].pop('street1'),
            "VendorAddress2":kwargs['sender_address'].pop('street2'),
            "VendorPincode":kwargs.pop("billing_zip"),
            "VendorTeleNo":kwargs.pop("billing_tel"),
        }
    })
    return dicttoxml.dicttoxml(xml_dict,attr_type=False, custom_root="NewDataSet")

def xml2dict(xml=''):
    params = OrderedDict()
    params = xmltodict.parse(xml)
    return params
    

dict_sample = {
    "_id" : "568ff88609959d2e380bf43e",
    "status" : "InfoReceived",
    "courier_weight" : 12.0000000000000000,
    "is_cod_booking" : "false",
    "courier_price" : 65.8499999999999940,
    "billing_tel" : "9999991111",
    "status_code" : "null",
    "is_cod_shipment" : "null",
    "alert_receiver" : "false",
    "delivery_name" : "AJ Kumar ",
    "courier_mode" : "domestic",
    "notified_on" : "null",
    "order_date" : "2016-01-08T17:57:26.175Z",
    "courier_type" : "parcel",
    "partner" : {
        "user_id" : "554c085809959d182c33ebd7",
        "id" : "554a795a09959d1a90d06d12"
    },
    "receiver_address" : {
        "country" : "India",
        "street2" : "street 2 of Address",
        "street3" : "null",
        "company_name" : "AJKumar ",
        "street1" : "Mandatory street 1 of Address"
    },
    "delivery_city" : "Bangalore",
    "customer_reference" : "OD104886794715843000",
    "billing_country" : "India",
    "total_billing_weight" : 62.1000000000000010,
    "actual_weight" : 12.0000000000000000,
    "sender_address" : {
        "street1" : "shipper addresss line 1",
        "street2" : "Shipper addresss line 2",
        "street3" : "Shipper addresss line 3",
        "company_name" : "sender",
        "country" : "India"
    },
    "packages" : [ 
        {
            "actual_weight" : 12000.0000000000000000,
            "rate" : 98.0000000000000000,
            "price" : 65.8499999999999940,
            "weight" : 62100.0000000000000000,
            "dimensions" : {
                "h" : 90.0000000000000000,
                "l" : 138.0000000000000000,
                "w" : 25.0000000000000000
            }
        }
    ],
    "user_id" : "CC000100132",
    "dimensions" : {
        "width" : 25.0000000000000000,
        "length" : 138.0000000000000000,
        "height" : 90.0000000000000000
    },
    "content_info" : {
        "description" : "Hero Megastar 26T 18Speed Road Cycle Yellow, Black",
        "value" : "6749.0"
    },
    "bank_ref_no" : "ecz_wallet",
    "billing_email" : "aj@ecz.com",
    "billing_zip" : "560010",
    "collect_on_delivery" : 0.0000000000000000,
    "is_cop_request" : "false",
    "cod_amount_plus_st" : 0.0000000000000000,
    "pickup" : "null",
    "billing_name" : "SENDER_NAME",
    "is_test_booking" : "true",
    "order_status" : "Success",
    "status_message" : "null",
    "delivery_zip" : "400079",
    "card_name" : "null",
    "delivery_tel" : "9004110621",
    "delivery_country" : "India",
    "order_source" : "api",
    "internal_comments" : "null",
    "need_insurance" : "false",
    "order_id" : "ECZ35044",
    "vendor_id" : "5554c32d95613e604c91926f",
    "invoice_date" : "null",
    "language" : "EN",
    "delivery_email" : "null",
    "purpose" : "commercial",
    "payment_made" : "api_instamojo",
    "cancel_url" : "http://www.ecz.ecom.com/cancel-transaction",
    "payment_mode" : "api_instamojo",
    "invoice_number" : "",
    "merchant_id" : "34272",
    "awb" : "794671891855",
    "billing_city" : "Bangalore",
    "label_meta" : {
        "url" : "http://205.147.96.143/download/labels/794671891855.pdf",
        "generated_date" : "2016-01-08T17:57:31.263Z",
        "awb" : "794671891855"
    },
    "delivery_address" : "AJ , TEST BOOKING - DO NOT SHIP, Ali Milk Centre, Near Ajwa Hotel, India",
    "courier_reference" : "null",
    "product_id" : "49771509-b3ab-4643-b2a9-5a6ab1a0ae97",
    "courier_amount" : 98.0000000000000000,
    "currency" : "INR",
    "notified" : "null",
    "is_partner_request" : "true",
    "failure_message" : "null",
    "drop_off_point" : "",
    "is_dropoff" : "false",
    "amount" : "98.0",
    "books" : {
        "fuel_surcharge" : 25.0000000000000000,
        "waybill_fee" : 0,
        "extra_charges" : 0,
        "price" : 65.8499999999999940,
        "base_rate" : 43.8999999999999990,
        "cod_charges" : {},
        "service_tax" : 14.0000000000000000,
        "gateway_amount" : 0.0000000000000000,
        "total_paid_amount" : "98.0",
        "margin" : 0.0000000000000000,
        "markup" : 20.0000000000000000,
        "gateway_charge" : 0.0000000000000000
    },
    "is_multi_packet" : "false",
    "redirect_url" : "http://www.ecz.ecom.com/success",
    "billing_address" : "sender, TEST BOOKING - DO NOT SHIP, Shipper addresss line 2, Shipper addresss line 3, India",
    "cod_amount" : 0.0000000000000000,
    "delivery_state" : "Maharashtra",
    "is_cod_amount_credited" : "null",
    "billing_state" : "Karnataka",
    "tracking_id" : "null",
}


xml = dict2xml(**dict_sample)
#print xml

#obj_cre = {}
#obj_cre["clientId"] = "DOTZOT";
#obj_cre["userName"] = "dztuser";
#obj_cre["password"] = "dotzot@2013";

#url = "http://webxpress.cloudapp.net/DMS_DZT_TEST/services/Cust_WS_Ver2.asmx?WSDL&op=PushOrderData_WalkInVendors"
#headers = {'Content-Type': 'application/xml'}
#resp = requests.post(url, params=obj_cre, data =xml, headers=headers,)
#print resp.content

# Suppose we get the resp back as xml so converting it back to dictionary

resp = xml
params = xml2dict(resp) 
print params
