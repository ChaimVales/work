from utils.deck import shuffle, create_deck

def create_card(rank:str,suite:str) -> dict:
    card_dict = {"rank":rank,"suite":suite}
    if card_dict["rank"] == "J":
        card_dict["value"] = 11
    elif card_dict["rank"] == "Q":
        card_dict["value"] = 12
    elif card_dict["rank"] == "K":
        card_dict["value"] = 13
    elif card_dict["rank"] == "A":
        card_dict["value"] = 14
    else:
        card_dict["value"] = int(card_dict["rank"])
    return card_dict


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        "WAR"




