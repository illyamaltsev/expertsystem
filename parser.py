

# parser
def parse(tokens):
    true_facts = []
    question_facts = []
    rules = []
    i = 0
    while i < len(tokens):
        k, v = tokens[i]
        if k is "true_facts":
            while k is not "\n" and i < len(tokens):
                k, v = tokens[i]
                if k is "fact":
                    true_facts.append(v)
                i = i + 1
        elif k is "question_facts":
            while k is not "\n" and i < len(tokens):
                k, v = tokens[i]
                if k is "fact":
                    question_facts.append(v)
                i = i + 1
        elif k is "fact":
            rule = {
                "all": "",
                "arr": []
            }
            while k is not "\n" and i < len(tokens):
                rule["all"] = rule["all"] + " " + v
                rule["arr"].append(tokens[i])
                i = i + 1
                k, v = tokens[i]
            rule["all"] = rule["all"][1:]
            rules.append(rule)
        elif k is "\n":
            i = i + 1
    return true_facts, question_facts, rules
