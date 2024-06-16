# flask
from app import create_app


app = create_app()


# test app run
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

    # Path to the certificate and key files
    # context = ('cert.pem', 'key.pem')
    # app.run(debug=True, host="0.0.0.0", port=443, ssl_context=context)
