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
    def __init__(self):
        self.stopwords = stopwords.words('english')
        self.lmtzr = WordNetLemmatizer()
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
        # self.word2vec_model = Word2Vec.load('slm/app/cached_models/word2vec_model.gensim')
        self.word2vec_model = Word2Vec.load_word2vec_format('app/cached_models/google.bin',binary=True)

    def extracting_definitions(self,df,requested_question):
        req_tokens = [self.generate_tokens(requested_question)]
        req_question_vectorized = self.vectorize(req_tokens)
        for tokens in req_tokens:
            word = '|'.join(tokens)
            df1 = df.loc[df['terms'].str.contains(word)]

        score3 = []
        for i, datapoint in df1.iterrows():
            data_tokenized3 = [self.generate_tokens(datapoint.topic_information)]
            data_vectorized3 = self.vectorize(data_tokenized3)
            similarity3 = self.get_vec_similarity(data_vectorized3, req_question_vectorized)
            score3.append(similarity3)

        df1["score"] = score3
        df1 = df1.sort_values(by=["score"], ascending=False)
        df1.reset_index(inplace=True, drop=True)
        df1 = df1[['topic', 'topic_information','score']]
        return df1


    def calculate_score_word2vec(self,df,requested_question):
       if self.word2vec_model is None:
           self.init()
       # Requested input question from sample dataset
       # requested_question = "Is shareholder consent needed for notice and access?"
       # requested_question = "Does a circular have to say the debt that a director owes to the company?"
       # requested_question = "When does a meeting have to be held?"
       # requested_question = "Do meeting results have to be disclosed?"
       # requested_question = "What information is required about fees paid to a compensation expert?"
       definition_df = self.extracting_definitions(df,requested_question)

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
       df = df.loc[df.score_w2v > 0.40]
       df = self.tfidf_scoring(df,requested_question)
       df["score"] = df["score_w2v"] + df["score_tfidf"]
       df = df.loc[df.score > 0.55]
       df.drop(['score_w2v', 'score_tfidf'], axis=1, inplace=True)
       df = df.sort_values(by=["score"], ascending=False)
       df.reset_index(inplace=True, drop=True)
       final_df = pd.concat([definition_df, df])
       final_df.drop_duplicates(subset=['topic_information'], keep='first', inplace=True)
       final_df.reset_index(inplace=True, drop=True)
       # final_df.to_csv("/home/algo/Desktop/old_ques3.csv")
       return df

    def tfidf_scoring(self,df,requested_question):
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
       # dict = {k: g["topic_information"].tolist() for k, g in df.groupby("topic")}
       return df


    def scoring_tree_data(self,cbcr_tree,osact_tree,form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree,
                                     ni51_tree,cbcact_tree,ni54_tree,form5_tree,form6_tree,tsx_manual_tree):
        all_trees = [cbcr_tree,osact_tree,form1_tree, ni58_tree, notice_tsx_tree, notice_cbc_tree,
                                     ni51_tree,cbcact_tree,ni54_tree,form5_tree,form6_tree,tsx_manual_tree]
        tokenized_trees = [self.create_preprocessed_tokens(node) for tree in all_trees for node in tree]
        #Training ngrams and tfidf model
        self.train_ngrams_models(tokenized_trees)
        # self.train_word2vec_model(tokenized_trees)

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
        complete_df_with_def_terms = self.adding_definition_terms(complete_df)

        return complete_df_with_def_terms

    def adding_definition_terms(self,df):
        terms = []
        for row in df.topic_information:
            t = row.split("means", 1)[0]
            t = self.extract_terms_between_quotes(t)
            terms.append(t)
        df['terms'] = terms
        df['terms'] = df['terms'].str.replace(r'[^\w\s]', ' ')
        return df


    def standarize_df(self,df):
        df.drop(df.index[[0]],inplace= True)
        df.reset_index(drop= True,inplace= True)
        return df

    def create_avg_sentence_vector(self, words):
        """
        Create vector from word2vec model by sentence average method
        :param words: input requested question in the form of list
        :param model: word2vec model
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
        tokens = [self.lmtzr.lemmatize(word.lower()) for word in re.findall(self.words, raw_sentence)
                  if word.lower() not in self.stopwords]
        tokens = [self.stemmer.stem(word) for word in tokens if len(word) > 2]
        return tokens

    def generate_tokens(self, raw_sentence):
        tokens = [word.lower() for word in re.findall(self.words, raw_sentence) if
                  word.lower() not in self.stopwords]
        return tokens


    def train_ngrams_models(self,sent_tokens):
        """
        Train bigrams,trigrams and dictionary and save them in cached models
        :param df: user's data-frame
        :param function_type: function type for which the analysis has to be done
        """
        bigrams = Phrases(sentences=sent_tokens, min_count=1, threshold=1)
        trigrams = Phrases(sentences=bigrams[sent_tokens], min_count=1, threshold=1)
        sent_tokens_transformed = trigrams[bigrams[sent_tokens]]
        d = corpora.Dictionary(sent_tokens_transformed)
        bow_corpus = [d.doc2bow(sent_tokens) for sent_tokens in sent_tokens_transformed]
        # d.filter_extremes(no_below=3, no_above=0.8)
        # d.compactify()
        tfidf = TfidfModel(corpus=bow_corpus, id2word=d)
        try:
            bigrams.save('slm/app/cached_models/bigrams.gensim')
            trigrams.save('slm/app/cached_models/trigrams.gensim')
            d.save('slm/app/cached_models/dictionary.dict')
            tfidf.save('slm/app/cached_models/tfidf.gensim')
        except:
            pass

    def train_word2vec_model(self,sentences):
        """
        Function to train Word2Vec model. The model is trained with a vector size on 300 and
        saved on physical memory for future references.
        :param sentences:list of tokenized sentences
        :return:
        """
        if len(sentences) > 0:
            model_file = "slm/app/cached_models/word2vec_model.gensim"
            if os.path.isfile(model_file):
                model = Word2Vec.load(model_file)
                try:
                    model.build_vocab(self.vectorize(sentences), update=True)
                    model.train(self.vectorize(sentences))
                except:
                    pass
                model.save(model_file)
                return "Existing model upgraded successfully"
            else:
                model = Word2Vec(size=300, window=2, min_count=2, workers=2)
                model.build_vocab(self.vectorize(sentences))
                model.train(self.vectorize(sentences))

                # model = Word2Vec(trigrams[bigrams[sentences]], size=200, window=5, min_count=5, workers=4)
                model.save(model_file)
                return "New model saved successfully Success"

    def vectorize(self,sent_token):
        """
        Function to vectorize titles of a user
        :param df: titles data-frame of a user
        :return: list of BOW transformed corpus for designation
        """
        sent_token = self.trigrams[self.bigrams[sent_token]]
        sent_vector = [self.dictionary.doc2bow(token) for token in sent_token]
        sent_vector = self.tfidf[sent_vector]
        sent_vector = matutils.corpus2dense(sent_vector, num_terms=len(self.dictionary.values()))
        return sent_vector.transpose()

    def get_vec_similarity(self, v1, v2):
        if len(np.nonzero(v1)[0]) == 0 or len(np.nonzero(v2)[0]) == 0:
            sim = 0.0
        else:
            sim = 1 - spatial.distance.cosine(v1, v2)
        return sim

    def data_parser_pos_tagging(self, sentences):
        """
        Parse data for POS
        :param sentences: sentence of Q/A in the form of string
        :return: POS tags Tree of the input
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
        To POS tag sentence for noun, adjective, verbs
        :param sentence:
        :param pos_noun_tags: Noun tag list
        :return: List of Nouns, Adjective and Verbs from current sentence added
        """
        for word, pos in pos_tag(sentence):
            if pos in ['NN', "NNP", "NNS"]:
                pos_noun_tags.append(word)
        return pos_noun_tags

    def data_parser_synonyms_extract_stopwords_cleaning(self, sentences):
        """
        Clean stopwords and extract synonyms for words
        :param sentences: sentence whose cleaning is to be performed
        :return: list of words and their synonyms
        """
        # For testing without contextual similarity
        sentence_with_synonyms = [words for words in sentences
                                  if words not in self.stopwords]
        sentence_with_synonyms = self.get_synonyms_of_words(sentence_with_synonyms)
        return sentence_with_synonyms

    def get_synonyms_of_words(self, sentence):
        """
        extract synonyms of words
        :param sentence: list of sentence
        :return: list of words with their synonyms
        """
        # word_list = [word.lower() for word in re.findall(self.words, sentence) if word not in self.stopwords]
        word_list_with_synonyms = []
        for word in sentence:
            word_list_with_synonyms.extend([word])
            for ss in wn.synsets(word):
                word_list_with_synonyms.extend(ss.lemma_names())
        return list(set(word_list_with_synonyms))

    def get_common_tokens(self, list1, list2):
        """
        calculates intersection of two list of words
        :param list1: list of words
        :param list2: list of words
        :return: lenght of common words
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

    @staticmethod
    def extract_terms_between_quotes(text):
        terms = re.findall(r'\"(.+?)\"', text.lower())
        return ",".join(terms)
