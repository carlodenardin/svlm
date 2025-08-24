def process_return(return_request: dict) -> dict:
    """
    Implements a product return processing algorithm as described:
    - Validate the return request (product, customer, reason)
    - Check product serial validity and condition
    - Decide eligibility for refund or replacement based on condition and serial
    - Initiate the chosen process (refund or replacement) and prepare details
    - Notify the customer with a summary message

    Input:
    - return_request: dict with keys:
        - product: dict with at least 'product_id', 'serial_number' (optional), 'condition' (optional)
        - customer: dict with at least 'name' (and optionally 'email', 'address', 'phone')
        - reason: str describing the return reason
        - order_total: numeric (optional) total amount of the order
        - order_id: identifier for the order (optional)

    Output:
    - dict containing:
        - status: 'invalid' or 'completed'
        - outcome: 'refund', 'replacement', or 'none'
        - details: dict with process-specific fields
        - notification: textual message prepared for the customer
    """

    def validate_request(req: dict):
        if not isinstance(req, dict):
            return (False, 'Return request must be a dictionary.')
        if 'product' not in req or 'customer' not in req or 'reason' not in req:
            return (False, 'Missing required fields: product, customer, or reason.')
        return (True, '')

    def is_serial_valid(serial: str) -> bool:
        if isinstance(serial, str) and serial.strip():
            return True
        return False

    def determine_outcome(condition: str, serial_valid: bool, reason: str) -> str:
        if not serial_valid:
            return 'none'
        c = (condition or '').lower()
        if c in {'new', 'like_new', 'unused', 'gently_used'}:
            return 'refund'
        if c in {'damaged', 'defective', 'refurbished'}:
            return 'replacement'
        return 'refund'

    def initiate_process(outcome: str, req: dict) -> dict:
        details = {}
        if outcome == 'refund':
            amount = 0.0
            if isinstance(req.get('order_total'), (int, float)):
                amount = float(req.get('order_total'))
            details['refund_amount'] = amount
            details['refund_status'] = 'processed'
        elif outcome == 'replacement':
            order_id = req.get('order_id', 'UNKNOWN')
            product_id = req.get('product', {}).get('product_id', 'UNKNOWN')
            tracking = f'TRK-{str(hash((order_id, product_id)) % 1000000).zfill(6)}'
            details['replacement_status'] = 'initiated'
            details['replacement_tracking'] = tracking
        else:
            details['note'] = 'not eligible for refund or replacement'
        return details

    def notify_customer(outcome: str, req: dict, details: dict) -> str:
        customer = req.get('customer', {})
        name = customer.get('name', 'Customer')
        if outcome == 'refund':
            amount = details.get('refund_amount', 0.0)
            return f'Hello {name}, your refund of ${amount:.2f} has been processed.'
        if outcome == 'replacement':
            tracking = details.get('replacement_tracking', '')
            return f'Hello {name}, a replacement has been initiated. Tracking: {tracking}'
        return f'Hello {name}, your return request could not be processed for a refund or replacement due to eligibility criteria.'
    valid, reason = validate_request(return_request)
    if not valid:
        return {'status': 'invalid', 'reason': reason}
    product = return_request.get('product', {})
    serial = product.get('serial_number', '')
    serial_valid = is_serial_valid(serial)
    condition = product.get('condition', '')
    reason_for_return = return_request.get('reason', '')
    outcome = determine_outcome(condition, serial_valid, reason_for_return)
    details = initiate_process(outcome, return_request)
    notification = notify_customer(outcome, return_request, details)
    return {'status': 'completed', 'outcome': outcome, 'details': details, 'notification': notification}