import requests
def prompts(name, description):
    def decorator(func):
        func.name = name
        func.description = description
        return func

    return decorator

# 方法统一为 get_nft 内容
class NFT_info:
    def __init__(self, device):
        print(f"Using NFT_info_api to {device}")
        self.api_key = "434cacfe-adc9-4d35-974a-79bc06905319"

    # 获取address信息
    @prompts(name="Get nft collection_address by name",
             description="useful when you want to learn about collection_address through providing its name."
                         "from its its collection name"
                         "The input to this tool should be a collection name separated by spaces,like Bored Ape Yacht Club"
                         "representing the collection name")
    def get_nft_collection_address_by_name(self, inputs):
        # contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
        # # return self.inference_replace(f"{image_path},{to_be_removed_txt},background")
        keywords=inputs.replace("","%20")
        url = f"https://data-api.nftgo.io/eth/v1/collection/name/{keywords}"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        collections = response.json()['collections']
        collection = collections[0]
        contracts = collection['contracts']
        return contracts
    # 获取基本信息
    @prompts(name="Get an NFT by contract",
             description="useful when you want to learn about nft information through contract_address"
                         "from its description or location. "
                         "The input to this tool should be a comma separated string of two, "
                         "representing the contract_address and the token_id need to be removed. ")
    def get_nft_by_contract(self, inputs):
        contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
        # return self.inference_replace(f"{image_path},{to_be_removed_txt},background")
        url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/info"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.text
    # 获取交易数据
    @prompts(name="Get NFT Metrics",
             description="useful when you want to know about nft metrics like last_price,avg_price_usd through contract address "
                         " This function sends a GET request to the NFT metrics API to retrieve metrics about an NFT with the given contract address and token ID."
                         "The input to this tool should be a comma separated string of two "
                         "representing the contract address of the NFT to retrieve metrics for, The token ID of the NFT to retrieve metrics for ")
    def get_nft_metrics(self,inputs):
        contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
        url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/metrics"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.text
    # 评估稀缺性
    @prompts(name="Get NFT Rarity",
             description="useful when you want to know about nft Rarity through contract address "
                         " This function sends a GET request to the NFT metrics API to retrieve metrics about an NFT with the given contract address and token ID."
                         "The input to this tool should be a comma separated string of two, "
                         "representing the contract address of the NFT to retrieve metrics for, The token ID of the NFT to retrieve metrics for ")
    def get_nft_rarity(self,inputs):
        contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
        url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/metrics"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.text

    # 获取市场概况
    @prompts(name="Get Market Rarity",
             description="useful when you want to know about nft market"
                         " This function sends a GET request to the NFT metrics API to Retrieve various metrics related to the overall NFT market, such as volume, price trends, etc."
                         "The input to this tool The input to this tool should be a comma separated string of two "
                         "representing the contract address of the NFT to retrieve metrics for, The token ID of the NFT to retrieve metrics for ")
    def Get_Market_metric(self,inputs=None):
        url = "https://data-api.nftgo.io/eth/v1/market/metrics"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)

        print(response.text)


class Collection:
    def __init__(self, device):
        print(f"Using NFT_info_api to {device}")
        self.api_key = "434cacfe-adc9-4d35-974a-79bc06905319"
        # 获取address信息
    @prompts(name="Get address's portfolio",
             description="useful when you want to learn about Retrieve the portfolio of an address, including all NFTs owned."
                         "from its its address name"
                         "The input to this tool should be a Ethereum address, 42-character hexadecimal string beginning with 0x "
                         "representing the collection name")
    def Get_address_portfolio(self, inputs):
        # contract_address, token_id = inputs.split(",")[0], ','.join(inputs.split(',')[1:])
        # # return self.inference_replace(f"{image_path},{to_be_removed_txt},background")

        url = f"https://data-api.nftgo.io/eth/v1/address/{inputs}/collection?offset=0&limit=1"

        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)

        return response

    @prompts(name="Get address's portfolio",
             description="useful when you want to learn about Retrieve the portfolio of an address, including all NFTs owned."
                         "from its its address name"
                         "The input to this tool should be a Ethereum address, 42-character hexadecimal string beginning with 0x "
                         "representing the collection name")
    def get_address_collection(self,address):
        """
        This function sends a GET request to the NFT collection API to retrieve a list of NFT collections owned by the given address.
        Args:
            address (str): The Ethereum address to retrieve the NFT collections for.
        Returns:
            str: A string containing the JSON-formatted response from the API, which includes a list of the NFT collections owned by
            the address.
        """
        url = f"https://data-api.nftgo.io/eth/v1/address/{address}/collection"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.text

    @prompts(name="Get address's metrics",
             description="Retrieve all key metrics related to a specific address, such as the number of NFTs owned,etc."
                         "from its its address name"
                         "The input to this tool should be a Ethereum address, 42-character hexadecimal string beginning with 0x "
                         "representing the collection name")
    def get_address_metrics(self,address):
        """
        This function sends a GET request to the NFT address metrics API to retrieve metrics about an Ethereum address.

        Args:
            address (str): The Ethereum address to retrieve metrics for.

        Returns:
            str: A string containing the JSON-formatted response from the API, which includes metrics for the address.
        """
        url = f"https://data-api.nftgo.io/eth/v2/address/metrics?address={address}"
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        return response.text

class History:

    def get_collection_transactions(contract_address, action='all', start_time=None, end_time=None, offset=0, limit=20,
                                    asc=False, exclude_wash_trading=False):
        """
        This function sends a GET request to the NFT collection transaction history API to retrieve a list of transaction history
        for a specific NFT collection.

        Args:
            contract_address (str): Address of the contract for this NFT collection, beginning with 0x.
            action (str, optional): The type of transactions. Can be 'all', 'buy', 'sell', 'transfer', or 'burn'.
                Default is 'all'.
            start_time (str, optional): Queries can be bounded by a Start Time and End Time.
            Start Time is the earliest timestamp to include in the transaction query, formatted as an UTC timestampin seconds or ISO 8601
            format date time string, such as 2022-08-20T00:00:00+00:00. Start Time limited to 2021-09-01T00:00:00+00:00 or later.
            end_time (str, optional): Where an End Time is specified, transaction queries will fetch all transactions up to but excluding the End Time,
            which is formatted as an UTC timestamp in seconds or ISO 8601 format date time string.
            The query window varies according to the plan.
            offset (int, optional): The index of data segments. The returned data is divided into many segments.
             One segment is returned at a time. {offset} parameter indicates the index of data segments.
            limit (int, optional): The size of a returned data segment
            asc (bool, optional): Whether to sort results in ascending order
            exclude_wash_trading (bool, optional): Whether excluding wash trading transactions

        Returns:
            str: A string containing the JSON-formatted response from the API, which includes a list of transaction history
            for the NFT collection.
        """
        url = f"https://data-api.nftgo.io/eth/v1/history/collection/{contract_address}/transactions?action={action}"
        if start_time:
            url += f"&start_time={start_time}"
        if end_time:
            url += f"&end_time={end_time}"
        url += f"&offset={offset}&limit={limit}&asc={asc}&exclude_wash_trading={exclude_wash_trading}"
        headers = {
            "accept": "application/json",
            # "X-API-KEY": X_API_KEY
        }
        response = requests.get(url, headers=headers)
        return response.text

    def get_nft_transactions(contract_address, token_id, action='all', scroll=None, scroll_limit=10):
        """
        This function sends a GET request to the NFT transaction history API to retrieve a list of transaction history
        for a specific NFT.

        Args:
            contract_address (str): Address of the contract for this NFT collection, beginning with 0x
            token_id (integer): The token ID for this NFT. Each item in an NFT collection will be assigned a unique id,
             the value generally ranges from 0 to N, with N being the total number of NFTs in a collection..
            action (str, optional): The type of transactions.
            scroll (int, optional):Timestamp in second. {scroll_limit} transactions occurring earlier than {scroll} will be returned. Default value is current time..
            scroll_limit (int, optional): The maximum number of transactions to return in each page when using scroll.
                Default is 10.

        Returns:
            str: A string containing the JSON-formatted response from the API, which includes a list of transaction history
            for the NFT.
        """
        url = f"https://data-api.nftgo.io/eth/v1/history/nft/transactions?contract_address={contract_address}&token_id={token_id}&action={action}"
        if scroll:
            url += f"&scroll={scroll}&scroll_limit={scroll_limit}"
        headers = {
            "accept": "application/json",
            # "X-API-KEY": X_API_KEY
        }
        response = requests.get(url, headers=headers)
        return response.text

