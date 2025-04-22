taxMap = {'DC':0.06,'MD':0.06, 'VA':0.053}

## Sample Set 1

markup = {'laborPre':0.3, 'subcontractPre':0.3, 'materialsPre':0.3, 'concretePre':0.3, 'evcePre':0.22}

labourJson = {
    'labour1':{'category':'lead electrician', 'amount':85, 'hours':12},
    'labour2':{'category':'helper', 'amount':30, 'hours':8},
    'labour3':{'category':'helper', 'amount':30, 'hours':0},
    'inspection':{'category':'lead electrician', 'amount':65, 'hours':2}
}

subContractorJson = {
    'electrical_contractor':{'category':'TBD', 'amount':0, 'units':0},
    'dry_wall':{'category':'150 minimum', 'amount':300, 'units':1},
    'trenching&excavation':{'category':'300 minimum', 'amount':0, 'units':0}
}

permitJson = {
    'electrical_permitting': {'category': 'jurisdiction', 'amount': 125.00, 'units': 1.00},
    'building_permit': {'category': 'Building Permit (DC Only)', 'amount': 0.00, 'units': 1.00},
    'surveyor_fee': {'category': 'Surveyor Fee', 'amount': 0.00, 'units': 1.00},
    'expediting_admin': {'category': 'Expediting/Administration', 'amount': 0.00, 'units': 1.00},
    'master_electrician': {'category': 'Master Electrician Fee', 'amount': 300.00, 'units': 1.00}
}
materialJson = {
    'material_0': {'category': 'Heavy-up Load Management SubPanel', 'comment': '', 'amount': 0.00, 'units': 1.00},
    'material_1a': {'category': 'Circuit Breaker Non-GFCI', 'comment': '1 @ 2 Pole/60 amp Brand/Type Circuit Breaker Non-GFI', 'amount': 50.00, 'units': 1.00},
    'material_1b': {'category': 'Circuit Breaker GFIC', 'comment': '2 @ 2 Pole/20 amp Brand/Type Tandems Circuit Breaker', 'amount': 40.00, 'units': 2.00},
    'material_2': {'category': 'Breaker for Disconnect', 'comment': '1 @ 2 Pole/50 amp Brand/Type Circuit Breaker', 'amount': 30.00, 'units': 0.00},
    'material_3a': {'category': 'Rigid PVC Schedule 40 Conduit', 'comment': 'Schedule 40 Conduit', 'amount': 1.74, 'units': 0.00},
    'material_3b': {'category': 'Ridgid EMT', 'comment': 'EMT', 'amount': 1.94, 'units': 25.00},
    'material_4': {'category': 'Flexible Conduit', 'comment': '1 @ Corlon Flexible Conduit', 'amount': 1.75, 'units': 0.00},
    'material_5': {'category': 'Building Wire (Copper Stranded)', 'comment': '# x AWG/2 wire Copper Stranded', 'amount': 5.00, 'units': 30.00},
    'material_6': {'category': 'Building Wire (Stranded)', 'comment': '#TBDAWG/3 wire Stranded', 'amount': 3.00, 'units': 0.00},
    'material_7': {'category': 'Underground Wire', 'comment': '#6/3 wire Rated Underground Cable', 'amount': 0.00, 'units': 0.00},
    'material_8': {'category': 'Indoor NEMA Disconnect/Plug Receptacle', 'comment': 'Flushed or Unflushed', 'amount': 0.00, 'units': 0.00},
    'material_9': {'category': 'Outdoor NEMA Disconnect Plug Receptacle', 'comment': 'Disconnect', 'amount': 75.00, 'units': 1.00},
    'material_10': {'category': 'PVC Conduit Accessories', 'comment': 'Schedule 40 Connectors, Couplings, Angles, LB\'s', 'amount': 403.50, 'units': 0.20}
}

wallPenetrationJson = {
    'wall_penetration': {'category': 'Wall Penetrations', 'comment': '', 'amount': 50.00, 'units': 0.00},
    'concrete_fastening': {'category': 'Concrete Work (Fastening)', 'comment': '', 'amount': 1000.00, 'units': 0.00},
    'concrete_footer': {'category': 'Concrete Work (Footer)', 'comment': '', 'amount': 50.00, 'units': 0.00},
    'concrete_labor': {'category': 'Concrete Work (Labor)', 'comment': 'Hour', 'amount': 95.00, 'units': 0.00}
}

addOnJson = {
    'add_on_1': {'category': 'Trenching', 'comment': 'Hour', 'amount': 95.00, 'units': 0.00},
    'add_on_2': {'category': 'Boring', 'comment': 'Hour', 'amount': 95.00, 'units': 0.00},
    'add_on_3': {'category': 'Equipment Rental & Transportation', 'comment': 'Day', 'amount': 700.00, 'units': 0.00}
}

evceJson = {
    'evce': {'category': 'EVCE', 'comment': 'Customer Furnished', 'amount': 519.00, 'units': 0.00},
    'pedestal': {'category': 'Pedestal', 'comment': 'TBD', 'amount': 325.00, 'units': 0.00},
    'surge_protections': {'category': 'Surge Protections', 'comment': 'TBD', 'amount': 100.00, 'units': 0.00},
    'smart_switcher': {'category': 'Smart Switcher', 'comment': 'TBD', 'amount': 550.00, 'units': 0.00}
}


# #ATHARV 1

# labourJson = {'labor1':{'category':'Lead Electrician', 'amount':65.00, 'hours':8}, 'labor2':{'category':'Helper', 'amount':30.00, 'hours':8}, 'labor3':{'category':'Helper', 'amount':30.00, 'hours':8}, 'inspection':{'category':'Lead Electrician', 'amount':65.00, 'hours':2}}

# subContractorJson = {'electrical_contractor':{'category':'TBD', 'amount':0.00, 'units':0}, 'dry_wall':{'category':'TBD', 'amount':300.00, 'units':1}, 'trenching_and_excavation':{'category':'TBD', 'amount':0.00, 'units':0}}

# permitJson = {'electrical_permitting':{'category':'Electrical Permitting', 'amount':300.00, 'units':1.00}, 'building_permit':{'category':'Building Permit (DC Only)', 'amount':175.00, 'units':0.00}, 'surveyor_fee':{'category':'Surveyor Fee', 'amount':82.00, 'units':0.00}, 'expediting_admin':{'category':'Expediting/Administration', 'amount':500.00, 'units':0.00}, 'master_electrician':{'category':'Master Electrician Fee', 'amount':300.00, 'units':1.00}}

# materialJson = {'material_0':{'category':'Heavy-up', 'amount':3500.00, 'units':1.00}, 'material_1a':{'category':'Circuit Breaker Non-GFCI', 'comment':'1 @ 2 Pole/100 amp Cutler/Hammer Tan Circuit Breaker Non-GFI', 'amount':125.00, 'units':1.00}, 'material_1b':{'category':'Circuit Breaker GFIC', 'comment':'1 @ 2 Pole/TBD amp Brand/Type GFCI Circuit Breaker', 'amount':150.00, 'units':0.00}, 'material_2':{'category':'Breaker for Disconnect', 'comment':'1 @ 2 Pole/50 amp Square D/Homeline Circuit Breaker', 'amount':30.00, 'units':0.00}, 'material_3a':{'category':'Ridgid PVC Schedule 40 Conduit', 'comment':'Schedule 40 Conduit', 'amount':1.74, 'units':0.00}, 'material_3b':{'category':'Ridgid EMT', 'comment':'EMT', 'amount':1.94, 'units':25.00}, 'material_4':{'category':'Flexible Conduit', 'comment':'1 @ Corlon Flexible Conduit', 'amount':1.75, 'units':0.00}, 'material_5':{'category':'Building Wire (Copper Stranded)', 'comment':'#6AWG/4 wire Copper Stranded', 'amount':5.00, 'units':0.00}, 'material_6':{'category':'Building Wire (Stranded)', 'comment':'#TBDAWG/3 wire Stranded', 'amount':12.00, 'units':30.00}, 'material_7':{'category':'Underground Wire', 'comment':'#6/3 wire Rated Underground Cable', 'amount':0.00, 'units':0.00}, 'material_8':{'category':'Indoor NEMA Disconnect/Plug Receptacle', 'comment':'Flushed or Unflushed', 'amount':0.00, 'units':0.00}, 'material_9':{'category':'Outdoor NEMA Disconnect Plug Receptacle', 'comment':'Disconnect', 'amount':300.00, 'units':1.00}, 'material_10':{'category':'PVC Conduit Accessories', 'comment':'Schedule 40 Connectors, Couplings, Angles, LB\'s', 'amount':833.50, 'units':0.20}}

# wallPenetrationJson = {'wall_penetration':{'category':'Wall Penetrations', 'amount':50.00, 'units':0.00}, 'concrete_fastening':{'category':'Concrete Work (Fastening)', 'amount':50.00, 'units':0.00}, 'concrete_footer':{'category':'Concrete Work (Footer)', 'amount':50.00, 'units':0.00}, 'concrete_labor':{'category':'Concrete Work (Labor)', 'amount':95.00, 'units':0.00}}

# addOnJson = {'add_on_1':{'category':'Trenching', 'amount':95.00, 'units':0.00}, 'add_on_2':{'category':'Boring', 'amount':95.00, 'units':0.00}, 'add_on_3':{'category':'Equipment Rental & Transportation', 'amount':700.00, 'units':0.00}}

# evceJson = {'evce':{'category':'EVCE', 'comment':'Customer Furnished', 'amount':519.00, 'units':0.00}, 'pedestal':{'category':'Pedestal', 'comment':'TBD', 'amount':325.00, 'units':0.00}, 'surge_protections':{'category':'Surge Protections', 'comment':'TBD', 'amount':100.00, 'units':0.00}, 'smart_switcher':{'category':'Smart Switcher', 'comment':'TBD', 'amount':550.00, 'units':0.00}}

# markup = {'laborPre':0.3, 'subcontractPre':0.3, 'materialsPre':0.25, 'concretePre':0.3, 'evcePre':0.22}

## ATHARV 2
# labourJson = {'labor1':{'category':'Lead Electrician', 'amount':65.00, 'hours':8}, 'labor2':{'category':'Helper', 'amount':30.00, 'hours':8}, 'labor3':{'category':'Helper', 'amount':30.00, 'hours':0}}#, 'inspection':{'category':'Lead Electrician', 'amount':65.00, 'hours':2}}

# subContractorJson = {'electrical_contractor':{'category':'TBD', 'amount':0.00, 'units':0}, 'dry_wall':{'category':'TBD', 'amount':300.00, 'units':1}, 'trenching_and_excavation':{'category':'TBD', 'amount':0.00, 'units':0}}

# permitJson = {'electrical_permitting':{'category':'Electrical Permitting', 'amount':125.00, 'units':1.00}, 'building_permit':{'category':'Building Permit (DC Only)', 'amount':175.00, 'units':0.00}, 'surveyor_fee':{'category':'Surveyor Fee', 'amount':82.00, 'units':0.00}, 'expediting_admin':{'category':'Expediting/Administration', 'amount':500.00, 'units':0.00}, 'master_electrician':{'category':'Master Electrician Fee', 'amount':300.00, 'units':1.00}}

# materialJson = {'material_0':{'category':'Heavy-up', 'amount':0.00, 'units':1.00}, 'material_1a':{'category':'Circuit Breaker Non-GFCI', 'comment':'1 @ 2 Pole/60 amp Cutler/Hammer Tan Circuit Breaker Non-GFI', 'amount':50.00, 'units':1.00}, 'material_1b':{'category':'Circuit Breaker GFIC', 'comment':'2 @ 2 Pole/20 amp Cutler/Hammer Tan Tandems Circuit Breaker', 'amount':40.00, 'units':2.00}, 'material_2':{'category':'Breaker for Disconnect', 'comment':'1 @ 2 Pole/50 amp Square D/Homeline Circuit Breaker', 'amount':30.00, 'units':0.00}, 'material_3a':{'category':'Ridgid PVC Schedule 40 Conduit', 'comment':'Schedule 40 Conduit', 'amount':1.74, 'units':0.00}, 'material_3b':{'category':'Ridgid EMT', 'comment':'EMT', 'amount':1.94, 'units':25.00}, 'material_4':{'category':'Flexible Conduit', 'comment':'1 @ Corlon Flexible Conduit', 'amount':1.75, 'units':0.00}, 'material_5':{'category':'Building Wire (Copper Stranded)', 'comment':'#6AWG/3 wire Copper Stranded', 'amount':5.00, 'units':30.00}, 'material_6':{'category':'Building Wire (Stranded)', 'comment':'#TBDAWG/3 wire Stranded', 'amount':3.00, 'units':0.00}, 'material_7':{'category':'Underground Wire', 'comment':'#6/3 wire Rated Underground Cable', 'amount':0.00, 'units':0.00}, 'material_8':{'category':'Indoor NEMA Disconnect/Plug Receptacle', 'comment':'Flushed or Unflushed', 'amount':0.00, 'units':0.00}, 'material_9':{'category':'Outdoor NEMA Disconnect Plug Receptacle', 'comment':'Disconnect', 'amount':75.00, 'units':1.00}, 'material_10':{'category':'PVC Conduit Accessories', 'comment':'Schedule 40 Connectors, Couplings, Angles, LB\'s', 'amount':403.50, 'units':0.20}}

# wallPenetrationJson = {'wall_penetration':{'category':'Wall Penetrations', 'amount':50.00, 'units':0.00}, 'concrete_fastening':{'category':'Concrete Work (Fastening)', 'amount':50.00, 'units':0.00}, 'concrete_footer':{'category':'Concrete Work (Footer)', 'amount':50.00, 'units':0.00}, 'concrete_labor':{'category':'Concrete Work (Labor)', 'amount':95.00, 'units':0.00}}

# addOnJson = {'add_on_1':{'category':'Trenching', 'amount':95.00, 'units':0.00}, 'add_on_2':{'category':'Boring', 'amount':95.00, 'units':0.00}, 'add_on_3':{'category':'Equipment Rental & Transportation', 'amount':700.00, 'units':0.00}}

# evceJson = {'evce':{'category':'EVCE', 'comment':'Customer Furnished', 'amount':519.00, 'units':0.00}, 'pedestal':{'category':'Pedestal', 'comment':'TBD', 'amount':325.00, 'units':0.00}, 'surge_protections':{'category':'Surge Protections', 'comment':'TBD', 'amount':100.00, 'units':0.00}, 'smart_switcher':{'category':'Smart Switcher', 'comment':'TBD', 'amount':550.00, 'units':0.00}}

# markup = {'laborPre':0.3, 'subcontractPre':0.3, 'materialsPre':0.3, 'concretePre':0.3, 'evcePre':0.22}

## ATHARV 3
labourJson = {'labor1':{'category':'Lead Electrician', 'amount':65.00, 'hours':10}, 'labor2':{'category':'Helper', 'amount':30.00, 'hours':10}, 'labor3':{'category':'Helper', 'amount':30.00, 'hours':0}, 'inspection':{'category':'Lead Electrician', 'amount':65.00, 'hours':2}}

subContractorJson = {'electrical_contractor':{'category':'TBD', 'amount':0.00, 'units':0}, 'dry_wall':{'category':'TBD', 'amount':300.00, 'units':1}, 'trenching_and_excavation':{'category':'TBD', 'amount':0.00, 'units':0}}

permitJson = {'electrical_permitting':{'category':'Electrical Permitting', 'amount':125.00, 'units':1.00}, 'building_permit':{'category':'Building Permit (DC Only)', 'amount':175.00, 'units':0.00}, 'surveyor_fee':{'category':'Surveyor Fee', 'amount':82.00, 'units':0.00}, 'expediting_admin':{'category':'Expediting/Administration', 'amount':500.00, 'units':0.00}, 'master_electrician':{'category':'Master Electrician Fee', 'amount':300.00, 'units':1.00}}

materialJson = {'material_0':{'category':'Heavy-up', 'amount':2000.00, 'units':1.00}, 'material_1a':{'category':'Circuit Breaker Non-GFCI', 'comment':'1 @ 2 Pole/60 amp Cutler/Hammer Tan Circuit Breaker Non-GFI', 'amount':50.00, 'units':1.00}, 'material_1b':{'category':'Circuit Breaker GFIC', 'comment':'2 @ 2 Pole/20 amp Cutler/Hammer Tan Tandems Circuit Breaker', 'amount':40.00, 'units':2.00}, 'material_2':{'category':'Breaker for Disconnect', 'comment':'1 @ 2 Pole/50 amp Square D/Homeline Circuit Breaker', 'amount':30.00, 'units':0.00}, 'material_3a':{'category':'Ridgid PVC Schedule 40 Conduit', 'comment':'Schedule 40 Conduit', 'amount':1.74, 'units':0.00}, 'material_3b':{'category':'Ridgid EMT', 'comment':'EMT', 'amount':1.94, 'units':25.00}, 'material_4':{'category':'Flexible Conduit', 'comment':'1 @ Corlon Flexible Conduit', 'amount':1.75, 'units':0.00}, 'material_5':{'category':'Building Wire (Copper Stranded)', 'comment':'#6AWG/3 wire Copper Stranded', 'amount':5.00, 'units':30.00}, 'material_6':{'category':'Building Wire (Stranded)', 'comment':'#TBDAWG/3 wire Stranded', 'amount':3.00, 'units':0.00}, 'material_7':{'category':'Underground Wire', 'comment':'#6/3 wire Rated Underground Cable', 'amount':0.00, 'units':0.00}, 'material_8':{'category':'Indoor NEMA Disconnect/Plug Receptacle', 'comment':'Flushed or Unflushed', 'amount':0.00, 'units':0.00}, 'material_9':{'category':'Outdoor NEMA Disconnect Plug Receptacle', 'comment':'Disconnect', 'amount':75.00, 'units':1.00}, 'material_10':{'category':'PVC Conduit Accessories', 'comment':'Schedule 40 Connectors, Couplings, Angles, LB\'s', 'amount':2403.50, 'units':0.20}}

wallPenetrationJson = {'wall_penetration':{'category':'Wall Penetrations', 'amount':50.00, 'units':0.00}, 'concrete_fastening':{'category':'Concrete Work (Fastening)', 'amount':50.00, 'units':0.00}, 'concrete_footer':{'category':'Concrete Work (Footer)', 'amount':50.00, 'units':0.00}, 'concrete_labor':{'category':'Concrete Work (Labor)', 'amount':95.00, 'units':0.00}}

addOnJson = {'add_on_1':{'category':'Trenching', 'amount':95.00, 'units':0.00}, 'add_on_2':{'category':'Boring', 'amount':95.00, 'units':0.00}, 'add_on_3':{'category':'Equipment Rental & Transportation', 'amount':700.00, 'units':0.00}}

evceJson = {'evce':{'category':'EVCE', 'comment':'Customer Furnished', 'amount':519.00, 'units':0.00}, 'pedestal':{'category':'Pedestal', 'comment':'TBD', 'amount':325.00, 'units':0.00}, 'surge_protections':{'category':'Surge Protections', 'comment':'TBD', 'amount':100.00, 'units':0.00}, 'smart_switcher':{'category':'Smart Switcher', 'comment':'TBD', 'amount':550.00, 'units':0.00}}

markup = {'laborPre':0.3, 'subcontractPre':0.3, 'materialsPre':0.3, 'concretePre':0.3, 'evcePre':0.22}
