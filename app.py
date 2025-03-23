from flask import Flask, render_template
from blockchain.blockchain import Blockchain
from api.routes import api
from config import config_by_name

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    # Initialize blockchain
    blockchain = Blockchain(difficulty=app.config['BLOCKCHAIN_DIFFICULTY'])
    app.config['BLOCKCHAIN'] = blockchain
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(host='0.0.0.0', port=5000)