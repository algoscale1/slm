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
from slm.app.models import Header, Term
import csv
import pandas as pd

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

    # construction of trees from data
    cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree, ni51_tree, cbcact_tree, \
    ni54_tree, form5_tree, form6_tree, tsx_manual_tree = \
        tree.display_tree(cbcr, osact, form1, ni58, notice_tsx, notice_cbc, ni51, cbcact, ni54, form5, form6,
                          tsx_manual)

    # Converting trees to data frame
    complete_data = score.converting_trees_to_df(cbcr_tree, osact_tree, form1_tree, ni58_tree, notice_tsx_tree,
                                            notice_cbc_tree,
                                            ni51_tree, cbcact_tree, ni54_tree, form5_tree, form6_tree,
                                            tsx_manual_tree)

    # filtering answers on the basis of scores using word2vec model
    answers_df = score.calculate_score_word2vec(complete_data, requested_question)
    # converting df data points to a dictionary
    headings = answers_df.topic.values.tolist()
    answers = answers_df.topic_information.values.tolist()
    heading_with_answers = {"headings": headings, "answers": answers}
    if len(headings) == 0:
        return HttpResponse("no results found")
    else:
        return HttpResponse(json.dumps(heading_with_answers))


@csrf_exempt
def home(request):
    """
    returns home page for querying questions
    :param request:
    :return:
    """
    return render(request, template_name="searchPage.html")


@csrf_exempt
def db(request):

    df = pd.read_csv('/home/ubuntu/def.csv')
    for index,row in df.iterrows():

        executive_officer = Term(name=row['definition term']).save()
        continuous_disclosure = Header(title=row['heading']).save()
        executive_officer.header.connect(continuous_disclosure)
    return HttpResponse("done")

from .models import session


@csrf_exempt
def get_terms(request):
    if request.method =='POST':
        title = json.loads(request.body.decode("utf-8"))['title']
        # title = "'National Instrument 51-102 Continuous Disclosure Obligations'"
        result = session.run("MATCH (:Header{title:"+title+"})<-[:DEFINED_IN]-(Term) RETURN Term.name;")

        terms = []
        for record in result:
              terms.append(record[0])

        session.close()
        results = {"terms": terms}
        return HttpResponse(json.dumps(results))


@csrf_exempt
def get_headers(request):
    if request.method =='POST':
        term  = json.loads(request.body.decode("utf-8"))['term']
        term = "'form of proxy'"
        result = session.run("MATCH (Term{name:"+term+"})--(Header) RETURN Header.title;")

        headers= []
        for record in result:
              headers.append(record[0])

        session.close()
        results = {"headers": headers}
        return HttpResponse(json.dumps(results))