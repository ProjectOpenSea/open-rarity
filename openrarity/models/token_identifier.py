from dataclasses import dataclass
from typing import Literal, Annotated
from pydantic import Field

@dataclass
class EVMContractTokenIdentifier:
    '''This token is identified by the contract address and token ID number.

    This identifier is based off of the interface as defined by ERC721 and ERC1155, where
    unique tokens belong to the same contract but have their own numeral token id.
    '''
    identifier_type: Literal['evm_contract']
    contract_address: str
    token_id: int

    def __str__(self):
        return f"Contract({self.contract_address}) #{self.token_id}"

@dataclass
class SolanaMintAddressTokenIdentifier:
    '''This token is identified by their solana account address.

    This identifier is based off of the interface defined by the Solana SPL token standard
    where every such token is declared by creating a mint account.
    '''
    identifier_type: Literal['solana_mint_address']
    mint_address: str

    def __str__(self):
        return f"MintAddress({self.mint_address})"

# This is used to specifies how the collection is identified and the
# logic used to group the NFTs together
TokenIdentifier = Annotated[
    (
		EVMContractTokenIdentifier |
		SolanaMintAddressTokenIdentifier
    )
  ,
  Field(discriminator='identifier_type')
]