class InferenceEngine:
     def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

     def forward_chain(self):
        while True:
            new_facts = set()
            triggered_rules = []

            for rule in self.rules:
                if rule.is_triggered(self.facts):
                    print(f"Rule triggered: {rule}")
                    triggered_rules.append(rule)
                    
            if not triggered_rules:
                print('no rules triggered')
                break
            for rule in triggered_rules:
                print(f"Removing rule: {rule}")
                self.rules.remove(rule)
            if triggered_rules:  
                rule_with_longest_antecedent = max(triggered_rules, key=lambda r: len(r.antecedent))
                print(f"Rule with longest antecedent: {rule_with_longest_antecedent}")
                new_facts |= rule_with_longest_antecedent.consequent
                self.facts = new_facts
        return self.facts


class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent
    
    def is_triggered(self, facts):
        return self.antecedent.issubset(facts)
    def __repr__(self):
        return f"Rule({self.antecedent}, {self.consequent})"

class Fact:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Fact):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
    def __repr__(self):
         return f"Fact('{self.name}')"    
