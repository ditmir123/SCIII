from mrjob.job import MRJob
import re

SENTENCE_REGEXP = re.compile(r'[.?!]')

class MRSentenceCount(MRJob):
    def mapper(self,_,line):
        sentences = SENTENCE_REGEXP.split(line)

        for sentence in sentences:
            if sentence.strip():
                yield 'Count of sentences',1
            
    def reducer(self,key,values):
        yield key,sum(values)


if __name__ == '__main__':
    MRSentenceCount.run()
