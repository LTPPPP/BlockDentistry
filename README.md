# Dental Equipment Blockchain System

A blockchain-based system for tracking dental equipment throughout its lifecycle. This system provides a secure, immutable record of equipment registration, transfers, maintenance, and sterilization processes.

## Features

- **Equipment Registration**: Register new dental equipment with detailed information
- **Ownership Transfer**: Track transfers of equipment between owners and locations
- **Maintenance Records**: Keep immutable maintenance history records
- **Sterilization Tracking**: Monitor sterilization status and methods
- **Blockchain Security**: All transactions are securely stored on a blockchain
- **Simple Web Interface**: Easy-to-use UI for interacting with the system

## Project Structure

```
├── blockchain/         # Core blockchain implementation
│   ├── __init__.py
│   ├── block.py        # Block data structure
│   ├── blockchain.py   # Blockchain implementation
│   └── proof_mechanisms.py  # Consensus algorithms
├── models/             # Data models
│   ├── __init__.py
│   ├── equipment.py    # Dental equipment model
│   ├── transaction.py  # Transaction model
│   └── user.py         # User model
├── api/                # API endpoints
│   ├── __init__.py
│   ├── routes.py       # API route definitions
│   └── validators.py   # Request validators
├── utils/              # Utility functions
│   ├── __init__.py
│   ├── crypto.py       # Cryptographic functions
│   └── serializers.py  # Data serializers
├── templates/          # HTML templates
│   └── index.html      # Main UI interface
├── config.py           # Configuration settings
├── app.py              # Application entry point
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── LICENSE             # License information
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/LTPPPP/BlockDentistry.git
   cd BlockDentistry
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Access the web interface at http://localhost:5000

## API Endpoints

### Equipment Management

- `POST /api/equipment/register` - Register new dental equipment
- `POST /api/equipment/transfer` - Transfer equipment ownership
- `POST /api/equipment/maintenance` - Record equipment maintenance
- `POST /api/equipment/sterilization` - Update equipment sterilization status
- `GET /api/equipment/<equipment_id>` - Get equipment history

### Blockchain Operations

- `GET /api/mine_block` - Mine a new block
- `GET /api/get_chain` - Get the full blockchain

## Usage Examples

### Registering New Equipment

```json
POST /api/equipment/register
{
  "name": "Dental Chair",
  "manufacturer": "DentalTech",
  "model": "DT-2000",
  "serial_number": "DT2000-12345",
  "manufacturing_date": "2024-01-15",
  "expiry_date": "2034-01-15",
  "category": "treatment",
  "registered_by": "Dr. Smith",
  "certification_info": {
    "certification_body": "Dental Equipment Regulatory Authority",
    "certificate_number": "DERA-789456",
    "issue_date": "2024-01-20"
  }
}
```

### Transferring Equipment

```json
POST /api/equipment/transfer
{
  "equipment_id": "a1b2c3d4-e5f6-7890-abcd-1234567890ab",
  "sender": "Dr. Smith",
  "receiver": "Dr. Johnson",
  "location": "Clinic B, Room 105",
  "notes": "Transferred as part of clinic expansion"
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security Considerations

- This system is designed for tracking and record-keeping purposes
- The blockchain implementation provides immutability and transparency
- For production use, additional security measures should be implemented including authentication, authorization, and data validation

## Future Enhancements

- User authentication and role-based access control
- Advanced search and reporting features
- Integration with dental practice management systems
- Mobile application for easy scanning and tracking
- Support for IoT sensors for automated status updates
