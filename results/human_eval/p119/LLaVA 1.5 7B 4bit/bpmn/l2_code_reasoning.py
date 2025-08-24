import random
import string
from datetime import datetime

def calculate_refund(price, condition):
    """
    Calculate refund amount based on price and product condition.
    Multipliers:
      new -> 1.0
      like new -> 0.9
      used -> 0.5
      damaged -> 0.2
    """
    multipliers = {
        'new': 1.0,
        'like new': 0.9,
        'used': 0.5,
        'damaged': 0.2
    }
    multiplier = multipliers.get(condition.lower())
    if multiplier is None:
        raise ValueError(f"Unknown condition: {condition}")
    return round(price * multiplier, 2)

def update_inventory(product):
    """
    Update inventory to reflect the returned item being restocked.
    Returns the new inventory count.
    """
    count = product.get('inventory_count', 0)
    new_count = count + 1
    product['inventory_count'] = new_count
    return new_count

def update_customer_records(customer, return_request, refund_id, refund_amount):
    """
    Update customer records with the new return entry.
    Returns the updated customer object.
    """
    if 'returns' not in customer:
        customer['returns'] = []
    entry = {
        'refund_id': refund_id,
        'refund_amount': refund_amount,
        'product_sku': return_request.get('product', {}).get('sku'),
        'reason': return_request.get('reason'),
        'date': datetime.utcnow().isoformat() + 'Z'
    }
    customer['returns'].append(entry)
    return customer

def send_email(customer, product, refund_amount, refund_id, processing_time_days):
    """
    Simulate sending a confirmation email to the customer.
    Returns True if email "sent".
    """
    subject = f"Return Refund Confirmation - {refund_id}"
    body = (
        f"Hello {customer.get('name','')},\n\n"
        f"Your return for '{product.get('name','product')}' has been processed.\n"
        f"Refund Amount: ${refund_amount:.2f}\n"
        f"Refund ID: {refund_id}\n"
        f"Estimated processing time: {processing_time_days} day(s).\n\n"
        "Thank you for shopping with us."
    )
    # In a real system, send email using an SMTP service or API.
    # Here we simply simulate by returning True.
    return True

def process_return(return_request):
    """
    Process a product return according to the described algorithm.
    
    return_request: dict with keys
      - 'customer': dict with at least 'name' and 'email'
      - 'product': dict with at least 'name', 'sku', 'price', 'inventory_count' (optional), 'condition'
      - 'reason': str
      - 'payment_method': str
    Returns a summary dict with processing details.
    """
    logs = []
    
    # Extract inputs
    customer = return_request.get('customer')
    product = return_request.get('product')
    reason = return_request.get('reason')
    payment_method = return_request.get('payment_method', 'default')
    
    # Step 1: Verify customer information and return reason
    if not isinstance(customer, dict) or not customer.get('name') or not customer.get('email'):
        raise ValueError("Invalid customer information")
    logs.append("Step 1: Customer information verified.")
    
    if not reason:
        raise ValueError("Return reason must be provided.")
    logs.append("Step 1.1: Return reason verified.")
    
    # Step 2: Check product availability and condition
    if not isinstance(product, dict) or product.get('price') is None or product.get('sku') is None:
        raise ValueError("Invalid product information")
    condition = product.get('condition', '').lower()
    if condition not in {'new', 'like new', 'used', 'damaged'}:
        raise ValueError("Unsupported product condition.")
    logs.append(f"Step 2: Product verified with condition '{condition}'.")
    
    # Step 3: Calculate refund amount based on price and condition
    price = float(product.get('price'))
    refund_amount = calculate_refund(price, condition)
    logs.append(f"Step 3: Refund amount calculated: {refund_amount:.2f}")
    
    # Step 4: Notify customer of the refund amount and processing time
    processing_time_days = 3  # assumed processing time
    notify_message = f"Refund of ${refund_amount:.2f} will be processed in {processing_time_days} day(s)."
    logs.append("Step 4: Notification prepared: " + notify_message)
    
    # Step 5: Process the refund using the chosen payment method
    refund_id = "RFND-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    # In a real system, integrate with payment gateway here.
    logs.append(f"Step 5: Refund processed via {payment_method}. Refund ID: {refund_id}")
    
    # Step 6: Update product inventory and customer records
    new_inventory = update_inventory(product)
    updated_customer = update_customer_records(customer, return_request, refund_id, refund_amount)
    logs.append("Step 6: Inventory and customer records updated.")
    
    # Step 7: Send a confirmation email to the customer
    email_sent = send_email(customer, product, refund_amount, refund_id, processing_time_days)
    logs.append("Step 7: Confirmation email sent.")
    
    return {
        'status': 'completed',
        'refund_id': refund_id,
        'refund_amount': round(refund_amount, 2),
        'processing_time_days': processing_time_days,
        'inventory_count_after_update': new_inventory,
        'customer_records_current': updated_customer,
        'email_sent': email_sent,
        'logs': logs
    }

# Example usage (commented out - for illustration only):
# if __name__ == "__main__":
#     req = {
#         'customer': {'name': 'Alice Smith', 'email': 'alice@example.com'},
#         'product': {'name': 'Widget Pro', 'sku': 'WP-1000', 'price': 99.99, 'condition': 'Used', 'inventory_count': 5},
#         'reason': 'No longer needed',
#         'payment_method': 'credit_card'
#     }
#     result = process_return(req)
#     print(result)