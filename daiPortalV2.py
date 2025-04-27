import yaml
from yaml.loader import SafeLoader

import streamlit as st
import streamlit_authenticator as stauth

import plotly.express as px
import json
from datetime import *

from mongodb import pushInfo
from coreLogic import bill
from processCustomer import fetchRecords
# from mongodb import printJson

with open("./trailCreds.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

def tabForm(tab, tabRef):

    deploymentStrategy = {
        "custom" : {"numLabours":1, "labour1":{"category":"","hours":0, "amount":0.0}},
        "strat1" : {"numLabours":2,
                    "labour1":{"category":"Lead Electrician","hours":8, "amount":65.0},
                    "labour2":{"category":"Helper","hours":8, "amount":35.0}
                    },
        "strat2" : {"numLabours":3,
                    "labour1":{"category":"Lead Electrician","hours":8, "amount":65.0},
                    "labour2":{"category":"Helper","hours":8, "amount":35.0},
                    "labour3":{"category":"Helper","hours":6, "amount":35.0},
                    },
        "strat3" : {"numLabours":3,
                    "labour1":{"category":"Lead Electrician","hours":8, "amount":65.0},
                    "labour2":{"category":"Helper","hours":8, "amount":35.0},
                    "labour3":{"category":"Helper","hours":8, "amount":35.0},
                    }
    }

    deploymentStrategyEncode = {
        "Custom" : "custom",
        "50 Amp Interior Wall Mounted Hard Wired" : "strat1",
        "40 Amp Interior Wall Mounted Plug-in" : "strat2",
        "50 Amp Exterior Pedestal Mounted Hard Wired" : "strat3"
     }

    st.session_state.tabInfo[tabRef] = {'tabLabor':{}, 'tabSubCon':{}, 'tabLicense':{}, 'tabTrenching':{}, 'tabEVCE':{}}
    with tab.expander("Deployment"):
        deployStrat = st.selectbox(label="Select the deployment Strategy:",
                                    options=deploymentStrategyEncode.keys(),key=f"deployment@{tabRef}",)
        st.session_state.stratKey = deploymentStrategyEncode[deployStrat]
        st.session_state.strategy = deploymentStrategy[deploymentStrategyEncode[deployStrat]]

    with tab.expander("Labor Details"):
        numLabourers = st.number_input(label = "Number of Labourers", min_value=1, max_value=5, value=st.session_state.strategy['numLabours'], key=f'numlabour@{tabRef}')
        tabLabor = {f"Labor_{i+1}" : {} for i in range(0, numLabourers)}

        for i in range(numLabourers):
            if f"labour{i+1}" in st.session_state.strategy.keys():
                defaultVals = st.session_state.strategy[f"labour{i+1}"]
            else:
                defaultVals = {"category":"","hours":0, "amount":0.0}

            st.text(f"Labor {i+1}")

            tabLabor[f"Labor_{i+1}"]['category'] = st.text_input(label = 'Category', max_chars=25, value=defaultVals["category"], key=f"labour{i+1}#category@{tabRef}")
            tabLabor[f"Labor_{i+1}"]['amount'] = st.number_input(label = 'Amount', min_value=0.0,value=defaultVals["amount"], key=f"labour{i+1}#amount@{tabRef}")
            tabLabor[f"Labor_{i+1}"]['hours'] = st.number_input(label = 'Hours', min_value=0, max_value=24,value=defaultVals["hours"], key=f"labour{i+1}#hour@{tabRef}")
            st.divider()

    with tab.expander("Subcontractor"):
        tabSubCon = {'elecContractor':{'amount':0, 'units':0}, 'dryWall':{'amount':0, 'units':0}, 'trenching':{'amount':0, 'units':0}}
        if st.toggle("Electrical Contractor", key=f"elecCon@{tabRef}"): #and deployment strategy
            tabSubCon['elecContractor']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"elecCon#amount@{tabRef}")
            tabSubCon['elecContractor']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"elecCon#units@{tabRef}")
        if st.toggle("Dry Wall", key=f"drywall@{tabRef}"): #and deployment strategy
            tabSubCon['dryWall']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"drywall#amount@{tabRef}")
            tabSubCon['dryWall']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"drywall#units@{tabRef}")
        if st.toggle("Trenching & Excavation", key=f"trench@{tabRef}"): #and deployment strategy
            tabSubCon['trenching']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"trench#amount@{tabRef}")
            tabSubCon['trenching']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"trench#units@{tabRef}")

    with tab.expander("Licensing"):
        tabLicense = {'elecPermit':{}, 'buildingPermit':{}, 'surveyorFee':{}, 'adminFee':{},'masterElecFee':{}}

        st.write("Electrical Permitting")
        tabLicense['elecPermit']['amount'] = st.number_input(label = 'Amount', min_value=0.0, value=125.0, key=f"elecPermit#amount@{tabRef}")
        tabLicense['elecPermit']['units'] = st.number_input(label = 'Quantity', min_value=0, max_value=24,value=1, key=f"elecPermit#units@{tabRef}")
        st.divider()

        st.write("Building Permit")
        tabLicense['buildingPermit']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"buildingPermit#amount@{tabRef}")
        tabLicense['buildingPermit']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"buildingPermit#units@{tabRef}")
        st.divider()

        st.write("Surveyor Fee")
        tabLicense['surveyorFee']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"surveyorFee#amount@{tabRef}")
        tabLicense['surveyorFee']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"surveyorFee#units@{tabRef}")
        st.divider()

        st.write("Expediting/Administration Fee")
        tabLicense['adminFee']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"adminFee#amount@{tabRef}")
        tabLicense['adminFee']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"adminFee#units@{tabRef}")
        st.divider()

        st.write("Master Electrician Fee")
        tabLicense['masterElecFee']['amount'] = st.number_input(label = 'Amount', min_value=0.0,value=300.0, key=f"masterElecFee#amount@{tabRef}")
        tabLicense['masterElecFee']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"masterElecFee#units@{tabRef}")

    with tab.expander("Wall Penetrations & Concrete Work"):
        tabWallPenetration = {"wallPenetration":{'amount':0, 'units':0},"ConcreteFastening":{'amount':0, 'units':0},"ConcreteFooter":{'amount':0, 'units':0},"ConcreteLabor":{'amount':0, 'units':0}}

        if st.toggle("Wall Penetrations", key=f"wallPene@{tabRef}"):
            tabWallPenetration['wallPenetration']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"wallPene#amount@{tabRef}")
            tabWallPenetration['wallPenetration']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"wallPene#units@{tabRef}")

        if st.toggle("Concrete Work", key=f"concWork@{tabRef}"):
            st.write("Concrete Work - Fastening")
            tabWallPenetration['ConcreteFastening']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"concFast#amount@{tabRef}")
            tabWallPenetration['ConcreteFastening']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"concFast#units@{tabRef}")

            st.write("Concrete Work - Footer")
            tabWallPenetration['ConcreteFooter']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"concFoot#amount@{tabRef}")
            tabWallPenetration['ConcreteFooter']['units'] = st.number_input(label = 'Units', min_value=0, max_value=24, key=f"concFoot#units@{tabRef}")

            st.write("Concrete Work - Labor")
            tabWallPenetration['ConcreteLabor']['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"concLabor#amount@{tabRef}")
            tabWallPenetration['ConcreteLabor']['units'] = st.number_input(label = 'Hours', min_value=0, max_value=24, key=f"concLabor#units@{tabRef}")

    with tab.expander("Trenching and Excavation"):
        tabTrenching = {'add-on1': {}, 'add-on2': {}, 'add-on3': {}}
        for addon in tabTrenching:
            st.write(f"{addon.title()}")
            tabTrenching[addon]['amount'] = st.number_input(label=f"{addon} Amount", min_value=0.0, key=f"{addon}#amount@{tabRef}")
            tabTrenching[addon]['units'] = st.number_input(label=f"{addon} Units", min_value=0, key=f"{addon}#units@{tabRef}")
            st.divider()

    with tab.expander("Materials"):
        tabEVCE = {
            'EVCE': {},
            'Pedestal': {},
            'Surge Protections': {},
            'Smart Switcher': {}
        }
        numMaterials = st.number_input(label = "Number of Materials", min_value=1, max_value=12, key=f'nummaterial@{tabRef}')
        tabMaterial = {f"Material_{i+1}" : {} for i in range(0, numMaterials)}


        for i in range(numMaterials):
            st.text(f"Material {i+1}")
            tabMaterial[f"Material_{i+1}"]['category'] = st.text_input(label = 'Category', max_chars=25, key=f"material{i+1}#category@{tabRef}")
            tabMaterial[f"Material_{i+1}"]['amount'] = st.number_input(label = 'Amount', min_value=0.0, key=f"material{i+1}#amount@{tabRef}")
            tabMaterial[f"Material_{i+1}"]['units'] = st.number_input(label = 'Units', min_value=0, key=f"material{i+1}#unit@{tabRef}")
            st.divider()


    with tab.expander("EVCEs + Add Ons"):
        tabEVCE = {
            'EVCE': {},
            'Pedestal': {},
            'Surge Protections': {},
            'Smart Switcher': {}
        }

        for item in tabEVCE:
            st.write(f"{item}")
            tabEVCE[item]['amount'] = st.number_input(label=f"{item} Amount", min_value=0.0, key=f"{item.replace(' ', '')}#amount@{tabRef}")
            tabEVCE[item]['units'] = st.number_input(label=f"{item} Units", min_value=0, key=f"{item.replace(' ', '')}#units@{tabRef}")
            st.divider()

    st.session_state.tabInfo[tabRef] = {'tabLabor':tabLabor, 'tabSubCon':tabSubCon, 'tabLicense':tabLicense, 'tabTrenching':tabTrenching, 'tabEVCE':tabEVCE}

    # st.session_state.tabInfo[tabRef] = json.dumps(st.session_state.tabInfo[tabRef])


    billInfo = bill()
    billInfo.labourCalc(tabLabor)
    billInfo.subContractorCalc(tabSubCon)
    billInfo.licensingCalc(tabLicense)
    billInfo.elecServiceCalc(tabMaterial)
    billInfo.wallCalc(tabWallPenetration)
    billInfo.outdoorCalc(tabTrenching)
    billInfo.evceCalc(tabEVCE)
    billInfo.preTaxCalc()

    if st.session_state.qMerit:
        grandTot = billInfo.finalCalcs(permit=425, state=st.session_state.userState)
    else:
        grandTot = billInfo.finalCalcs(permit=425, state=st.session_state.userState, referralQmerit=0)


    billInfoSplit = {'Labor':billInfo.labourTot,
            'Sub Contractor':billInfo.subContractorTot,
            'Licensing':billInfo.licensingTot,
            'Material':billInfo.elecServiceTot,
            'Trenching':billInfo.wallTot,
            'Outdoor':billInfo.outdoorTot,
            'EVCE':billInfo.evceTot,
    }

    with tab.expander("Estimate Total:"):
        col1, col2 = st.columns(2)
        col1.header("Estimate Breakdown")
        for ky in billInfoSplit:
            col1.write(f"{ky} Cost: ${billInfoSplit[ky]}")
        col1.write(f"Pre-Tax Service Fee Total: ${billInfo.preServiceFeeTot:.2f}")
        col1.write(f"Grand Total Service Fee: ${grandTot:.2f}")
        billInfoSplit_noZero = {k: v for k, v in billInfoSplit.items() if v > 0}
        fig_ = px.pie(values=billInfoSplit_noZero.values(), names=billInfoSplit_noZero.keys())
        col2.plotly_chart(fig_, key=f'chart@{tabRef}')



def sidebar():
    custInfo = {}
    st.session_state.defaultCustInfo = {"custName":None, "custAddr":None, "custPhone":None}
    with st.sidebar:
        st.title("Dai Tech's Operations Platform.")
        with st.expander("Customer Configuration"):
            form = st.form("Customer Reference")
            custInfo['CustomerNumber'] = form.text_input(label="Customer Reference Number",value="",help='Customer\'s Reference Number.', placeholder='', max_chars= 50)
            # st.session_state.defaultCustInfo = form.form_submit_button("submit")
            if form.form_submit_button("Submit"):
                if custInfo['CustomerNumber'] != "":
                    valid, response = fetchRecords(custInfo['CustomerNumber'])
                    if valid:
                        st.session_state.defaultCustInfo = response
                        st.success('Data Imported!', icon="✅")
                    else:
                        st.error('Customer ID not found', icon="🚨")




            custInfo['CustomerName'] = st.text_input(label="Customer Name",value=st.session_state.defaultCustInfo['custName'],help='Customer\'s name.', placeholder='', max_chars= 50)
            custInfo['CustomerAddr'] = st.text_area(label="Customer's House Address", max_chars=255, value=st.session_state.defaultCustInfo['custAddr'])
            custInfo['CustomerPhone'] = st.text_input(label="Customer's Phone Number", help='Format: 2404321554', value=st.session_state.defaultCustInfo['custPhone'])
            # numEstimates = st.segmented_control(label="Number of estimates",options=[1,2,3,4], default=3,help="Estimate Forms")
            numEstimates = st.number_input(label="Number of estimates", help='',min_value=1,step=1, max_value=4)
            st.session_state.qMerit = st.checkbox("QMerit Customer")
            custInfo['userqMerit'] = st.session_state.qMerit
            custInfo['userState'] = st.segmented_control("State of Residency", options=['VA','MD','DC'],default='VA')
            st.session_state.userState = custInfo['userState']
        # with st.expander("Budget Summary"):
        #     st.write("Grand Estimate:")
            st.divider()
            if st.button("Save Information", type='primary',help="Save only when all estimates are ready."):
                st.session_state.finalpush = {"custInfo":custInfo, "estimates":st.session_state.tabInfo, "time":datetime.now()}
                pushInfo(st.session_state.finalpush)


    tabs = st.tabs([f'Estimate {i}' for i in range(1, numEstimates+1)])
    st.session_state.tabInfo = {f'estRef{i}':{} for i in range(1, numEstimates+1)}

    for tab,tabRef in zip(tabs,st.session_state.tabInfo.keys()):
        tabForm(tab, tabRef)



try:
    authenticator.login()
except Exception as e:
    print("ERR: ", e)
    st.error(e)

if st.session_state.get('authentication_status'):
    authenticator.logout()
    st.title("Dai Tech Operations")
    st.write(f"Welcome *{st.session_state.get('name')}* to the portal")
    sidebar()
elif st.session_state.get('authentication_status') is False:
    st.error('Username/password is incorrect')
elif st.session_state.get('authentication_status') is None:
    st.warning('Please enter your username and password')
