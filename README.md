# EV Charging Estimate Portal – Dai Tech Corp

This project is a web-based internal tool developed for Dai Tech Corp, an EV charging infrastructure startup. The portal streamlines the process of generating installation estimates for residential and commercial EV charging setups.

## Problem Statement

Previously, Dai Tech Corp managed customer estimates through a manual, multi-step workflow:
- Customer leads were fetched from Zoho CRM.
- Electricians performed site visits and noted down materials and setup needs.
- Team members compiled these observations into an Excel-based estimate sheet, calculating labor, materials, permits, trenching, wall mounting, taxes, etc.
- The process was time-consuming, error-prone, and hard to track.

## Solution

Our team digitized and automated this workflow by building a centralized web portal with the following features:

### Features

- Excel Logic Replicated in Python: All estimate calculations previously done in Excel were migrated into reusable Python logic.
- Interactive Web Interface: Built using Streamlit, the UI allows users to:
  - Log in securely (role-based access)
  - Input customer and project details
  - Toggle relevant estimate components (e.g., trenching, wall mounting)
  - Input materials, labor, and other costs interactively
- Estimate Generation: Uses the backend Python logic to calculate total costs, including labor, materials, taxes, and other overheads.
- Data Persistence:
  - Save and retrieve records from MongoDB Atlas
  - Import/export user records from CSV (Zoho integration planned)
- Deployment: Hosted on an AWS EC2 instance for secure, internet-wide access.

## Tech Stack

- Frontend/UI: Streamlit
- Backend Logic: Python
- Database: MongoDB Atlas
- Authentication: Role-based login system
- Deployment: AWS EC2
- CRM Integration (planned): Zoho

## Folder Structure

```
project/
├── auth/
│   ├── trailCreds.yaml
│   └── zohoContact.csv
├── coreLogic.py
├── daiPortal_experimental.py
├── daiPortal.py
├── jsonFiles.py
├── mongodb.py
├── processCustomer.py
└── README.md
```

## Steps to Run This Application

1. Ensure Python 3 is installed and configured on your computer.
2. Install the necessary packages by running:
   ```
   pip install -r requirements.txt
   ```
3. Open the command prompt or terminal.
4. Navigate into the project directory containing the files listed above.
5. Run the application using the command:
   ```
   streamlit run daiPortal.py
   ```

## Future Improvements

- Direct Zoho CRM integration to fetch and update customer leads
- PDF export of final estimates
- Admin dashboard for tracking past estimates and customer analytics
