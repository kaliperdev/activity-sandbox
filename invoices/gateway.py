def charge(client, invoice):
    return client.post("/charge", json=invoice)
