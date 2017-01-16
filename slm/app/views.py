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


@csrf_exempt
def get_answers(request):
    """
    this function returns answers and linked to url `slm/answers/`
    :param request: http request which contains the requested question
    :return: dictionary of answers
    """
    requested_question = request.POST['question']

    cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree, ni51_tree, cbcact_tree, \
    ni54_tree, form5_tree, form6_tree, tsx_manual_tree = \
        tree.display_tree(cbcr, osact, form1, ni58, notice_tsx, notice_cbc, ni51, cbcact, ni54, form5, form6,
                          tsx_manual)

    complete_data = score.scoring_tree_data(cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree,
                                            notice_cbc_tree,
                                            ni51_tree, cbcact_tree, ni54_tree, form5_tree, form6_tree,
                                            tsx_manual_tree)

    # filtering answers on the basis of scores using word2vec model
    answers_df = score.calculate_score_word2vec(complete_data, requested_question)

    # converting df datapoints to a dictionary
    headings = answers_df.topic.values.tolist()
    answers = answers_df.topic_information.values.tolist()
    scores = answers_df.score.values.tolist()

    heading_with_answers = {}
    for heading, answer in zip(headings, answers):
        heading_with_answers[heading] = answer
    # print(heading_with_answers)
    return HttpResponse(json.dumps(heading_with_answers))

@csrf_exempt
def home(request):
    """
    returns home page for quering questions
    :param request:
    :return:
    """
    return render(request, template_name="searchPage.html")

