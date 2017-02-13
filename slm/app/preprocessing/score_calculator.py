import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from gensim import matutils, corpora
from gensim.models import TfidfModel
from gensim.models.phrases import Phrases
from scipy import spatial
from nltk import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from gensim.models.word2vec import Word2Vec
from nltk.corpus import wordnet as wn
import os


class ScoreData:
#This is a class for scoring data
    def __init__(self):
        self.stopwords = stopwords.words('english')
        # Lemmatizer
        self.lmtzr = WordNetLemmatizer()
        # Stemmer
        self.stemmer = PorterStemmer()
        self.word2vec_model = None
        self.words = re.compile(r"\w+", re.I)
        try:
            self.bigrams = Phrases.load('slm/app/cached_models/bigrams.gensim')
        except:
            self.bigrams = None
        try:
            self.trigrams = Phrases.load('slm/app/cached_models/trigrams.gensim')
        except:
            self.trigrams = None
        try:
            self.dictionary = corpora.Dictionary.load('slm/app/cached_models/dictionary.dict')
        except:
            self.dictionary = None
        try:
            self.tfidf = TfidfModel.load('slm/app/cached_models/tfidf.gensim')
        except:
            self.tfidf = None

    def init(self):
        # Google Word2Vec Corpus Loaded
        self.word2vec_model = Word2Vec.load_word2vec_format('slm/app/cached_models/google.bin',binary=True)

    def calculate_score_word2vec(self,df,requested_question):
        """
        To calculate score according to Word2Vec model
        :param df: complete Dataframe
        :param requested_question: Input question requested by the user
        :return: dataframe after adding TF-IDF scores
        """
        if self.word2vec_model is None:
            self.init()
        sent_tokens = self.data_parser_pos_tagging(requested_question)
        req_question_vectorized = self.create_avg_sentence_vector(sent_tokens)
        score1 = []
        for i, datapoint in df.iterrows():
            pos_tags_all = self.data_parser_pos_tagging(datapoint.topic_information)
            pos_tags = self.data_parser_pos_tagging(datapoint.topic.lower())
            topic_keywords = self.generate_tokens(datapoint.topic.lower())
            data_vectorized1 = self.create_avg_sentence_vector(pos_tags_all + pos_tags)
            similarity1 = self.get_vec_similarity(data_vectorized1, req_question_vectorized)
            keyword_similarity = self.get_common_tokens(sent_tokens, topic_keywords)
            score1.append(similarity1 + (keyword_similarity / 50))

        df["score_w2v"] = score1
        df = df.sort_values(by=["score_w2v"], ascending=False)
        # Setting Threshold as 0.4 on word2vec results
        df = df.loc[df.score_w2v > 0.40]
        df = self.tfidf_scoring(df,requested_question)
        df["score"] = df["score_w2v"] + df["score_tfidf"]
        # Setting overall threshold as 0.55 after combining both the scores
        df = df.loc[df.score > 0.55]
        df.drop(['score_w2v', 'score_tfidf'], axis=1, inplace=True)
        df = df.sort_values(by=["score"], ascending=False)
        df.reset_index(inplace=True, drop=True)
        return df

    def tfidf_scoring(self,df,requested_question):
        """
        To calculate score according to TF-IDF model
        :param df: Dataframe received from word2vec model
        :param requested_question: Input question requested by the user
        :return: dataframe after adding TF-IDF scores
        """
        req_question_tokenized = [self.create_preprocessed_tokens(requested_question)]
        req_question_vectorized = self.vectorize(req_question_tokenized)
        score2 = []
        for i, datapoint in df.iterrows():
            data_tokenized2 = [self.create_preprocessed_tokens(datapoint.topic_information)]
            data_vectorized2 = self.vectorize(data_tokenized2)
            similarity2 = self.get_vec_similarity(data_vectorized2, req_question_vectorized)
            score2.append(similarity2)
        df["score_tfidf"] = score2
        df = df.sort_values(by=["score_tfidf"], ascending=False)
        df = df.loc[df.score_tfidf > 0.00]
        df = df.sort_values(by=["topic"], ascending=False)
        df.reset_index(inplace=True, drop=True)
        return df


    def converting_trees_to_df(self,cbcr_tree,osact_tree,form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree,
                                     ni51_tree,cbcact_tree,ni54_tree,form5_tree,form6_tree,tsx_manual_tree):
        """
        Function to convert all trees into dataframes
        :param cbcr_tree: Canada Business Corporations Regulations tree
        :param osact_tree: Ontario Securities Act tree
        :param form1_tree: Form 58-101F1 Corporate Governance Disclosure tree
        :param ni58_tree: National Instrument 58-101 Disclosure of Corporate Governance Practices tree
        :param notice_tsx_tree: TSX Staff Notice 2015-0002 (September 10, 2015) - Subsections 461.1-461.4 and Section 464 Director Elections and Annual Meetings tree
        :param notice_cbc_tree: Notice concerning notice-and-access regime recently adopted by the Canadian Securities Administrators tree
        :param ni51_tree: National Instrument 51-102 Continuous Disclosure Obligations tree
        :param cbcact_tree: Canada Business Corporations Act tree
        :param ni54_tree: National Instrument 54-101 Communication with Beneficial Owners of Securities of a Reporting Issuer tree
        :param form5_tree: Form 51-102F5 Information Circular tree
        :param form6_tree: Form 51-102F6 Statement of Executive Compensation tree
        :param tsx_manual_tree: TSX Company Manual tree
        :return: concatenated complete dataframe
        """
        all_trees = [cbcr_tree,osact_tree,form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree,
                                     ni51_tree,cbcact_tree,ni54_tree,form5_tree,form6_tree,tsx_manual_tree]
        tokenized_trees = [self.create_preprocessed_tokens(node) for tree in all_trees for node in tree]
        #Training ngrams and tfidf model
        self.train_ngrams_models(tokenized_trees)

        cbcr_df = pd.DataFrame({'topic' : cbcr_tree[0],'topic_information':cbcr_tree})
        cbcr_df = self.standarize_df(cbcr_df)
        osact_df = pd.DataFrame({'topic': osact_tree[0],'topic_information': osact_tree})
        osact_df = self.standarize_df(osact_df)
        form1_df = pd.DataFrame({'topic': form1_tree[0],'topic_information': form1_tree})
        form1_df = self.standarize_df(form1_df)
        ni58_df = pd.DataFrame({'topic': ni58_tree[0],'topic_information': ni58_tree})
        ni58_df = self.standarize_df(ni58_df)
        notice_tsx_df = pd.DataFrame({'topic': notice_tsx_tree[0],'topic_information': notice_tsx_tree})
        notice_tsx_df = self.standarize_df(notice_tsx_df)
        notice_cbc_df = pd.DataFrame({'topic': notice_cbc_tree[0],'topic_information': notice_cbc_tree})
        notice_cbc_df = self.standarize_df(notice_cbc_df)
        ni51_df = pd.DataFrame({'topic': ni51_tree[0],'topic_information': ni51_tree})
        ni51_df = self.standarize_df(ni51_df)
        cbcact_df = pd.DataFrame({'topic': cbcact_tree[0],'topic_information': cbcact_tree})
        cbcact_df = self.standarize_df(cbcact_df)
        ni54_df = pd.DataFrame({'topic': ni54_tree[0],'topic_information': ni54_tree})
        ni54_df = self.standarize_df(ni54_df)
        form5_df = pd.DataFrame({'topic': form5_tree[0], 'topic_information': form5_tree})
        form5_df = self.standarize_df(form5_df)
        form6_df = pd.DataFrame({'topic': form6_tree[0], 'topic_information': form6_tree})
        form6_df = self.standarize_df(form6_df)
        tsx_manual_df = pd.DataFrame({'topic': tsx_manual_tree[0], 'topic_information': tsx_manual_tree})
        tsx_manual_df = self.standarize_df(tsx_manual_df)

        complete_df = pd.concat([ni51_df,ni54_df,ni58_df,osact_df,cbcact_df,cbcr_df,form1_df,form5_df,form6_df,notice_cbc_df,notice_tsx_df,tsx_manual_df],axis = 0)
        return complete_df

    def standarize_df(self,df):
        """
        Standardize the dataframe
        :param df: input dataframe
        :return: dataframe in standardized format
        """
        df.drop(df.index[[0]],inplace= True)
        df.reset_index(drop= True,inplace= True)
        return df

    def create_avg_sentence_vector(self, words):
        """
        Create vector from word2vec model by sentence average method
        :param words: input requested question in the form of list
        :return: sentence vector in the form of array
        """
        sent_vector = np.zeros(self.word2vec_model.vector_size, )
        number_of_words = 0

        for word in words:
            if word in self.word2vec_model:
                number_of_words += 1
                sent_vector = np.add(sent_vector, self.word2vec_model[word])
        if number_of_words > 0:
            sent_vector = np.divide(sent_vector, number_of_words)
        return sent_vector

    def create_preprocessed_tokens(self,raw_sentence):
        """
        tokenize sentence for tf-idf model
        :param raw_sentence: raw_sentence in the form of string
        :return: tokenize sentence in list form
        """
        tokens = [self.lmtzr.lemmatize(word.lower()) for word in re.findall(self.words, raw_sentence)
                  if word.lower() not in self.stopwords]
        tokens = [self.stemmer.stem(word) for word in tokens if len(word) > 2]
        return tokens

    def generate_tokens(self, raw_sentence):
        """
        tokenize sentence into words
        :param raw_sentence: raw sentence in the  form of string
        :return: tokenized sentence in list form
        """
        tokens = [word.lower() for word in re.findall(self.words, raw_sentence) if
                  word.lower() not in self.stopwords]
        return tokens


    def train_ngrams_models(self,sent_tokens):
        """
        Train bigrams,trigrams and dictionary and save them in cached models
        :param sent_tokens: concatenated overall complete dataframe
        """
        bigrams = Phrases(sentences=sent_tokens, min_count=1, threshold=1)
        trigrams = Phrases(sentences=bigrams[sent_tokens], min_count=1, threshold=1)
        sent_tokens_transformed = trigrams[bigrams[sent_tokens]]
        d = corpora.Dictionary(sent_tokens_transformed)
        bow_corpus = [d.doc2bow(sent_tokens) for sent_tokens in sent_tokens_transformed]
        tfidf = TfidfModel(corpus=bow_corpus, id2word=d)
        try:
            bigrams.save('slm/app/cached_models/bigrams.gensim')
            trigrams.save('slm/app/cached_models/trigrams.gensim')
            d.save('slm/app/cached_models/dictionary.dict')
            tfidf.save('slm/app/cached_models/tfidf.gensim')
        except:
            pass

    def vectorize(self,sent_token):
        """
        Function to vectorize the data
        :param sent_token: input tokenized data
        :return: list of BOW (Bag of Words) transformed corpus
        """
        sent_token = self.trigrams[self.bigrams[sent_token]]
        sent_vector = [self.dictionary.doc2bow(token) for token in sent_token]
        sent_vector = self.tfidf[sent_vector]
        sent_vector = matutils.corpus2dense(sent_vector, num_terms=len(self.dictionary.values()))
        return sent_vector.transpose()

    def get_vec_similarity(self, v1, v2):
        """
        calculates vectors similarity
        :param v1: vector
        :param v2: vector
        :return: a float value which represents similarity
        """
        if len(np.nonzero(v1)[0]) == 0 or len(np.nonzero(v2)[0]) == 0:
            sim = 0.0
        else:
            sim = 1 - spatial.distance.cosine(v1, v2)
        return sim

    def data_parser_pos_tagging(self, sentences):
        """
        Parse data for Parts-Of-Speech
        :param sentences: sentence in the form of string
        :return: POS tags list of the input
        """
        pos_noun_tags= []
        sentences_tokenized = sent_tokenize(sentences)
        for sentence in sentences_tokenized:
            sentence_tokenized = word_tokenize(sentence.lower())
            pos_noun_tags = self.pos_tagging(sentence_tokenized, pos_noun_tags)
            pos_noun_tags = [tags for tags in pos_noun_tags if len(tags) > 2]
        return pos_noun_tags

    def pos_tagging(self, sentence, pos_noun_tags):
        """
        To POS tag sentence for nouns
        :param sentence: input sentence
        :param pos_noun_tags: Noun tag list
        :return: List of Nouns from current sentence
        """
        for word, pos in pos_tag(sentence):
            if pos in ['NN', "NNP", "NNS"]:
                pos_noun_tags.append(word)
        return pos_noun_tags

    def get_common_tokens(self, list1, list2):
        """
        calculates intersection of two list of words
        :param list1: list of words
        :param list2: list of words
        :return: length of common words
        """
        list2 = [word for word in list2]
        l1 = []
        l2 = []
        for word in list1:
            l1.append(word)
        for word in list2:
            l2.append(word)
        sim = len(set(l1).intersection(l2))
        return sim

