from nose.tools import *
from ex48 import lexicon, parser

def test_sentence():
    s1 = parser.Sentence(('noun', "princess"), ('verb', "stop"), ('noun', "bear"))
    print(">>>s1.subject", s1.subject)
    print(">>> s1.verb", s1.verb)
    assert s1.subject == 'princess'
    assert s1.verb == 'stop'
    assert s1.object == 'bear'

def test_peek():
    word_list = []
    assert None == parser.peek(word_list)
    word_list = lexicon.scan("Princess Kill Bear")
    assert 'noun' == parser.peek(word_list)

def test_match():
    word_list = []
    assert None == parser.match(word_list, 'noun')
    word_list = lexicon.scan("Princess Kill Bear")
    assert None == parser.match(word_list, 'verb')
    assert ('verb', 'Kill') == parser.match(word_list, 'verb')

def test_skip():
    #word_list = []
    #assert None == parser.skip(word_list, 'stop')
    word_list = lexicon.scan("Bear kill the princess")
    print("WORD_LIST is ", word_list)
    #print("PEEK is ", parser.peek(word_list))
    #print("MATCH is", parser.match(word_list, 'noun'))
    #print("SKIP is ", parser.skip(word_list, 'noun'))
    assert ('noun', 'Bear') == parser.match(word_list, 'noun')
    assert ('verb', 'kill') == parser.match(word_list, 'verb')
    assert ('stop', 'the') == parser.match(word_list, 'stop')
    assert ('noun', 'princess') == parser.match(word_list, 'noun')
    assert None == parser.skip(word_list, 'stop')


def test_parse_verb():
    word_list = lexicon.scan("bear in cabinet")
    #print(word_list)
    #print("PARSE VERB is", parser.parse_verb(word_list))
    #assert ParserError("Expected a verb next") == parser.parse_verb(word_list)
    assert ('noun', 'bear') == parser.match(word_list, 'noun')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)


def test_parse_object():
    #word_list = lexicon.scan("princess kill the bear")
    #assert ('noun', 'princess') == parser.parse_object(word_list)
    word_list = lexicon.scan("kill the")
    assert_raises(parser.ParserError, parser.parse_object, word_list)


def test_parse_subject():
    #word_list = lexicon.scan("go north")
    #assert ('noun', 'player') == parser.parse_subject(word_list)
    word_list = lexicon.scan("in north")
    assert_raises(parser.ParserError, parser.parse_subject, word_list)

def test_parse_sentence():
    word_list = lexicon.scan("princess kill the bear")
    s = parser.parse_sentence(word_list)
    assert s.subject == 'princess'
    assert s.verb == 'kill'
    assert s.object == 'bear'
