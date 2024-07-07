def xor_opr(buf1,buf2):
    #converts a hexadecimal string to its byte equivalent
    buf1_in_bytes = bytes.fromhex(buf1)
    buf2_in_bytes = bytes.fromhex(buf2)
    #Checks that both strings are the same length.
    if len(buf1_in_bytes)!=len(buf1_in_bytes):
        raise ValueError("ERROR,THE BUFFERS SHOULD HAVE THE SAME LENGTH ") #  the function raise ValueError for throwing exceptions or errors
    # the XOR operation on each byte pair
    xor_result = bytes(n ^ m for n, m in zip(buf1_in_bytes, buf2_in_bytes ))
    #Converts the resultat XOR to hexadecimal string
    return xor_result.hex()

if __name__ == "__main__":
    buf1='1c0111001f010100061a024b53535009181c'
    buf2='686974207468652062756c6c277320657965'
    buf1_xor_buf2 = xor_opr(buf1,buf2)
    print(buf1_xor_buf2)
    
    
     
    
