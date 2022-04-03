import pyciphering

text_to_encode = "Hello, world!"

encoded_text = pyciphering.caesar.encode(text_to_encode, 3)
print(encoded_text)
decoded_text = pyciphering.caesar.decode(encoded_text, 3)
print(decoded_text)

encoded_text = pyciphering.atbash.encode(text_to_encode)
print(encoded_text)
decoded_text = pyciphering.atbash.decode(encoded_text)
print(decoded_text)

encoded_text = pyciphering.viegenere.encode(text_to_encode, "key")
print(encoded_text)
decoded_text = pyciphering.viegenere.decode(encoded_text, "key")
print(decoded_text)

encode_text = pyciphering.bifid.encode(text_to_encode)
print(encode_text)
decode_text = pyciphering.bifid.decode(encode_text)
print(decode_text)

encode_text = pyciphering.trifid.encode(text_to_encode)
print(encode_text)
decode_text = pyciphering.trifid.decode(encode_text)
print(decode_text)

encode_text = pyciphering.polybius.encode(text_to_encode)
print(encode_text)
decode_text = pyciphering.polybius.decode(encode_text)
print(decode_text)