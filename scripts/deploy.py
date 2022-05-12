def run(nre):
    # print(“Compiling contract…”)
    nre.compile(["contracts/MyToken.cairo"]) # we compile our contract first
    print("Deploying contract…")
    # name = str(str_to_felt("MyToken"))
    # symbol = str(str_to_felt("MTK"))
    # decimals = "18"
    owner = "0x0511c34a48146c49a341d1405b01bd4f5ad09af0ae9db45a6e40711cc529fc7a"
    params = [owner]
    address, abi = nre.deploy("MyToken")
    print(f"ABI: {abi},\nContract address: {address}")
    # 0x00a23a9007bc986de63566fa328cf163ee8a239a91ff944201b9ad3dc1dc5c85 //owner
    # 0x00185f8c2f9d99d93d88ccc1b73deb572207e7f0bb5a76570512520b4266c5f3
    # 0x0055e1a6d333950afe8efec26011df3d5552fc535f235b76f254710c34116a94
# Auxiliary functions
# def str_to_felt(text):
#     b_text = bytes(text, "ascii")
#     return int.from_bytes(b_text, "big")
# def uint(a):
#     return(a, 0)