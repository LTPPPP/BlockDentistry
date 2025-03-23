from flask import Blueprint, request, jsonify, current_app
from models.transaction import Transaction, TransactionType
from models.equipment import DentalEquipment
from api.validators import TransactionValidator, EquipmentValidator

api = Blueprint('api', __name__)

@api.route('/equipment/register', methods=['POST'])
def register_equipment():
    """Register new dental equipment"""
    json_data = request.get_json()
    
    # Validate equipment data
    is_valid, message = EquipmentValidator.validate_equipment(json_data)
    if not is_valid:
        return jsonify({'error': message}), 400
    
    # Create equipment object
    equipment = DentalEquipment(
        name=json_data['name'],
        manufacturer=json_data['manufacturer'],
        model=json_data['model'],
        serial_number=json_data['serial_number'],
        manufacturing_date=json_data['manufacturing_date'],
        expiry_date=json_data.get('expiry_date'),
        category=json_data.get('category'),
        certification_info=json_data.get('certification_info')
    )
    
    # Create a transaction for the new equipment
    transaction = Transaction(
        transaction_type=TransactionType.NEW_EQUIPMENT,
        equipment_id=equipment.id,
        sender=json_data.get('registered_by'),
        details={'equipment': equipment.to_dict()}
    )
    
    # Add the transaction to the blockchain
    blockchain = current_app.config['BLOCKCHAIN']
    block_index = blockchain.add_transaction(transaction)
    
    # Store equipment data in a local database as well (not implemented here)
    
    return jsonify({
        'message': f'Equipment registered and will be added to block {block_index}',
        'equipment_id': equipment.id
    }), 201

@api.route('/equipment/transfer', methods=['POST'])
def transfer_equipment():
    """Transfer equipment ownership"""
    json_data = request.get_json()
    
    required_fields = ['equipment_id', 'sender', 'receiver', 'location']
    for field in required_fields:
        if field not in json_data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    # Create a transaction for the equipment transfer
    transaction = Transaction(
        transaction_type=TransactionType.TRANSFER,
        equipment_id=json_data['equipment_id'],
        sender=json_data['sender'],
        receiver=json_data['receiver'],
        details={
            'location': json_data['location'],
            'notes': json_data.get('notes')
        }
    )
    
    # Add the transaction to the blockchain
    blockchain = current_app.config['BLOCKCHAIN']
    block_index = blockchain.add_transaction(transaction)
    
    # Update equipment data in the local database (not implemented here)
    
    return jsonify({
        'message': f'Transfer will be added to block {block_index}',
        'transaction_id': transaction.id
    }), 201

@api.route('/equipment/maintenance', methods=['POST'])
def record_maintenance():
    """Record equipment maintenance"""
    json_data = request.get_json()
    
    required_fields = ['equipment_id', 'maintenance_type', 'details', 'performed_by']
    for field in required_fields:
        if field not in json_data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    # Create a transaction for the maintenance record
    transaction = Transaction(
        transaction_type=TransactionType.MAINTENANCE,
        equipment_id=json_data['equipment_id'],
        sender=json_data['performed_by'],
        details={
            'maintenance_type': json_data['maintenance_type'],
            'details': json_data['details'],
            'date': json_data.get('date')
        }
    )
    
    # Add the transaction to the blockchain
    blockchain = current_app.config['BLOCKCHAIN']
    block_index = blockchain.add_transaction(transaction)
    
    # Update equipment data in the local database (not implemented here)
    
    return jsonify({
        'message': f'Maintenance record will be added to block {block_index}',
        'transaction_id': transaction.id
    }), 201

@api.route('/equipment/sterilization', methods=['POST'])
def update_sterilization():
    """Update equipment sterilization status"""
    json_data = request.get_json()
    
    required_fields = ['equipment_id', 'status', 'performed_by']
    for field in required_fields:
        if field not in json_data:
            return jsonify({'error': f'Missing field: {field}'}), 400
    
    # Create a transaction for the sterilization update
    transaction = Transaction(
        transaction_type=TransactionType.STERILIZATION,
        equipment_id=json_data['equipment_id'],
        sender=json_data['performed_by'],
        details={
            'status': json_data['status'],
            'method': json_data.get('method'),
            'date': json_data.get('date')
        }
    )
    
    # Add the transaction to the blockchain
    blockchain = current_app.config['BLOCKCHAIN']
    block_index = blockchain.add_transaction(transaction)
    
    # Update equipment data in the local database (not implemented here)
    
    return jsonify({
        'message': f'Sterilization update will be added to block {block_index}',
        'transaction_id': transaction.id
    }), 201

@api.route('/mine_block', methods=['GET'])
def mine_block():
    """Mine a new block"""
    blockchain = current_app.config['BLOCKCHAIN']
    
    # Check if there are pending transactions
    if not blockchain.pending_transactions:
        return jsonify({'message': 'No pending transactions to mine'}), 200
    
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block.proof
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    
    response = {
        'message': 'Mined a new block!',
        'block': block.to_dict()
    }
    
    return jsonify(response), 200

@api.route('/get_chain', methods=['GET'])
def get_chain():
    """Get the full blockchain"""
    blockchain = current_app.config['BLOCKCHAIN']
    response = blockchain.get_chain_data()
    return jsonify(response), 200

@api.route('/equipment/<equipment_id>', methods=['GET'])
def get_equipment_history(equipment_id):
    """Get the history of a specific equipment"""
    blockchain = current_app.config['BLOCKCHAIN']
    
    # Search for transactions related to the equipment
    transactions = []
    for block in blockchain.chain:
        for transaction in block.transactions:
            if transaction.get('equipment_id') == equipment_id:
                transaction_copy = transaction.copy()
                transaction_copy['block_index'] = block.index
                transaction_copy['block_timestamp'] = block.timestamp
                transactions.append(transaction_copy)
    
    return jsonify({
        'equipment_id': equipment_id,
        'transaction_count': len(transactions),
        'transactions': transactions
    }), 200