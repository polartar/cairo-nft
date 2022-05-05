def run(nre):
    # print(“Compiling contract…”)
    nre.compile(["contracts/MyToken.cairo"]) # we compile our contract first
    print("Deploying contract…")
    # name = str(str_to_felt("MyToken"))
    # symbol = str(str_to_felt("MTK"))
    # decimals = "18"
    owner = "0x003d251b15b3b9c61abc0cd534c5d319987ae5b5a6d2b35fe192a5e45e906ad6"
    params = [owner]
    address, abi = nre.deploy("MyToken")
    print(f"ABI: {abi},\nContract address: {address}")
    # 0x00a23a9007bc986de63566fa328cf163ee8a239a91ff944201b9ad3dc1dc5c85 //owner
    # 0x00185f8c2f9d99d93d88ccc1b73deb572207e7f0bb5a76570512520b4266c5f3
# Auxiliary functions
# def str_to_felt(text):
#     b_text = bytes(text, "ascii")
#     return int.from_bytes(b_text, "big")
# def uint(a):
#     return(a, 0)