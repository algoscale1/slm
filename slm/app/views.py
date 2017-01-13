import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from slm.app.preprocessing import score_calculator
from slm.app.preprocessing import building_tree
from slm.app.tree_structures.act_and_regulations import cbcr, osact, cbcact
from slm.app.tree_structures.forms import form1, form5, form6
from slm.app.tree_structures.manual_and_notices import notice_cbc, notice_tsx, tsx_manual
from slm.app.tree_structures.nis import ni58, ni51, ni54

tree = building_tree.BuildTree()
score = score_calculator.ScoreData()


def main_function(self):
    cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree, ni51_tree, cbcact_tree, \
    ni54_tree, form5_tree, form6_tree, tsx_manual_tree = \
        tree.display_tree(cbcr, osact, form1, ni58, notice_tsx, notice_cbc, ni51, cbcact, ni54, form5, form6,
                               tsx_manual)

    complete_data = score.scoring_tree_data(cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree,
                                                 notice_cbc_tree,
                                                 ni51_tree, cbcact_tree, ni54_tree, form5_tree, form6_tree,
                                                 tsx_manual_tree)

    score.calculate_score_word2vec(complete_data)

    return HttpResponse("done")


@csrf_exempt
def home(request):
    from slm.settings import BASE_DIR,STATICFILES_DIRS
    print(BASE_DIR)
    print(STATICFILES_DIRS)
    return render(request, template_name="searchPage.html")


@csrf_exempt
def hey(request):
    print("post successful")
    question = request.POST['question']
    print(question, "question")
    answers = {"key1": "ans", "key2": "ans2", "key3": "ans3"}
    return HttpResponse(json.dumps(answers))
