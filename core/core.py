import clips
import copy 

class Core:
    def __init__(self, filename):    
        self.env = clips.Environment()
        self.env.load(filename)

    def assert_fact(self, fact):
        self.env.assert_string(fact)

    def get_activations(self):
        return list(self.env.activations())

    def get_hit_rules(self):
        count = len(list(self.env.activations()))
        rules = []
        while (count>0):
            for activation in self.env.activations():
                rules.append(activation.name)
            self.env.run(limit=1)
            count = len(list(self.env.activations()))
        return rules

    def get_matched_facts(self):
        return self.facts
    
    def get_results(self):
        self.facts = []
        for fact in self.env.facts():
            self.facts.append(str(fact))
        return self.facts[len(list(self.env.facts()))-1]
