#!/usr/bin/env python
# https://en.bitcoin.it/wiki/Protocol_documentation#Addresses

import hashlib
import base58

# ECDSA bitcoin Public Key
pubkey = '04b6ce0b255740891c56ac3b298695bad5449dcc216259f79a5fab81c18f7f3fcd5e9c1471b4c7eb7df6a94ed71aee6255be9a18d75c0dc59c9392c6a1cba2e515'
# See 'compressed form' at https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
compress_pubkey = False


def hash160(hex_str):
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(hex_str)
    rip.update( sha.digest() )
    print ( "key_hash = \t" + rip.hexdigest() )
    return rip.hexdigest()  # .hexdigest() is hex ASCII


if (compress_pubkey):
    if (ord(bytearray.fromhex(pubkey[-2:])) % 2 == 0):
        pubkey_compressed = '02'
    else:
        pubkey_compressed = '03'
    pubkey_compressed += pubkey[2:66]
    hex_str = bytearray.fromhex(pubkey_compressed)
else:
    hex_str = bytearray.fromhex(pubkey)

# Obtain key:

key_hash = '3C' + hash160(hex_str)

# Obtain signature:

sha = hashlib.sha256()
sha.update( bytearray.fromhex(key_hash) )
checksum = sha.digest()
sha = hashlib.sha256()
sha.update(checksum)
checksum = sha.hexdigest()[0:8]

print ( "checksum = \t" + sha.hexdigest() )
print ( "key_hash + checksum = \t" + key_hash + ' ' + checksum )
print ( "bitcoin address = \t" + base58.b58encode( bytes(bytearray.fromhex(key_hash + checksum)) ) )
