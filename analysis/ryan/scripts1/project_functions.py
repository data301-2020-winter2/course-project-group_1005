import glob
import pandas as pd
import numpy as np

def load_and_process(path):
    frames = []
    for file in glob.glob(path):
        game_id = file[20:-4]
        frame = (
            pd
            .read_csv(file, dtype=object, usecols=[
                "language",
                "review",
                "timestamp_created",
                "timestamp_updated",
                "voted_up",
                "votes_up",
                "votes_funny",
                "weighted_vote_score",
                "comment_count",
                "received_for_free",
                "written_during_early_access",
                "author.num_games_owned",
                "author.num_reviews",
                "author.playtime_forever",
                "author.playtime_last_two_weeks",
                "author.playtime_at_review",
                "author.last_played"
            ])
            .rename(columns={
                "voted_up": "recommended",
                "weighted_vote_score": "steam_algorithm_score",
                "author.num_games_owned": "num_games_owned",
                "author.num_reviews": "num_reviews",
                "author.playtime_forever": "playtime_forever",
                "author.playtime_last_two_weeks": "playtime_last_two_weeks",
                "author.playtime_at_review" : "playtime_at_review",
                "author.last_played": "last_played"
            })
            .assign(game_id=game_id)
        )
        frames.append(frame)
    data = pd.concat(objs=frames)
    return data

# Example:
# data = load_and_process('..\..\data\data_raw\*.csv')
# data