import pandas as pd


item = pd.read_excel("POS_DATA.xls","POS_DATA")
# Saving Excel File Columns as List / Array
Cashier_username = item["Cashier_username"].values.tolist()
password = item["password"].values.tolist()
item1 = item["item1"].values.tolist()  # e search
Item_qty1	= item["Item_qty1"].values.tolist() 
Price1	= item["Price1"].values.tolist()
others_item1_sugarlevel1_ID = item["others_item1_sugarlevel1_ID"].values.tolist()
others_item1_sugarlevel2_ID = item["others_item1_sugarlevel2_ID"].values.tolist()
others_item1_addons1_ID	= item["others_item1_addons1_ID"].values.tolist()
others_item1_addons2_ID	= item["others_item1_addons2_ID"].values.tolist()
others_item1_addons3_ID	= item["others_item1_addons3_ID"].values.tolist()
Select_item1_discount_ID = item["Select_item1_discount_ID"].values.tolist()
item_item1_select_dic_ID = item["item_item1_select_dic_ID"].values.tolist()
Card_name_item1	= item["Card_name_item1"].values.tolist()
Card_number_item1 = item["Card_number_item1"].values.tolist()
amount= item["amount"].values.tolist()
type_of_payment = item["type_of_payment"].values.tolist()
Other_payment_btn_ID = item["Other_payment_btn_ID"].values.tolist()
reference_number_optional = item["reference_number_optional"].values.tolist()






