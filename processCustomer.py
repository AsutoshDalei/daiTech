import pandas as pd

daiData = pd.read_csv("./auth/zohoContact.csv",index_col="Record Id")

def fetchRecords(daiID):
    try:
        custinfo = daiData.loc[daiID]
        name = f"{custinfo['First Name']} {custinfo['Last Name']}"
        mobile = custinfo['Mobile']
        addr = [custinfo.fillna('nan')[ar] for ar in ["Work Street Address (1)", "Work Address ( 2) /Suite", "City,State", "Postal Code"] if custinfo.fillna('nan')[ar]!='nan' ]

        return True, {"custName":name, "custPhone":mobile, "custAddr": ', '.join(addr)}

    except:
        return False, None
