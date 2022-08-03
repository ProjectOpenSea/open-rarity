import logging

import numpy as np

from open_rarity.models.collection import Collection
from open_rarity.models.token import Token
from open_rarity.scoring.scorer import Scorer
from open_rarity.scoring.utils import get_attr_probs_weights

logger = logging.getLogger("open_rarity_logger")


class ArithmeticMeanRarityScorer(Scorer):
    """arithmetic mean of a token's n trait probabilities"""

    def score_token(self, collection: Collection, token: Token, normalized: bool = True) -> float:
        """Scores the token's rarity

        Parameters
        ----------
        token : Token
            token
        normalized : bool, optional
            apply traits normalization, True by default
        Returns
        -------
        float
            _description_
        """

        logger.debug(f"Computing arithmetic mean for token {token}")

        attr_probs, attr_weights = get_attr_probs_weights(collection, token, normalized)

        return float(np.average(attr_probs, weights=attr_weights))