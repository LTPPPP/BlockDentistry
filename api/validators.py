class TransactionValidator:
    @staticmethod
    def validate_equipment_transaction(transaction, required_fields=None):
        """Validate an equipment transaction"""
        if required_fields is None:
            required_fields = ['transaction_type', 'equipment_id', 'sender']
        
        # Check that all required fields are present
        for field in required_fields:
            if field not in transaction or not transaction[field]:
                return False, f"Missing required field: {field}"
        
        # Additional validation can be added here based on transaction type
        return True, "Transaction is valid"

class EquipmentValidator:
    @staticmethod
    def validate_equipment(equipment, required_fields=None):
        """Validate equipment data"""
        if required_fields is None:
            required_fields = ['name', 'manufacturer', 'model', 'serial_number', 'manufacturing_date']
        
        # Check that all required fields are present
        for field in required_fields:
            if field not in equipment or not equipment[field]:
                return False, f"Missing required field: {field}"
        
        # Additional validation can be added here
        return True, "Equipment is valid"