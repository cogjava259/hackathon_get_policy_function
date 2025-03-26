import functions_framework
from flask import jsonify
from mock_data import MOCK_COMMISSION_DATA


@functions_framework.http
def get_commission(request):
    """HTTP Cloud Function for fetching commission details."""

    # Enable CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type'
    }

    # Handle CORS preflight requests
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        # Get policy_id from query parameters
        policy_id = request.args.get('policy_id')

        if not policy_id:
            return jsonify({
                'status': 'error',
                'message': 'Policy ID is required'
            }), 400, headers

        # Fetch commission details from mock data
        commission = MOCK_COMMISSION_DATA.get(policy_id)

        if not commission:
            return jsonify({
                'status': 'error',
                'message': 'Commission details not found'
            }), 404, headers

        return jsonify({
            'status': 'success',
            'data': commission
        }), 200, headers

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500, headers
