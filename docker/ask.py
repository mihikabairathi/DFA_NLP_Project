import coreNLPQuestionGenerator as cqg
import template_question_generator as tqg
import sys

article = sys.argv[1]
nquestions = int(sys.argv[2])

line_split_article = cqg.readFile(article)
f_ = open(article)
string_article = f_.read()
f_.close()

s = ''

s += cqg.generateQuestions(line_split_article)

s += tqg.generate_questions(string_article)

s = s.split('\n')
s = s[:nquestions]
s = '\n'.join(s)

sys.stdout.write(s)