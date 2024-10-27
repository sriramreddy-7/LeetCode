import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    a,b=players.shape
    return [a,b]