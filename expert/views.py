from django.shortcuts import render
from django.http import JsonResponse
from .classes import Fact, Rule, InferenceEngine
from .forms import FactForm

def infer_facts(request):
    form = FactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print("Form is valid.")          
            selected_facts = form.cleaned_data['facts']
            facts = {Fact(fact) for fact in selected_facts}

            rules = [
                Rule({Fact('Animal has feathers'), Fact('Animal can fly')}, {Fact('Animal might be a bird')}),
                Rule({Fact('Animal has fur'), Fact('Animal gives live birth')}, {Fact('Animal might be a mammal')}),
                Rule({Fact('Animal has scales'), Fact('Animal lives in water')}, {Fact('Animal might be a fish')}),
                Rule({Fact('Animal has a shell'), Fact('Animal is slow-moving')}, {Fact('Animal might be a tortoise')}),
                Rule({Fact('Animal has long neck'), Fact('Animal has spots')}, {Fact('Animal might be a giraffe')}),
                Rule({Fact('Animal roars'), Fact('Animal has mane')}, {Fact('Animal might be a lion')}),
                Rule({Fact('Animal has stripes'), Fact('Animal is a large cat')}, {Fact('Animal might be a tiger')}),
                Rule({Fact('Animal has a trunk'), Fact('Animal has tusks')}, {Fact('Animal might be an elephant')}),
                Rule({Fact('Animal is small'), Fact('Animal can fly'), Fact('Animal is nocturnal')}, {Fact('Animal might be a bat')}),
                Rule({Fact('Animal hops'), Fact('Animal has a pouch')}, {Fact('Animal might be a kangaroo')}),
            ]
            
            print("Initial facts: ", facts)
            print("Initial rules: ", rules)
            
            print("Starting Inference...") 

            engine = InferenceEngine(rules, facts)
            inferred_facts = engine.forward_chain()
            
            print("Inference finished.")


            inferred_facts_str = [str(fact) for fact in inferred_facts]
            print("Inferred facts:", inferred_facts_str)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'facts': inferred_facts_str}, status=200)
            print({'form': form, 'inferred_facts': inferred_facts_str})
            return render(request, 'expert/se.html', {'form': form, 'inferred_facts': inferred_facts_str})
        else:
            print("Form is not valid.")
            print(form.errors)
    return render(request, 'expert/se.html', {'form': form})



