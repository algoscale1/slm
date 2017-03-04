from slm.app.models import session


class GraphDb:

    def __init__(self):
        pass

    @staticmethod
    def get_terms_db(title):
        """

        :param title:
        :return:
        """
        result = session.run("MATCH (:Header{title:"+title+"})<-[:DEFINED_IN]-(Term) RETURN Term.name;")

        terms = []
        for record in result:
              terms.append(record[0])

        return list(set(terms))

    @staticmethod
    def get_headers_db(term):
        """

        :param term:
        :return:
        """

        result = session.run("MATCH (Term{name:"+term+"})--(Header) RETURN Header.title;")

        headers= []
        for record in result:
              headers.append(record[0])

        return list(set(headers))