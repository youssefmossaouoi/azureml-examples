from promptflow import tool

class attrdict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def gen_examples() -> str:
  return [
    attrdict(question="What is 37593 * 67?", code="print(37593 * 67)"), 
    attrdict(question="anet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?", code="print((16-3-4)*2)"),
    attrdict(question="How many of the integers between 0 and 99 inclusive are divisible by 8?", code="print(len([i for i in range(100) if i % 8 == 0]))"),
    attrdict(question="A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?", code="print(2 + 2/2)")
  ]