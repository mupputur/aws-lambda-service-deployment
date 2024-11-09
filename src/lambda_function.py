import json


def lambda_handler(event, context):
    customers_data = [{"id":1,
                        "email":"isidro_von@hotmail.com",
                        "name":"Torrey Veum",
                        "company":"Hilll, Mayert and Wolf"
                     }, 
                     {"id":2,
                      "email":"frederique19@gmail.com",
                      "name":"Micah Sanford",
                      "company":"Stokes-Reichel"
                     },
                     {"id":3,
                      "email":"candido.cormier89@gmail.com",
                      "name":"Kristy Quigley",
                      "company":"Brown, Carter and Keeling"
                     }
                    ]
    
    # Get the customer id from the lanvda event
    try:
        if not event or 'id' not in event:
            raise ValueError("Invalid input: 'id' is required")
         
        customer_id  = event.get('id')
        for customer_data in customers_data:
            if customer_data.get('id') == customer_id:
                print(f"Identified the customer id : {customer_id} and processing data...")
                return {
                    "statusCode": 200,
                    "body": json.dumps(customer_data)
                }
        else:
            print(f"Customer id : {customer_id} not found in database record")
            return {
                    "statusCode": 404,
                    "message": "customer 'id' not found"
                }
    except Exception as e:
        print(f"Error occured while processing customer data. ERROR: {str(e)}")
        return {
            "statusCode": 500,
            "message": "Internal Server" 
        }