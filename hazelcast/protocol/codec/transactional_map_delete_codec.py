from hazelcast.serialization.bits import *
from hazelcast.protocol.client_message import ClientMessage
from hazelcast.protocol.custom_codec import *
from hazelcast.util import ImmutableLazyDataList
from hazelcast.protocol.codec.transactional_map_message_type import *

REQUEST_TYPE = TRANSACTIONALMAP_DELETE
RESPONSE_TYPE = 100
RETRYABLE = False


def calculate_size(name, txn_id, thread_id, key):
    """ Calculates the request payload size"""
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += calculate_size_str(txn_id)
    data_size += LONG_SIZE_IN_BYTES
    data_size += calculate_size_data(key)
    return data_size


def encode_request(name, txn_id, thread_id, key):
    """ Encode request into client_message"""
    client_message = ClientMessage(payload_size=calculate_size(name, txn_id, thread_id, key))
    client_message.set_message_type(REQUEST_TYPE)
    client_message.set_retryable(RETRYABLE)
    client_message.append_str(name)
    client_message.append_str(txn_id)
    client_message.append_long(thread_id)
    client_message.append_data(key)
    client_message.update_frame_length()
    return client_message


# Empty decode_response(client_message), this message has no parameters to decode



