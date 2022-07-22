from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import braintree
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment=braintree.Environment.Sandbox,
        merchant_id='6yjmrn6jh6fcpdmc',
        public_key='3782xqn6nf8g7ym7',
        private_key='1d0c67280bcf986db5a4b4a10dfe8382'
    )
    )

def validate_user_session(id, token):
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    
    except user_model.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, please login again'})
    return JsonResponse({'client_token': gateway.client_token.generate(), 'success': True})
    
@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid session, please login again'})

    nonce_from_the_client = request.form["paymentMethodNonce"]
    amount_from_the_client = request.form["amountFromTheClient"]

    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return JsonResponse({'success': result.is_success,
        'transaction': {'id' : result.transaction.id, 'amount' : result.transaction.amount}
        })
    
    else:
        return JsonResponse({'error': True, 'success': False})
    
