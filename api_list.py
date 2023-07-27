import requests
X_API_KEY = "434cacfe-adc9-4d35-974a-79bc06905319"
## NFT
def get_nft_info(contract_address, token_id):
    """
    This function sends a GET request to the NFT information API to retrieve information about an NFT with the given
    contract address and token ID.
    Args:
        contract_address (str): The contract address of the NFT to retrieve information for.Address of the contract for this NFT collection, beginning with 0x
        token_id (str): The token ID of the NFT to retrieve information for.The token ID for this NFT. Each item in an NFT collection will be assigned a unique id, the value generally ranges from 0 to N, with N being the total number of NFTs in a collection.

    Returns:
        str: A string containing the JSON-formatted response from the API, which includes information about the NFT.
    """
    url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/info"
    headers = {
    "accept": "application/json",
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text

def get_nft_metrics(contract_address, token_id):
    """
    This function sends a GET request to the NFT metrics API to retrieve metrics about an NFT with the given
    contract address and token ID.
    Args:
        contract_address (str): The contract address of the NFT to retrieve metrics for.
        token_id (str): The token ID of the NFT to retrieve metrics for.

    Returns:
        str: A string containing the JSON-formatted response from the API, which includes metrics for the NFT.
    """
    url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/metrics"
    headers = {
    "accept": "application/json",
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text


def get_nft_rarity(contract_address, token_id):
    """
    This function sends a GET request to the NFT rarity API to retrieve the rarity score and percentile for an NFT
    with the given contract address and token ID.

    Args:
        contract_address (str): The contract address of the NFT to retrieve rarity information for.
        token_id (str): The token ID of the NFT to retrieve rarity information for.

    Returns:
        str: A string containing the JSON-formatted response from the API, which includes the rarity score and
        percentile for the NFT.
    """
    url = f"https://data-api.nftgo.io/eth/v1/nft/{contract_address}/{token_id}/rarity"
    headers = {
    "accept": "application/json",
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text

## Address
def get_address_portfolio(address, offset=0, limit=20):
    """
    This function sends a GET request to the NFT portfolio API to retrieve a list of NFTs owned by the given address.

    Args:
        address (str): The Ethereum address to retrieve the NFT portfolio for.
        offset (int, optional): The index of data segments. The returned data is divided into many segments. One segment is returned at a time. {offset} parameter indicates the index of data segments.
        limit (int, optional): The size of a returned data segment. Default is 20.

    Returns:
        str: A string containing the JSON-formatted response from the API, which includes a list of the NFTs owned by
        the address.
    """
    url = f"https://data-api.nftgo.io/eth/v1/address/{address}/portfolio?offset={offset}&limit={limit}"
    headers = {
    "accept": "application/json",
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text


def get_address_collection(address):
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
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text


def get_address_metrics(address):
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
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text

## History

def get_collection_transactions(contract_address, action='all', start_time=None, end_time=None, offset=0, limit=20, asc=False, exclude_wash_trading=False):
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
    "X-API-KEY": X_API_KEY
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
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text


def get_address_transactions(contract_address, token_id, action='all', scroll=None, scroll_limit=10):
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
    '''
'https://data-api.nftgo.io/eth/v1/history/address/0xcaf1d788c67BdAAC155E7dcC4D64e2004eF651D4/activities?action=all&scroll=1661007946&exclude_wash_trading=false&contract_address=all' \

    '''
    # todo:将scroll自动转换成当前的时间戳
    url = f"https://data-api.nftgo.io/eth/v1/history/address/{contract_address}/activities?action=all&scroll=1661007946&exclude_wash_trading=false&contract_address=all"
    if scroll:
        url += f"&scroll={scroll}&scroll_limit={scroll_limit}"
    headers = {
    "accept": "application/json",
    "X-API-KEY": X_API_KEY
}
    response = requests.get(url, headers=headers)
    return response.text

## 市场
def Get_Market_metrics():
    "检索与整个 NFT 市场相关的各种指标，如数量、价格趋势等，以查看标准"
    """
    Retrieve various metrics related to the overall NFT market, such as volume, price trends, etc.here to see the criteria
    """
    url = "https://data-api.nftgo.io/eth/v1/market/metrics"
    headers = {
        "accept": "application/json",
        "X-API-KEY": X_API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.text

def Get_collection_ranking():
    """
    根据不同的因素(如数量、价格等)检索特定集合的排名，
    :return:
    """
    pass


## collection
