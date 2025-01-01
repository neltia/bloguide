import uvicorn


# test app run
if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)

    # Path to the certificate and key files
    # context = ('cert.pem', 'key.pem')
    # app.run(debug=True, host="0.0.0.0", port=443, ssl_context=context)
