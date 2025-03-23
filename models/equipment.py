from datetime import datetime
from utils.crypto import generate_uuid

class DentalEquipment:
    def __init__(self, name, manufacturer, model, serial_number, manufacturing_date,
                 expiry_date=None, sterilization_status=False, maintenance_history=None,
                 certification_info=None, category=None):
        self.id = generate_uuid()
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number
        self.manufacturing_date = manufacturing_date
        self.expiry_date = expiry_date
        self.sterilization_status = sterilization_status
        self.maintenance_history = maintenance_history or []
        self.certification_info = certification_info or {}
        self.category = category
        self.current_owner = None
        self.location = None
        self.status = "new"  # new, in_use, needs_maintenance, disposed
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_sterilization_status(self, status, performed_by, timestamp=None):
        """Update the sterilization status of the equipment"""
        self.sterilization_status = status
        self.updated_at = timestamp or datetime.now()
        self.maintenance_history.append({
            'type': 'sterilization',
            'status': status,
            'performed_by': performed_by,
            'timestamp': self.updated_at
        })
    
    def add_maintenance_record(self, maintenance_type, details, performed_by, timestamp=None):
        """Add a maintenance record to the equipment"""
        record_time = timestamp or datetime.now()
        maintenance_record = {
            'type': maintenance_type,
            'details': details,
            'performed_by': performed_by,
            'timestamp': record_time
        }
        self.maintenance_history.append(maintenance_record)
        self.updated_at = record_time
        return maintenance_record
    
    def transfer_ownership(self, new_owner, location, timestamp=None):
        """Transfer ownership of the equipment"""
        self.current_owner = new_owner
        self.location = location
        self.updated_at = timestamp or datetime.now()
    
    def update_status(self, status, reason=None, updated_by=None, timestamp=None):
        """Update the status of the equipment"""
        self.status = status
        self.updated_at = timestamp or datetime.now()
        
        status_update = {
            'from': self.status,
            'to': status,
            'reason': reason,
            'updated_by': updated_by,
            'timestamp': self.updated_at
        }
        
        self.maintenance_history.append(status_update)
    
    def to_dict(self):
        """Convert the equipment to a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'model': self.model,
            'serial_number': self.serial_number,
            'manufacturing_date': self.manufacturing_date,
            'expiry_date': self.expiry_date,
            'sterilization_status': self.sterilization_status,
            'maintenance_history': self.maintenance_history,
            'certification_info': self.certification_info,
            'category': self.category,
            'current_owner': self.current_owner,
            'location': self.location,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }