def handle_response(msg):
    try:
        print(msg['transcriptions'][0])
    except (KeyError) as ex:
        pass