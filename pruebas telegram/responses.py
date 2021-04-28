def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ("hola","ola","hi"):
        return "Hola papá" 
    
    if user_message in ("quien sos","quien chota sos","como te llamas"):
        return "Soy Peer, El bot"

    return "No te entiendo mano"