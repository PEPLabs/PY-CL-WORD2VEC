from src.main.lab import sampleW2V, retrieveVector, sampleSimilarity, similarPairExercise, retrieveSimilarWordsExercise, w2vDoesntMatchExercise

if __name__ == '__main__':
    print('sample w2v function: ')
    sampleW2V()
    
    print(retrieveVector(''))

    print('sample similarity function: ')
    sampleSimilarity()

    print('similar pair exercise' ,similarPairExercise())
    print('retrieve similar words exercise: ',retrieveSimilarWordsExercise(1))

    print('w2v doesn\'t match exercise: ', w2vDoesntMatchExercise([]))