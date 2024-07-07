import base64   #The base64 module is imported to use the Base64 encoding and decoding functions
def hex_base64(hex_str): #The variable hex_string is a string of characters contains a hexadecimal string that we want to convert to Base64
    data_in_bytes = bytes.fromhex(hex_str) # converts a hexadecimal string(hex-string) to its byte equivalent(data_in_bytes)
    data_in_base64 = base64.b64encode(data_in_bytes) # encodes bytes (data_in_bytes) into a Base64 string (data_in_base)
    return data_in_base64.decode('utf-8') # Cette méthode convertit les octets encodés en Base64 en une chaîne de caractères en utilisant l'encodage UTF-8.
if __name__ == "__main__":
 
   #give a value to the variable hex_str 
   hex_str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
   #Call the gex_base64 function
   base64_str= hex_base64(hex_str)
   #show the resultat
   print(base64_str)
    
