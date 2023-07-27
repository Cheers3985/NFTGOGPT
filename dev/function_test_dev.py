import requests
from langchain.tools import tool

# Get an NFT by contract
# Get NFT metrics
# Get rarity of an NFT

# info metrics rarity
# 构建结构化函数
def get_nft_by_contract(address="",token_id="",message=""):
    # contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
    # return self.inference_replace(f"{image_path},{to_be_removed_txt},background")
    url = f"https://data-api.nftgo.io/eth/v1/nft/{address}/{token_id}/{message}"
    headers = {
        "accept": "application/json",
        "X-API-KEY": "434cacfe-adc9-4d35-974a-79bc06905319"
    }
    response = requests.get(url, headers=headers)
    return response.text