#THIS FILE IS ONLY FOR TESTING, DO NOT USE THIS
import asyncio
import aiocoap
from flask import Flask, request

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def http_to_coap_proxy(path):
    print(path)
    # Convert the HTTP request to a CoAP request
    coap_request = aiocoap.Message(
        code= GET,
        uri=f'coap://127.0.0.1/{path}',
        payload=request.data,
        opt=aiocoap.Options(
            content_format=aiocoap.ContentFormat.APPLICATION_JSON,
        ),
    )
    coap_request.update(request.headers)

    # Send the CoAP request and get the response
    try:
        coap_response = aiocoap.Context.create_client_context().request(coap_request).response
    except Exception as e:
        print(f'Failed to send request: {e}')
        return '', 500

    # Convert the CoAP response to an HTTP response
    http_response = app.make_response((coap_response.payload, coap_response.code.value))
    http_response.headers.extend(coap_response.items())

    return http_response

# Run the HTTP server
app.run()