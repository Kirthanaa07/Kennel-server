CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "status": "Active"
    }
]

def get_all_customers():
  return CUSTOMERS

def get_single_customer(id):
  request_customer = None
  
  for customer in CUSTOMERS:
    if customer["id"] == id:
      request_customer = customer
      
  return request_customer  

def create_customer(customer):
  
  max_id = CUSTOMERS[-1]["id"]
  
  new_id = max_id + 1
  
  customer["id"] = new_id
  
  CUSTOMERS.append(customer)
  
  return customer

def delete_customer(customer):
    
    customer_index = -1
    
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
            
            
    if customer_index >= 0:
         CUSTOMERS.pop(customer_index) 
         
         
def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
         if customer["id"] == id:
           CUSTOMERS[index] = new_customer
           break            
      