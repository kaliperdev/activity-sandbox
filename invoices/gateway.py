def charge(client, invoice, tries=2):
    for attempt in range(tries):
        try:
            return client.post("/charge", json=invoice, timeout=10)
        except TimeoutError:
            if attempt == tries - 1:
                raise
