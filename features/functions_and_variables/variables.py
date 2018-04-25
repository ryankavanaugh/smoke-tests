zebra_url = '.thezebra.com/'
prepop_link = "https://release.onebox.thezebra.com/prepoptest/"
prepop_api_link = "https://release.onebox.thezebra.com/api/ext/v1/prepop/"

payload_test = {"responses":{"start":{"currently_insured":0},"vehicles":[{"vehicle_id":255273,"id":"vehicles-ba28-bd33-b258-001131ed3bba","year":2017,"make":"Audi","model":"A4","submodel":"2.0T Prestige 4dr Sedan","ownership":2,"primary_use":1,"miles":1,"garaging_address":"1122 South Lamar Boulevard"}],"drivers":[{"other_applicable":{},"id":"drivers-f8b4-6191-a4a6-1b7dcd4b60bc","first_name":"Derek","last_name":"Miles","date_of_birth":"09/17/1989","email":"abc@thezebra.com","phone":"(888) 888-8888","gender":0,"marital_status":1,"credit_score":2,"education":1,"residence_ownership":1,"violations":{"value":0,"incidents":[]}}],"discounts":{"currently_insured":0,"low_mileage":0,"multi_vehicle":0,"new_car_discount":1,"good_credit":0,"home_owner":0,"condo_owner":1,"no_violations":1,"currently_employed":1,"active_military":1,"pay_up_front":1,"auto_pay":1,"paperless":1},"zipcode":"78704","city":"Austin","state":"TX"}}


thirteen_prepop_headers = {
        'Authorization': "Token 46b355d640f6ca4962fcd1c5ae662a8a1b9fd7ab",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "9143bcb9-5bbc-4426-8022-24a6099c28c9"
        }


release_and_prod_prepop_headers = {
        'Authorization': "Token ceb351e14a24199533b5d46dc15b0b692af4ddd0",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "9143bcb9-5bbc-4426-8022-24a6099c28c9"
        }


jesse_durante_payload = '''{
  "first_name": "Jesse",
  "last_name": "Durante",
  "Email": "xyz@thezebra.com",
  "phone_number": "888.888.8888",
  "address": "2267 NW Glisan Street",
  "city": "Portland",
  "state": "OR",
  "zipcode": "97210",
  "prior_carrier": "AAA",
  "is_test": true,
  "prior_carrier_coverage_months": "2 years",
  "home_ownership": "Condo Owner",
  "credit_score": "Excellent (720+)",
  "currently_insured": true,
  "desired_coverage": "Superior",
  "vehicles": [
    {
      "vin": "1J4NT1FB2AD456789",
      "year": 2010,
      "make": "Jeep",
      "model": "Compass",
      "submodel": "no info",
      "ownership": "Lease",
      "has_alarm": false,
      "miles_per_year": "Over 15,000",
      "collision": 250,
      "comprehensive": 150,
      "primary_use": "Commute to work/school",
      "rental_limit": "25/750",
      "towing_limit": 35
    }
  ],
  "drivers": [
    {
      "first_name": "Tyra",
      "last_name": "Durante",
      "dob": "1990-08-17",
      "age": 27,
      "age_first_licensed": 18,
      "gender": "Female",
      "marital_status": false,
      "good_student": true,
      "drivers_training": true,
      "excluded": true,
      "education": "Bachelors Degree",
      "driver_relationship": "Spouse",
      "employment": "Employed",
      "incidents": []
    }
  ]
}'''


drift_api_headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "close",
        'Content-Length': "4772",
        'Content-Type': "application/json",
        'Host': "drift.thezebra.com",
        'User-Agent': "python-requests/2.18.1",
        'Cache-Control': "no-cache",
        'Postman-Token': "3ac6066c-d92f-4ffd-95b5-e2becf004d3e"
}


laura_johnson_payload = '''{
  "first_name": "Laura",
  "last_name": "Johnson",
  "Email": "xyz@thezebra.com",
  "phone_number": "8888888888",
  "address": "123 Main St.",
  "city": "Austin",
  "state": "TX",
  "zipcode": "78704",
  "prior_carrier": "USAA",
  "is_test": true,
  "prior_carrier_coverage_months": "1 year",
  "home_ownership": "Home Owner",
  "credit_score": "Good (680-719)",
  "currently_insured": true,
  "desired_coverage": "Standard",
  "vehicles": [
    {
      "vin": "3MEHM0JG7BR456789",
      "year": 2017,
      "make": "Porsche",
      "model": "911",
      "submodel": "AWD Carrera 4 2dr Convertible",
      "ownership": "Finance",
      "has_alarm": true,
      "miles_per_year": "6,001 - 10,000",
      "collision": 1000,
      "comprehensive": 100,
      "primary_use": "Pleasure",
      "rental_limit": "20/600",
      "towing_limit": 0
    }
  ],
  "drivers": [
    {
      "first_name": "Laura",
      "last_name": "Johnson",
      "dob": "1992-04-19",
      "age": 26,
      "age_first_licensed": 22,
      "gender": "Male",
      "marital_status": true,
      "good_student": true,
      "drivers_training": true,
      "excluded": false,
      "education": "No Diploma",
      "driver_relationship": "Other Related",
      "employment": "Retired",
      "has_incidents": false,
      "incidents": [
        {
          "category": "Auto Accident (At Fault)",
          "incident_type": "Vehicle damage"
        },
        {
          "category": "DUI or DWI",
          "incident_type": "DUI or DWI"
        },
        {
          "category": "Auto Accident (At Fault)",
          "incident_type": "Vehicle damage"
        }
      ]
    }
  ]
}'''


drift_api_payload_1 = '''{
"isTestLead": true,
"transactionId": "9a673c8f899142e4b5ff81b703704968",
"tracking": {
"quoteId": "5ac3cebcc3f6154f1832587e",
"browser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"ipAddress": "38.140.212.234",
"marketSegmentId": "1SD4Q",
"clientType": "DESKTOP"
},
"policyData": {
"policyCoverage": {
"fullGlass": false,
"deathIndemnity": 0,
"underinsuredMotoristPerAccident": 0,
"coverageCode": "BASIC",
"firstPartyBenefitsLimit": 0,
"medicalPaymentLimit": 0,
"underinsuredMotoristPropertyDamageLimit": 0,
"policyTermMonths": 6,
"liabilityPerPerson": 30000,
"uninsuredMotoristPerPerson": 0,
"liabilityPerAccident": 60000,
"includeWageLoss": false,
"underinsuredMotoristPerPerson": 0,
"personalInjuryLimit": 0,
"uninsuredMotoristPerAccident": 0,
"personalInjuryDeductible": 0,
"uninsuredMotoristPropertyDamageLimit": 0,
"propertyDamageLimit": 25000
},
"drivers": [
{
"hadDriverTraining": "NO",
"isExcluded": false,
"birthDate": "1991-02-12T00:00:00Z",
"relationshipToPrimaryDriver": "SELF",
"ageLicensed": 0,
"licenseStatus": "VALID",
"education": "BACHELORS_DEGREE",
"occupation": "EMPLOYED",
"city": "Austin",
"zip": "78704",
"state": "TX",
"residenceType": "APARTMENT",
"stateLicensed": "TX",
"isGoodStudent": "NO",
"employedDate": "2017-04-03T13:58:37.472097Z",
"address2": "",
"ownResidence": "NO",
"phone": "8888888888",
"address": "123 Main St.",
"county": "Travis",
"relationshipStatus": "SINGLE",
"firstName": "Larry",
"gender": "MALE",
"creditRating": "EXCELLENT",
"email": "xyz@thezebra.com",
"requireSr22": "NO",
"monthsAtResidence": 24,
"incidents": [],
"lastName": "Jones"
}
],
"vehicles": [
{
"trim": "C Platinum",
"vehicleCoverage": {
"comprehensive": 500,
"towingLimit": 0,
"rentalLimitPerDay": 0,
"rentalLimitPerAccident": 0,
"collision": 500
},
"annualMileage": 15000,
"vin": "2C3CCASGGH",
"garagingAddress": "123 Main St.",
"ownershipType": "LEASE",
"year": 2016,
"primaryUse": "PLEASURE",
"model": "300",
"make": "Chrysler",
"msrp": 45190,
"hasAlarm": "NO"
}
],
"isMultiPolicy": "NO",
"contact": {
"city": "Austin",
"gender": "MALE",
"firstName": "Larry",
"zip": "78704",
"employedDate": "2017-04-03T13:58:37.471424Z",
"lastName": "Jones",
"address2": "",
"creditRating": "EXCELLENT",
"relationshipStatus": "SINGLE",
"birthDate": "1991-02-12T00:00:00Z",
"county": "Travis",
"phone": "8888888888",
"state": "TX",
"residenceType": "APARTMENT",
"address": "123 Main St.",
"education": "BACHELORS_DEGREE",
"email": "xyz@thezebra.com",
"ownResidence": "NO",
"occupation": "EMPLOYED"
},
"basePolicyData": {
"isNonOwner": false,
"insuranceLine": "AUTO"
}
},
"requestedCarriers": [
{
"producerCode": "42E345",
"carrierExternalId": "Mercury",
"requestedProducts": [
{
"productExternalId": "26742559",
"isRealtimeProduct": true
}
],
"requestorId": "768988C2-2A28-420C-8C9E-322548E332A8",
"carrierPassword": "Zebra2018!",
"carrierId": "42E345admn",
"carrierName": "Mercury",
"orderCreditScore": false
},
{
"producerCode": "4230455-000-000",
"carrierExternalId": "Hallmark",
"requestedProducts": [
{
"productExternalId": "10032078",
"isRealtimeProduct": true
}
],
"requestorId": "768988C2-2A28-420C-8C9E-322548E332A8",
"carrierPassword": "TacoLife18",
"carrierId": "inszebra000",
"carrierName": "Hallmark",
"orderCreditScore": false
}
]
}'''


drift_api_payload_2 = '''{
"isTestLead": true,
"transactionId": "b892165913484056ac7c2f6b2821aca9",
"tracking": {
"quoteId": "5ac3d6e90f7d077aa2c97f3b",
"browser": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"ipAddress": "50.0.163.247",
"marketSegmentId": "3AVD1",
"clientType": "DESKTOP"
},
"policyData": {
"policyCoverage": {
"fullGlass": false,
"deathIndemnity": 0,
"underinsuredMotoristPerAccident": 100000,
"coverageCode": "BETTER",
"firstPartyBenefitsLimit": 0,
"medicalPaymentLimit": 1000,
"underinsuredMotoristPropertyDamageLimit": 0,
"policyTermMonths": 6,
"liabilityPerPerson": 50000,
"uninsuredMotoristPerPerson": 50000,
"liabilityPerAccident": 100000,
"includeWageLoss": false,
"underinsuredMotoristPerPerson": 50000,
"personalInjuryLimit": 0,
"uninsuredMotoristPerAccident": 100000,
"personalInjuryDeductible": 0,
"uninsuredMotoristPropertyDamageLimit": 0,
"propertyDamageLimit": 50000
},
"currentCoverage": {
"startDate": "2015-04-03T14:45:53.781005Z",
"liabilityPerPerson": 50000,
"liabilityPerAccident": 100000,
"carrierId": "nationwide",
"expirationDate": "2018-05-03T14:45:53.777510Z",
"propertyDamageLimit": 50000
},
"drivers": [
{
"hadDriverTraining": "NO",
"isExcluded": false,
"birthDate": "1952-11-28T00:00:00Z",
"relationshipToPrimaryDriver": "SELF",
"ageLicensed": 0,
"licenseStatus": "VALID",
"education": "HIGH_SCHOOL_DIPLOMA",
"occupation": "EMPLOYED",
"city": "Sebastopol",
"zip": "95472",
"state": "CA",
"residenceType": "CONDO",
"stateLicensed": "CA",
"isGoodStudent": "NO",
"employedDate": "2017-04-03T14:45:53.774246Z",
"address2": "",
"ownResidence": "YES",
"phone": "8888888888",
"address": "8301 Valley View Court",
"county": "Sonoma",
"relationshipStatus": "MARRIED",
"firstName": "Tess",
"gender": "FEMALE",
"creditRating": "FAIR",
"email": "abc@thezebra.com",
"requireSr22": "NO",
"monthsAtResidence": 24,
"incidents": [],
"lastName": "Ward"
},
{
"hadDriverTraining": "NO",
"isExcluded": false,
"birthDate": "1945-09-07T00:00:00Z",
"county": "Sonoma",
"relationshipToPrimaryDriver": "UNKNOWN",
"ageLicensed": 0,
"licenseStatus": "VALID",
"education": "BACHELORS_DEGREE",
"occupation": "EMPLOYED",
"city": "Sebastopol",
"zip": "95472",
"state": "CA",
"isGoodStudent": "NO",
"stateLicensed": "CA",
"residenceType": "UNKNOWN",
"address2": "",
"ownResidence": "UNKNOWN",
"phone": "8888888888",
"address": "8301 Valley View Court",
"employedDate": "2017-04-03T14:45:53.777177Z",
"relationshipStatus": "MARRIED",
"firstName": "Dominic",
"gender": "MALE",
"creditRating": "UNKNOWN",
"email": "abc@thezebra.com",
"requireSr22": "NO",
"monthsAtResidence": 24,
"incidents": [],
"lastName": "Ward"
}
],
"vehicles": [
{
"trim": "Base",
"vehicleCoverage": {
"comprehensive": 500,
"towingLimit": 0,
"rentalLimitPerDay": 30,
"rentalLimitPerAccident": 900,
"collision": 500
},
"annualMileage": 6000,
"vin": "JTJHF10U10",
"garagingAddress": "8301 Valley View Court",
"ownershipType": "OWN",
"year": 2001,
"primaryUse": "PLEASURE",
"model": "RX 300",
"make": "Lexus",
"msrp": 36250,
"hasAlarm": "NO"
},
{
"trim": "Base",
"vehicleCoverage": {
"comprehensive": 500,
"towingLimit": 0,
"rentalLimitPerDay": 30,
"rentalLimitPerAccident": 900,
"collision": 500
},
"annualMileage": 6000,
"vin": "1FTEE142VH",
"garagingAddress": "8301 Valley View Court",
"ownershipType": "OWN",
"year": 1997,
"primaryUse": "BUSINESS",
"model": "E-150",
"make": "Ford",
"msrp": 19370,
"hasAlarm": "NO"
}
],
"contact": {
"city": "Sebastopol",
"gender": "FEMALE",
"firstName": "Tess",
"zip": "95472",
"employedDate": "2017-04-03T14:45:53.771206Z",
"lastName": "Ward",
"address2": "",
"creditRating": "FAIR",
"relationshipStatus": "MARRIED",
"birthDate": "1952-11-28T00:00:00Z",
"county": "Sonoma",
"phone": "8888888888",
"state": "CA",
"residenceType": "CONDO",
"address": "8301 Valley View Court",
"education": "HIGH_SCHOOL_DIPLOMA",
"email": "abc@thezebra.com",
"ownResidence": "YES",
"occupation": "EMPLOYED"
},
"isMultiPolicy": "NO",
"basePolicyData": {
"isNonOwner": false,
"insuranceLine": "AUTO"
}
},
"requestedCarriers": [
{
"producerCode": "5513263",
"carrierExternalId": "Infinity",
"requestedProducts": [
{
"productExternalId": "2625830",
"isRealtimeProduct": true
}
],
"requestorId": "768988C2-2A28-420C-8C9E-322548E332A8",
"carrierPassword": "e@tMOREtac0s",
"carrierId": "5513263",
"carrierName": "Infinity",
"orderCreditScore": true
},
{
"producerCode": "2006597",
"carrierExternalId": "Kemper Specialty",
"requestedProducts": [
{
"productExternalId": "528722-1",
"isRealtimeProduct": false
}
],
"requestorId": "768988C2-2A28-420C-8C9E-322548E332A8",
"carrierPassword": "e@tMOREtac0s20",
"carrierId": "2006597",
"carrierName": "Kemper Specialty",
"orderCreditScore": false
}
]
}'''

payment_plan_counter = 0

# incidents": [
#     {
#         "category": "DUI or DWI",
#         "incident_type": "DUI or DWI"
#     }
# ]

#