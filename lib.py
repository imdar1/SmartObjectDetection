import clips

env = clips.Environment()

rule = """
(defrule my-rule
  (ordered-fact 3)
  =>
  (assert (ordered-fact segitiga)))
"""
env.build(rule)

for rule in env.rules():
    print(rule)

# Assert the first ordeded-fact as string so its template can be retrieved
fact_string = "(ordered-fact 3)"
fact = env.assert_string(fact_string)

template = fact.template

assert template.implied == True

new_fact = template.new_fact()
new_fact.extend((3, 4, 5))
new_fact.assertit()

for fact in env.facts():
    print(fact)

print("Result:")
x = env.run()
print(x)

for fact in env.facts():
    print(fact)