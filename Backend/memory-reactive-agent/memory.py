memory_store = {}


def get_memory(session_id):

    if session_id not in memory_store:
        memory_store[session_id] = []

    return memory_store[session_id]


def save_memory(session_id, message):

    memory = get_memory(session_id)

    memory.append(message)